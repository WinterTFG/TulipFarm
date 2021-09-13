import redis
import re, os
import requests
import json
import logging
import pandas as pd
import uuid

from datetime import datetime
from fastapi import FastAPI

###
### INIT
###
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

rho = os.environ.get('REDISHOST') # ergoredis
rds = os.environ.get('REDISPORT') # '6379'
nho = os.environ.get('NODEHOST')  # 'ergonode_testnet'
nod = os.environ.get('NODEPORT')  # '9052' # ?? make env
fee = os.environ.get('POOLFEE')   # 0.007 # pool fee .7%
hdr = {'api_key': os.environ.get('APIKEY')}
minPayout = os.environ.get('MINPAYOUT') # 10 # ergs

# con = create_engine(f'postgresql://winter:t00lip@{dbo}:{dbp}/winter')
red = redis.StrictRedis(host=rho, port=rds, db=0, charset="utf-8", decode_responses=True)
adr = json.loads(requests.get(f'http://{nho}:{nod}/mining/rewardAddress').content)['rewardAddress']

###
### FUNCTIONS
###
# from mhs_sam
def MinersRewardAtHeight(h):
    fixedRatePeriod       = 525600
    fixedRate             = 75000000000 # satoshis
    epochLength           = 64800 
    foundersInitialReward = 7500000000 # satoshis
    oneEpochReduction     = 3000000000 # satoshis

    if h < fixedRatePeriod + (2 * epochLength):
        return fixedRate - foundersInitialReward
    else:
        epoch = int(1 + (h - fixedRatePeriod) / epochLength)
        return int(max(fixedRate - oneEpochReduction * epoch, 0))


def GetBlockInfo(showMinerInfo=False):

    # red = redis.StrictRedis(host=rho, port=rds, db=0, charset="utf-8", decode_responses=True)
    xac = json.loads(requests.get(f'http://{nho}:{nod}/wallet/transactions?minInclusionHeight=0', headers=hdr).content)

    miners = {} # miner = worker.rig
    blocks = {}
    mrb = {0: 0} # most recent block; init blank

    try:
        # search all redis keys in this format
        for k in red.keys():             
            # match format using regex
            m = re.search('^ergo:shares:(?P<stype>round|payout)(?P<round>\d+)$', k)
            if m:
                round = m.group('round')
                stype = m.group('stype')
                miners[round] = {}
                blocks[round] = {
                    'fee': fee,
                    'totalShares': 0,
                    'rewardAmount_sat': 0,
                    'totalAmountAfterFee_sat': 0,
                    'status': 'unconfirmed',
                    'shareType': stype,
                    'difficulty': -1,
                    'timestamp': -1
                }                

                blockDetails = {}
                try:
                    blockHeader = json.loads(requests.get(f'http://{nho}:{nod}/blocks/at/{round}', headers=hdr).content)[0]
                    blockDetails = json.loads(requests.get(f'http://{nho}:{nod}/blocks/{blockHeader}', headers=hdr).content)

                    # keep what we can
                    if 'header' in blockDetails:
                        if 'timestamp' in blockDetails['header']: blocks[round]['timestamp'] = blockDetails['header']['timestamp']
                        if 'difficulty' in blockDetails['header']: blocks[round]['difficulty'] = blockDetails['header']['difficulty']

                except Exception as e:
                    logging.error(e)
                    pass

                # now sum shares by miner
                shares = red.hgetall(f'ergo:shares:round{round}')
                for s in shares:
                    share = int(shares[s])
                    # tally total blocks
                    blocks[round]['totalShares'] += share
                    # tally miner blocks
                    if s not in miners[round]: miners[round][s] = {'shares': 0}
                    miners[round][s]['shares'] += share # add shares                    
                    miners[round][s]['worker'] = s.split('.')[0]
                    if len(s.split('.')) == 1: miners[round][s]['rig'] = '' # only worker name
                    else: miners[round][s]['rig'] = s.split('.')[1] # worker.rig
                    miners[round][s]['shareType'] = 'round'

                # now sum shares by miner
                shares = red.hgetall(f'ergo:shares:payout{round}')
                for s in shares:
                    share = int(shares[s])
                    # tally total blocks
                    blocks[round]['totalShares'] += share
                    # tally miner blocks
                    if s not in miners[round]: miners[round][s] = {'shares': 0}
                    miners[round][s]['shares'] += share # add shares                    
                    miners[round][s]['worker'] = s.split('.')[0]
                    if len(s.split('.')) == 1: miners[round][s]['rig'] = '' # only worker name
                    else: miners[round][s]['rig'] = s.split('.')[1] # worker.rig
                    miners[round][s]['shareType'] = 'payout'

        # complete block information
        for x in xac:

            # search all transactions for payments to reward address
            for o in x['outputs']:

                # transaction details
                if o['address'] == adr:                        
                    round = str(o['creationHeight'])

                    if round in blocks:
                        blocks[round]['rewardAmount_sat'] = int(o['value']) # satoshis
                        blocks[round]['fee'] = fee
                        blocks[round]['totalAmountAfterFee_sat'] = int(o['value'] - o['value']*fee)

                    # scans=9 is confirmed
                    if 9 in x['scans']:
                        blocks[round]['status'] = 'confirmed'
                    else:
                        blocks[round]['status'] = 'unconfirmed'

        # find most recent block
        for b in blocks:
            mrb[blocks[b]['timestamp']] = b

    except Exception as e:
        logging.error(f'getTransactionInfo::{e}')

    if showMinerInfo:
        return json.dumps({'miners': miners, 'blocks': blocks, 'mostRecentBlock': {'block': mrb[max(mrb)], 'timestamp': max(mrb)}})
    else:
        return json.dumps(blocks)


def ProcessBlocks():
    try :
        blockInfo = json.loads(GetBlockInfo(True)) # convert result to dict
        miners = blockInfo['miners']
        blocks = blockInfo['blocks']
        rows = [] # prepare for dataframe
        rounds = {}

        for block in miners:

            for miner in miners[block]:

                # make sure there is an actual reward, and shareType = round (don't double pay)
                if (blocks[block]['rewardAmount_sat'] > 0) and (blocks[block]['shareType'] == 'round') and (miners[block][miner]['shareType'] == 'round'):
                    totalAmountAfterFee_sat = int(blocks[block]['rewardAmount_sat']) - (int(blocks[block]['rewardAmount_sat'])*fee)
                    workerShares_erg = (int(miners[block][miner]['shares'])/int(blocks[block]['totalShares'])) * totalAmountAfterFee_sat / 1000000
                    rows.append([block, miner, miners[block][miner]['worker'], miners[block][miner]['rig'], 'waiting', miners[block][miner]['shares'], workerShares_erg, blocks[block]['rewardAmount_sat'], fee, blocks[block]['totalShares'], totalAmountAfterFee_sat, '', 0.0, '', datetime.now().isoformat(), None, None])
                    rounds[block] = 0 # get distinct list; rather than append to list
        
        # update rounds so that are not counted again
        for round in rounds:
            logging.info(f'renaming redis key, ergo:shares:round{round}...')
            red.rename(f'ergo:shares:round{round}', f'ergo:shares:payout{round}')

    except Exception as e:
        logging.error(f'handleNewBlocks::{e}')

    return json.dumps(rows)

def ProcessPayouts():
    batch = str(uuid.uuid4())
    
    # add block/miner combo
    blocks = {}
    for k in red.keys():
        m = re.search('^ergo:shares:(?P<stype>round)(?P<round>\d+)$', k)
        if m:
            block = m.group('round')
            blocks[block] = red.hgetall(f'ergo:shares:round{block}')
    
    # remove block/miner already paid    
    for k in red.keys():
        m = re.search('^ergo:payout:(?P<stype>round)(?P<round>\d+)$', k)
        if m:
            block = m.group('round')
            rmv = red.hgetall(f'ergo:shares:round{block}')
            for r in rmv:
                if r in blocks[block]:
                    del blocks[block][r]

    # total shares by block
    miners = {}
    totals = {}
    for blk in blocks:
        if blk not in totals: totals[blk] = 0
        for mnr in blocks[blk]:
            shr = blocks[blk][mnr]
            totals[blk] += shr
            miner = mnr.split('.')[0]                
            if miner not in miners: miners[miner] = {}
            if blk in miners[miner]: miners[miner][blk] += shr
            else : miners[miner][blk] = shr

    # check for unpaid amounts by miner/block (worker=miner.rig)
    for m in miners:
        ergs = 0
        for b in miners[m]:
            blockReward = MinersRewardAtHeight(b) # calc reward
            blockReward_afterFee = blockReward - fee*blockReward # subtract fee
            ergs = blockReward_afterFee * (miners[m][b] / totals[b]) # find % of reward in ergs

        if ergs > minPayout:
            v = int(float(ergs)*1000000) # convert to satoshis
            bdy = [{'address': m, 'value': v, 'assets': []}]
            res = requests.post(f'http://{nho}:{nod}/wallet/payment/send', headers=hdr, json=bdy)

            # record payment to redis w/batch
            red.hset(f'ergo:payout:round{b}', m, v)


def GetStatsBlocks(st, nd):
    res = {
        'row': {},
        'totalRows': 0
    }
    try:
        totalRows = len(red.keys()) or 0
        nd = int(nd)
        st = int(st)
        res['totalRows'] = totalRows
        if nd >= totalRows:
            nd = totalRows
        blocks = {}
        for k in red.keys():
            m = re.search('^ergo:shares:(?P<stype>round|payout)(?P<round>\d+)$', k)
            if m:
                blocks[m.group('round')] = {
                    'block': 0,
                    'timestamp': 0,
                    'status': 'Confirmed',
                    'reward': 0.0
                }
        for k, v in list(reversed(sorted(blocks.items())))[st-1:nd-1]:
            blockHeader = json.loads(requests.get(f'http://{nho}:{nod}/blocks/at/{k}', headers=hdr).content)[0]
            blockDetails = json.loads(requests.get(f'http://{nho}:{nod}/blocks/{blockHeader}', headers=hdr).content)
            res['row'][k] = {
                'dateMined': 0,
                'status': 'Pending',
                'reward': 0
            }
            if 'blockTransactions' in blockDetails:

                if 'transactions' in blockDetails['blockTransactions']:

                    for trn in blockDetails['blockTransactions']['transactions']:

                        if 'outputs' in trn:
                            for o in trn['outputs']:
                                # logging.debug(o) 
                                # transaction details

                                res['row'][k] = {
                                    'dateMined': datetime.utcfromtimestamp(blockDetails['header']['timestamp']/1000).strftime("%Y/%m/%d %H:%M"),
                                    'status': 'Confirmed',
                                    'reward': float(o['value'])/1000000.0
                                }

                                if 'address' in o:
                                    if o['address'] != adr:
                                        round = str(o['creationHeight'])

                                        if round in blocks:
                                            res['row'][k] = {
                                                'dateMined': blockDetails['header']['timestamp'],
                                                'status': 'Confirmed',
                                                'reward': float(o['value'])/1000000.0
                                            }
                        

    except Exception as e:
        logging.error(e)

    return json.dumps(res)

