import redis
import re
import requests
import json
import logging
import sqlite3
import pandas as pd
import uuid
import time

from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine

app = FastAPI()

origins = [
    "http://www.tulipfarm.one",
    "http://tulipfarm.one",
    "http://www.tulipfarm.one:2127",
    "http://tulipfarm.one:2127",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

###
### INIT
###
### CRITICAL 50
### ERROR 40
### WARNING 30
### INFO 20
### DEBUG 10
### NOTSET 0
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

rho = 'ergoredis'
rds = '6379'
nho = 'ergonode'
nod = '9052'
fee = 0.007 # pool fee .7%
rwd = 67.5 # current estimate, used for uncofirmed calc
hdr = {'api_key': 'oncejournalstrangeweather'}
tbl = 'payouts'
#db = 'payouts.db'
dbo = 'ergodb'
dbp = '5432'

minPayout = 10 # ergs

con = create_engine(f'postgresql://winter:t00lip@{dbo}:{dbp}/winter')
red = redis.StrictRedis(host=rho, port=rds, db=0, charset="utf-8", decode_responses=True)
adr = json.loads(requests.get(f'http://{nho}:{nod}/mining/rewardAddress').content)['rewardAddress']

###
### FUNCTIONS
###
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
        
        # add new shares to waiting status
        df = pd.DataFrame(rows, columns=['block', 'miner', 'worker', 'rig', 'status', 'workerShares', 'workerShares_erg', 'blockReward_sat', 'poolFee_pct', 'totalBlockShares', 'totalAmountAfterFee_sat', 'pendingBatchId', 'payoutBatchAmount_erg', 'paidTransactionId', '_timestampWaiting', '_timestampPending', '_timestampPaid'])
        if len(df) > 0:
            logging.info(f'saving {len(df)} new shares to database...')
            df.to_sql('payouts', if_exists='append', con=con, index=False)
        
        # update rounds so that are not counted again
        for round in rounds:
            logging.info(f'renaming redis key, ergo:shares:round{round}...')
            red.rename(f'ergo:shares:round{round}', f'ergo:shares:payout{round}')

    except Exception as e:
        logging.error(f'handleNewBlocks::{e}')

    return json.dumps(rows)


def ProcessPayouts():
    payments = []

    try:
        df = pd.read_sql_query("select * from payouts where status = 'waiting'", con=con)
        dfTotals = df.groupby(['worker'])['workerShares_erg'].sum().reset_index()
        dfPending = dfTotals[dfTotals['workerShares_erg'] >= minPayout]

        for r in dfPending.itertuples():
            logging.info(f'pay {r.workerShares_erg:.2f} ergs to worker, {r.worker}...')

            batch = str(uuid.uuid4())
            logging.debug(f'log payment info for {r.worker}, batch: {batch}')
            bdy = [{'address': r.worker, 'value': int(float(r.workerShares_erg)*1000000), 'assets': []}]
            logging.debug(f'{type(bdy)}; {bdy}')
            res = requests.post(f'http://{nho}:{nod}/wallet/payment/send', headers=hdr, json=bdy)
            if res.status_code == 200:
                logging.info(f'Payment sent: {json.loads(res.content)}')
                tid = res.json()
                payments.append({
                    'batch': batch,
                    'payoutBatchAmount_ergs': r.workerShares_erg,
                    'transactionId': tid,
                    'worker': r.worker,
                    'timestamp': datetime.now().isoformat(),
                    'status': 'pending'
                })
                with con.connect() as sql:
                    sql.execute(f"""
                        update {tbl} 
                        set "pendingBatchId" = '{batch}'
                            , "payoutBatchAmount_erg" = {r.workerShares_erg}
                            , "_timestampPending" = '{datetime.now().isoformat()}'
                            , "paidTransactionId" = '{json.loads(res.content)}'
                            , "status" = 'pending'
                        where worker = '{r.worker}'
                            and "status" = 'waiting'
                        """)
            else:
                logging.error(f'Payment not sent: STATUS CODE={res.status_code}::{res.json()}')

    except Exception as e:
        logging.error(f'handlePayouts::{e}')

    return json.dumps(payments)


def VerifyPayments():
    logging.debug('paid')


def GetMinerInfo(id):
    try:
        df = pd.read_sql_query(f"select * from payouts where worker = '{id}'", con=con)        

    except Exception as e:
        logging.error(e)

    return df.to_json(orient='records')


def GetMinerEarnings(id, minute):
    try:
        df = pd.read_sql_query(f"""
		    with tot as (
                    select distinct block, worker, "workerShares_erg"
						, case 
							when "_timestampPending" > current_timestamp - ({minute} * interval '1 minute') then 'pending'
							else 'waiting'
						end as status
                    from payouts
                    where "_timestampWaiting" > current_timestamp - ({minute} * interval '1 minute')
            )
            select "worker", "status", sum("workerShares_erg") as ergs
            from tot
            where worker = '{id}'
			group by "worker", "status"
            """, con=con)

        tot = 0
        shr = 0
        blk = 0
        for k in red.keys():             
            # only unconfirmed
            m = re.search('^ergo:shares:(?P<stype>round)(?P<round>\d+)$', k)
            if m:
                round = m.group('round')
                shares = red.hgetall(f'ergo:shares:round{round}')
                for s in shares:
                    share = int(shares[s])
                    blk += 1
                    # tally total blocks
                    tot += share
                    # tally miner blocks
                    if s.split('.')[0] == id:
                        shr += share
                blk += (shr/tot)*rwd-(fee*rwd)
        if tot > 0:
            df = df.append(pd.DataFrame([[id, f'unconfirmed {shr}', blk]], columns=['worker', 'status', 'ergs']))

        return df.to_json(orient='records')
    
    except Exception as e:
        logging.error(e)

    return (json.dumps({}))


def GetMiners():
    try:
        df = pd.read_sql_query(f"select distinct worker, rig from payouts", con=con)        

    except Exception as e:
        logging.error(e)

    return df.to_json(orient='records')


def ArchivePayments():
    logging.debug('paid')


def initPayouts():
    with con.connect() as sql:
        sql.execute("drop table payouts")

    with con.connect() as sql:
        sql.execute("""
            create table if not exists payouts (
                id integer not null primary key autoincrement,
                block text,
                miner text,
                worker text,
                rig text,
                status text,
                workerShares integer,
                workerShares_erg integer,
                blockReward_sat integer,
                poolFee_pct real,
                totalBlockShares integer,
                totalAmountAfterFee_sat integer,
                pendingBatchId text,
                payoutBatchAmount_erg real,
                paidTransactionId text,
                _timestampWaiting datetime,
                _timestampPending datetime,
                _timestampPaid datetime
            )
        """)


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
            logging.debug(k)
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
            logging.debug(blockDetails)
            res['row'][k] = {
                'dateMined': 0,
                'status': 'Pending',
                'reward': 0
            }
            if 'blockTransactions' in blockDetails:

                if 'transactions' in blockDetails['blockTransactions']:
                    for x in blockDetails['blockTransactions']['transactions']:

                        if 'outputs' in x:
                            for o in x['outputs']:

                                # transaction details
                                if o['transactionId'] == adr:
                                    round = str(o['creationHeight'])

                                    if round in blocks:
                                        res['row'][k] = {
                                            'dateMined': o['timestamp'],
                                            'status': 'Confirmed',
                                            'reward': float(o['value'])/1000000.0
                                        }
                        

    except Exception as e:
        logging.error(e)

    return json.dumps(res)

###
### ROUTES
###
@app.get("/")
def go_home():
    return {"Tulip": "Farm"}

# check redis for any new blocks that pool has mined
@app.get("/payout/block/info")
async def BlockInfo():
    return GetBlockInfo(False)

# check redis for any new blocks that pool has mined
@app.get("/payout/block/miner")
async def BlockMiner():
    return GetBlockInfo(True)

# new -> waiting
@app.get("/payout/block/process")
async def BlockProcess():
    return ProcessBlocks()

# archive old blocks already paid
@app.get("/payout/block/archive/{id}")
async def Archive(id):
    return {"archive": f"below height: {id}"}

# pay miners
@app.get("/payout/miner/process")
async def MinerProcess():
    return ProcessPayouts()

# miner info
@app.get("/payout/miner/{id}")
async def MinerInfo(id):
    return GetMinerInfo(id)

# miner earnings
@app.get("/payout/miner/earnings/{id}/{minute}")
async def MinerEarnings(id, minute):
    return GetMinerEarnings(id, minute)

# all miner/rig combos
@app.get("/payout/miners")
async def Miners():
    return GetMiners()

# archive old blocks already paid
@app.get("/payout/miner/verify")
async def MinerVerify():
    return {"miner": "verify"}

# site last blocks
@app.get("/stats/blocks/{startRow}/{endRow}")
async def StatsBlocks(startRow, endRow):
    return GetStatsBlocks(startRow, endRow)

###
### MAIN
###
#if __name__ == "__main__":
    #getBlockInfo()
