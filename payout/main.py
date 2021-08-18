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

app = FastAPI()

###
### INIT
###
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

rho = 'ergoredis'
rds = '6379'
nho = 'ergonode'
nod = '9052'
fee = 0.007 # pool fee .7%
hdr = {'api_key': 'oncejournalstrangeweather'}
tbl = 'payouts'
db  = 'payouts.db'
minPayout = 10 # ergs

###
### FUNCTIONS
###
def GetBlockInfo():

    red = redis.StrictRedis(host=rho, port=rds, db=0, charset="utf-8", decode_responses=True)
    adr = json.loads(requests.get(f'http://{nho}:{nod}/mining/rewardAddress').content)['rewardAddress']
    xac = json.loads(requests.get(f'http://{nho}:{nod}/wallet/transactions?minInclusionHeight=0', headers=hdr).content)

    miners = {} # miner = worker.rig
    blocks = {}

    try:
        # search all redis keys in this format
        for k in red.keys():             
            # match format using regex
            m = re.search('^ergo:shares:round(?P<round>\d+)$', k)
            if m:
                round = m.group('round')
                miners[round] = {}
                blocks[round] = {
                    'fee': fee,
                    'totalShares': 0,
                    'rewardAmount_sat': 0,
                    'totalAmountAfterFee_sat': 0
                }                
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

        # complete block information
        for x in xac:

            # search all transactions for payments to reward address
            for o in x['outputs']:

                # only accept with scans=9
                if 9 in x['scans']:

                    # transaction details
                    if o['address'] == adr:                        
                        round = str(o['creationHeight'])
                        if round in blocks:
                            blocks[round]['rewardAmount_sat'] = int(o['value']) # satoshis
                            blocks[round]['fee'] = fee
                            blocks[round]['totalAmountAfterFee_sat'] = int(o['value'] - o['value']*fee)

    except Exception as e:
        logging.error(f'getTransactionInfo::{e}')

    return json.dumps({'miners': miners, 'blocks': blocks})


def ProcessBlocks():
    con = sqlite3.connect(db)
    red = redis.StrictRedis(host=rho, port=rds, db=0, charset="utf-8", decode_responses=True)

    try :
        blockInfo = json.loads(GetBlockInfo()) # convert result to dict
        miners = blockInfo['miners']
        blocks = blockInfo['blocks']
        rows = [] # prepare for dataframe
        rounds = {}
        for block in miners:
            for miner in miners[block]:
                if blocks[block]['rewardAmount_sat'] > 0:
                    totalAmountAfterFee_sat = int(blocks[block]['rewardAmount_sat']) - (int(blocks[block]['rewardAmount_sat'])*fee)
                    workerShares_erg = (int(miners[block][miner]['shares'])/int(blocks[block]['totalShares'])) * totalAmountAfterFee_sat / 1000000000
                    rows.append([block, miner, miners[block][miner]['worker'], miners[block][miner]['rig'], 'waiting', miners[block][miner]['shares'], workerShares_erg, blocks[block]['rewardAmount_sat'], fee, blocks[block]['totalShares'], totalAmountAfterFee_sat, '', 0.0, '', datetime.now().isoformat(), '', ''])
                    rounds[block] = 0 # get distinct list; rather than append to list
        
        # add new shares to waiting status
        df = pd.DataFrame(rows, columns=['block', 'miner', 'worker', 'rig', 'status', 'workerShares', 'workerShares_erg', 'blockReward_sat', 'poolFee_pct', 'totalBlockShares', 'totalAmountAfterFee_sat', 'pendingBatchId', 'payoutBatchAmount_erg', 'paidTransactionId', '_timestampWaiting', '_timestampPending', '_timestampPaid'])
        if len(df) > 0:
            logging.info('saving new shares to database...')
            df.to_sql('payouts', if_exists='append', con=con, index=False)
        
        # update rounds so that are not counted again
        for round in rounds:
            logging.info(f'renaming redis key, ergo:shares:round{round}...')
            red.rename(f'ergo:shares:round{round}', f'ergo:shares:payout{round}')

    except Exception as e:
        logging.error(f'handleNewBlocks::{e}')

    return json.dumps(rows)


def ProcessPayouts():
    con = sqlite3.connect(db)
    payments = []

    try:
        df = pd.read_sql_query("select * from payouts where status = 'waiting'", con=con)
        dfTotals = df.groupby(['worker'])['workerShares_erg'].sum().reset_index()
        dfPending = dfTotals[dfTotals['workerShares_erg'] >= minPayout]

        for r in dfPending.itertuples():
            logging.info(f'make payment to worker, {r.worker}...')

            batch = str(uuid.uuid4())
            logging.debug(f'log payment info for {r.worker}, batch: {batch}')
            bdy = [{'address': r.worker, 'value': int(r.workerShares_erg*1000000000), 'assets': []}]
            res = requests.post(f'http://{nho}:{nod}/wallet/payment/send', headers=hdr, json=bdy)
            logging.info(f'Payment sent: {json.loads(res.content)}')
            if res.status_code == 200:
                payments.append({
                    'batch': batch,
                    'payoutBatchAmount_ergs': r.workerShares_erg,
                    'totalBatchShares': -1,
                    'totalBatchReward': 67.5,
                    'transactionId': json.loads(res.content),
                    'shares': r.shares,
                    'worker': r.worker,
                    'rig': r.rig,
                    'timestamp': datetime.now().isoformat(),
                    'status': 'pending'
                })
                with sqlite3.connect(db) as sql:
                    sql.execute(f"""
                        update {tbl} 
                        set pendingBatchId = '{batch}'
                            , payoutBatchAmount_erg = {r.workerShares_erg}
                            , _timestampPending = '{datetime.now().isoformat()}'
                            , paidTransactionId = '{json.loads(res.content)}'
                            , status = 'pending'
                        where worker = '{r.worker}'
                            and status = 'waiting'
                        """)
            else:
                logging.error(f'Payment not sent: {res.content}')

    except Exception as e:
        logging.error(f'handlePayouts::{e}')

    return json.dumps(payments)


def VerifyPayments():
    logging.debug('paid')


def GetMinerInfo(id):
    con = sqlite3.connect(db)

    try:
        df = pd.read_sql_query(f"select * from payouts where worker = '{id}'", con=con)        

    except Exception as e:
        logging.error(e)

    return df.to_json(orient='records')

def GetMiners():
    con = sqlite3.connect(db)

    try:
        df = pd.read_sql_query(f"select distinct worker, rig from payouts", con=con)        

    except Exception as e:
        logging.error(e)

    return df.to_json(orient='records')

def ArchivePayments():
    logging.debug('paid')


def initPayouts():
    db = 'payouts.db'
    with sqlite3.connect(db) as sql:
        sql.execute("drop table payouts")

    with sqlite3.connect(db) as sql:
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


###
### ROUTES
###
@app.get("/")
def go_home():
    return {"Tulip": "Farm"}

# check redis for any new blocks that pool has mined
@app.get("/payout/block/info")
async def BlockInfo():
    return GetBlockInfo()

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

# all miner/rig combos
@app.get("/payout/miners")
async def Miners():
    return GetMiners()

# archive old blocks already paid
@app.get("/payout/miner/verify")
async def MinerVerify():
    return {"miner": "verify"}

###
### MAIN
###
#if __name__ == "__main__":
    #getBlockInfo()
