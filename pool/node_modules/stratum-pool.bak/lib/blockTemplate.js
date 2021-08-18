var bignum = require('bignum');

var merkleTree = require('./merkleTree.js');
var transactions = require('./transactions.js');
var util = require('./util.js');
var JSONbig = require('json-bigint');


/**
 * The BlockTemplate class holds a single job.
 * and provides several methods to validate and submit it to the daemon coin
**/
var BlockTemplate = module.exports = function BlockTemplate(jobId, rpcData, poolAddressScript, extraNoncePlaceholder, reward, txMessages, recipients){

    //private members
    // console.log('blocktemplate.rpcdata::'+JSON.stringify(rpcData))

    var submits = [];

    function getMerkleHashes(steps){
        return steps.map(function(step){
            return step.toString('hex');
        });
    }

    function getTransactionBuffers(txs){
        var txHashes = txs.map(function(tx){
            if (tx.txid !== undefined) {
                return util.uint256BufferFromHash(tx.txid);
            }
            return util.uint256BufferFromHash(tx.hash);
        });
        return [null].concat(txHashes);
    }

    function getVoteData(){
        if (!rpcData.masternode_payments) return new Buffer([]);

        return Buffer.concat(
            [util.varIntBuffer(rpcData.votes.length)].concat(
                rpcData.votes.map(function (vt) {
                    return new Buffer(vt, 'hex');
                })
            )
        );
    }

    //public members

    this.rpcData = rpcData;
    this.jobId = jobId;

    // console.log('rpcdata.b::'+rpcData.b) // debug
    this.target = rpcData.b ?
        bignum(rpcData.b, 10) :
        util.bignumFromBitsHex(rpcData.bits);
    // console.log('target::'+target); // debug

    this.difficulty = parseFloat((diff1 / this.target.toNumber()).toFixed(9));

    this.msg = Buffer.from(rpcData.msg, "hex");
    // this.prevHashReversed = util.reverseByteOrder(new Buffer(rpcData.previousblockhash, 'hex')).toString('hex');
    // this.transactionData = Buffer.concat(rpcData.transactions.map(function(tx){
    //     return new Buffer(tx.data, 'hex');
    // }));
    // this.merkleTree = new merkleTree(getTransactionBuffers(rpcData.transactions));
    // this.merkleBranch = getMerkleHashes(this.merkleTree.steps);
    // this.generationTransaction = transactions.CreateGeneration(
    //     rpcData,
    //     poolAddressScript,
    //     extraNoncePlaceholder,
    //     reward,
    //     txMessages,
    //     recipients
    // );

    this.serializeCoinbase = function(extraNonce1, extraNonce2){
        return Buffer.concat([
            this.msg,
            extraNonce1,
            extraNonce2
        ]);
    };


    //https://en.bitcoin.it/wiki/Protocol_specification#Block_Headers
    this.serializeHeader = function(merkleRoot, nTime, nonce){

        var header =  new Buffer(80);
        var position = 0;
        header.write(nonce, position, 4, 'hex');
        header.write(rpcData.bits, position += 4, 4, 'hex');
        header.write(nTime, position += 4, 4, 'hex');
        header.write(merkleRoot, position += 4, 32, 'hex');
        header.write(rpcData.previousblockhash, position += 32, 32, 'hex');
        header.writeUInt32BE(rpcData.version, position + 32);
        var header = util.reverseBuffer(header);
        // console.log('bits::'+rpcData.bits); // debug
        return header;
    };

    this.serializeBlock = function(header, coinbase){
        return Buffer.concat([
            header,

            util.varIntBuffer(this.rpcData.transactions.length + 1),
            coinbase,
            this.transactionData,

            getVoteData(),

            //POS coins require a zero byte appended to block which the daemon replaces with the signature
            new Buffer(reward === 'POS' ? [0] : [])
        ]);
    };

    this.registerSubmit = function(extraNonce1, extraNonce2, nTime, nonce){
        var submission = extraNonce1 + extraNonce2 + nTime + nonce;
        if (submits.indexOf(submission) === -1){
            submits.push(submission);
            return true;
        }
        return false;
    };

    this.getJobParams = function(){

        // console.log('b::'+rpcData.b) // debug
        if (!this.jobParams){
            this.jobParams = [
                this.jobId,
                this.rpcData.height,//this.prevHashReversed,
                this.rpcData.msg,// this.generationTransaction[0].toString('hex'),
                "",// this.generationTransaction[1].toString('hex'),
                "",// this.merkleBranch,
                this.rpcData.version,//  util.packInt32BE(this.rpcData.version).toString('hex'),
                rpcData.b, // nbits (encoded difficulty)
                "", //util.packUInt32BE(this.rpcData.curtime).toString('hex'),
                true
            ];
            // console.log('rpc.b/!jobParams::'+rpcData.b)
        }
        // console.log('jobParams::'+JSON.stringify(this.jobParams));
        return this.jobParams;
    };
};
