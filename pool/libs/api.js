var redis = require('redis');
var async = require('async');

var stats = require('./stats.js');
const { resolve } = require('path');
const { callbackify } = require('util');

module.exports = function(logger, portalConfig, poolConfigs){
    var _this = this;

    var portalStats = this.stats = new stats(logger, portalConfig, poolConfigs);
    

    this.liveStatConnections = {};

    let rounds = {}
    let workerShares = {}
    this.handleApiRequest = function(req, res, next){
        // console.log('REDIS:PORT::'+JSON.stringify(poolConfigs['ergo'].redis.host)) // debug
        // coin = 'ergo'
        var client = redis.createClient(poolConfigs['ergo'].redis.port, poolConfigs['ergo'].redis.host)
        client.keys('*', function(err, keys) {
            for(var i=0, len=keys.length; i<len; i++) {
                //console.log('KEY::'+JSON.stringify(keys[i]));
                var k = keys[i].split(':')
                // check for key in format <coin>:shares:round<value>
                if (k[2] != undefined) { // good
                    if (k[2].substring(0, 5) == 'round') {
                        workerShares = {} // reset count since reloading (so doesn't add to previous values)
                        var j = k[2].substring(5)
                        client.hgetall(keys[i], function (err, obj) {
                            if (err) { console.log(err); }
                            else { 
                                rounds[j] = obj; 
                                for (o in obj) {
                                    let workerAddress = o.split('.')
                                    if (workerShares[workerAddress] == undefined) { workerShares[workerAddress[0]] = Number(obj[o]); }
                                    else { workerShares[workerAddress[0]] += Number(obj[o]); }
                                }
                            }
                        });
                    }
                }
            }
        });

        switch(req.params.method){

            case 'stats':
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(portalStats.statsString);
                return;

            case 'pool_stats':
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify(portalStats.statPoolHistory));
                return;

            case 'live_stats':
                res.writeHead(200, {
                    'Content-Type': 'text/event-stream',
                    'Cache-Control': 'no-cache',
                    'Connection': 'keep-alive'
                });
                res.write('\n');
                var uid = Math.random().toString();
                _this.liveStatConnections[uid] = res;
                req.on("close", function() {
                    delete _this.liveStatConnections[uid];
                });

                return;

            case 'worker':
                res.writeHead(200, { 'Content-Type': 'application/json' });
                //res.end('ROUNDS::'+JSON.stringify(rounds));
                res.end('WRKSHR::'+JSON.stringify(workerShares));
            default:
                next();
        }
    };


    this.handleAdminApiRequest = function(req, res, next){
        switch(req.params.method){
            case 'pools': {
                res.end(JSON.stringify({result: poolConfigs}));
                return;
            }
            default:
                next();
        }
    };

};
