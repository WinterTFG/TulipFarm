var Stratum = require('./lib');
var req = require('http');

// stat tracker
const host = process.env.TULIPHOST;
const port = process.env.TULIPPORT;

// stratum pool
var pool = Stratum.createPool({

    "coin": {
        "name": "Ergo",
        "symbol": "ERG",
        "algorithm": "blake",
        "reward": "POW"
    },
    "extraNonce1Size": 1,

    "address": "3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG", // who me da money
    "jobRebroadcastTimeout": 55,
    "connectionTimeout": 600, // seconds after which to remove
    "emitInvalidBlockHashes": false,
    "tcpProxyProtocol": false,
    "banning": {
        "enabled": true,
        "time": 600, // seconds
        "invalidPercent": 50, // below this % triggers ban
        "checkThreshold": 500, // check invalid percent when after threshold submitted
        "purgeInterval": 300 // seconds
    },
    "ports": {
        "8009": { 
            "diff": 2000000000, // starting difficulty
            "multiplyDifficulty": true,
            "varDiff": {
                "minDiff": 200000000, // min difficulty
                "maxDiff": 200000000000, // network difficultyused if it is lower
                "targetTime": 15, // apx. 1 share per this many seconds
                "retargetTime": 10, // seconds
                "variancePercent": 30 // allow time to vary this % from target without retargeting
            }
        },
        "8008": { 
            "diff": 2000000000
        }
    },
    "daemons": [
        {   // ergo node
            "host": process.env.NODEHOST,
            "port": process.env.NODEPORT,
            "user": "ergo", // not required
            "password": "ergo" // not required
        }
    ],
    "p2p": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 19333,
        "disableTransactions": true

    }

}

//stratum authorization function
, function(ip, port , workerName, password, callback){ 
    console.log("AUTH::" + workerName + ":" + password + "@" + ip + ":" + port);
    callback({
        error: null,
        authorized: true,
        disconnect: false
    });
});

/*
    job             : 4,              // stratum job ID
    ip              : '71.33.19.37',  // client
    port            : 3333,           // client
    worker          : 'matt.worker1', // stratum worker name
    height          : 443795,         // block height
    blockReward     : 5000000000,     // qty satoshis received as payment for solving this block
    difficulty      : 64,             // worker difficulty
    shareDiff       : 78,             // actual difficulty of the share
    blockDiff       : 3349,           // block difficulty adjusted for share padding
    blockDiffActual : 3349            // actual difficulty for this block

    // block solution - set if block was found
    blockHash: '110c0447171ad819dd181216d5d80f41e9218e25d833a2789cb8ba289a52eee4',

    // exists if "emitInvalidBlockHashes" is set to true
    blockHashInvalid: '110c0447171ad819dd181216d5d80f41e9218e25d833a2789cb8ba289a52eee4'

    // txHash is the coinbase transaction hash from the block
    txHash: '41bb22d6cc409f9c0bae2c39cecd2b3e3e1be213754f23d12c5d6d2003d59b1d,

    // set if share is rejected for some reason
    error: 'low share difficulty' 
*/

// share found
pool.on('share', function(isValidShare, isValidBlock, data) {

    try {
        worker     = data.worker || 'undefined';
        height     = data.height || -1;
        difficulty = data.difficulty || 0;

        if (isValidBlock)
            url = "http://"+host+":"+port+"/block/"+worker+"/"+height+"/1";
        else if (isValidShare)
            url = "http://"+host+":"+port+"/share/"+worker+"/"+height+"/"+difficulty;
        else if (data.blockHash)
            url = "http://"+host+":"+port+"/block/"+worker+"/"+height+"/0";
        else
            url = "http://"+host+":"+port+"/share/"+worker+"/"+height+"/"+(-1*difficulty);

        req.get(url, res => { console.log(res.statusCode); })
    } 
    
    catch (error) {
        console.error(error);
    }    
    
    console.log('::'+JSON.stringify(data));
});

// logging
pool.on('log', function(severity, logKey, logText) {
    console.log(severity + ': ' + '[' + logKey + '] ' + logText);
});

// var uint64be = require('uint64be')
pool.start();

