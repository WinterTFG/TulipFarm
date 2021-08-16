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

###
### INIT
###
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

api = 'localhost' # localhost
rds = '6379'
nod = '9053'
fee = 0.007 # pool fee .7%
minPayout = 10 # ergs
hdr = {'api_key': 'oncejournalstrangeweather'}

red = redis.StrictRedis(host=api, port=rds, db=0, charset="utf-8", decode_responses=True)
adr = json.loads(requests.get(f'http://{api}:{nod}/mining/rewardAddress').content)['rewardAddress']
xac = json.loads(requests.get(f'http://{api}:{nod}/wallet/transactions?minInclusionHeight=0', headers=hdr).content)

db = 'payouts.db'
tbl = 'payouts'
con = sqlite3.connect(db)

miners = {} # miner = worker.rig
blocks = {}

###
### FUNCTIONS
###
def getBlockInfo():
    try:
        # search all redis keys in this format
        for k in red.keys(): 
            
            # match format using regex
            m = re.search('^ergo:shares:round(?P<round>\d+)$', k)
            if m:
                round = m.group('round')
                miners[round] = {}
                blocks[round] = {}
                blocks[round]['totalShares'] = 0
                blocks[round]['fee'] = fee
                blocks[round]['rewardAmount_sat'] = 0
                blocks[round]['totalAmountAfterFee_sat'] = 0
                
                # now sum shares by miner
                shares = red.hgetall(f'ergo:shares:round{round}')
                for s in shares:
                    share = int(shares[s])
                    blocks[round]['totalShares'] += share
                    try: 
                        if s in miners[round]:
                            miners[round][s] += share # add shares
                        else:
                            miners[round][s] = share # add shares
                    except ValueError: 
                        logging.error('not an int')
                    miners[round][s] = {}
                    miners[round][s]['worker'] = s.split('.')[0]
                    if len(s.split('.')) == 2: 
                        miners[round][s]['rig'] = s.split('.')[1]
                    else:
                        miners[round][s]['rig'] = ''
                    miners[round][s]['shares'] = share # add shares

    except Exception as e:
        logging.error(f'getBlockInfo::{e}')

def getTransactionInfo():
    try:
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


def handleNewBlocks():
    try :
        rows = []
        rounds = {}
        for block in miners:
            for miner in miners[block]:
                if blocks[block]['rewardAmount_sat'] > 0:
                    totalAmountAfterFee_sat = int(blocks[block]['rewardAmount_sat']) - (int(blocks[block]['rewardAmount_sat'])*fee)
                    workerShares_erg = (int(miners[block][miner]['shares'])/int(blocks[block]['totalShares'])) * totalAmountAfterFee_sat / 1000000000
                    rows.append([block, miner, miners[block][miner]['worker'], miners[block][miner]['rig'], 'waiting', miners[block][miner]['shares'], workerShares_erg, blocks[block]['rewardAmount_sat'], fee, blocks[block]['totalShares'], totalAmountAfterFee_sat, '', 0.0, '', datetime.now().isoformat(), '', ''])
                    rounds[block] = 0
        
        # add new shares to waiting status
        logging.info('saving new shares to database...')
        df = pd.DataFrame(rows, columns=['block', 'miner', 'worker', 'rig', 'status', 'workerShares', 'workerShares_erg', 'blockReward_sat', 'poolFee_pct', 'totalBlockShares', 'totalAmountAfterFee_sat', 'pendingBatchId', 'payoutBatchAmount_erg', 'paidTransactionId', '_timestampWaiting', '_timestampPending', '_timestampPaid'])
        if len(df) > 0:
            df.to_sql('payouts', if_exists='append', con=con, index=False)
        
        # update rounds so that are not counted again
        for round in rounds:
            logging.info(f'renaming redis key, ergo:shares:round{round}...')
            red.rename(f'ergo:shares:round{round}', f'ergo:shares:payout{round}')

    except Exception as e:
        logging.error(f'handleNewBlocks::{e}')

def handlePayouts():
    try:
        df = pd.read_sql_query("select * from payouts where status = 'waiting'", con=con)
        dfTotals = df.groupby(['worker'])['workerShares_erg'].sum().reset_index()
        dfPending = dfTotals[dfTotals['workerShares_erg'] >= minPayout]

        for r in dfPending.itertuples():
            logging.info(f'make payment to worker, {r.worker}...')

            batch = str(uuid.uuid4())
            logging.debug(f'log payment info for {r.worker}, batch: {batch}')
            bdy = [{'address': r.worker, 'value': int(r.workerShares_erg*1000000000), 'assets': []}]
            res = requests.post(f'http://{api}:{nod}/wallet/payment/send', headers=hdr, json=bdy)
            if res.status_code = 200:
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

def verifyPayment():
    logging.degub('paid')

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
### MAIN
###
if __name__ == "__main__":

    while True:
        try:
            # logging.warning('initPayouts...')
            # initPayouts()

            logging.warning('getBlockInfo...')
            getBlockInfo()
            logging.warning('getTransactionInfo...')
            getTransactionInfo()
            logging.warning('handleNewBlocks...')
            handleNewBlocks()
            logging.warning('handlePayouts...')
            handlePayouts()
            logging.warning('verifyPayment...')
            verifyPayment()

            logging.warning('sleeping...')
            time.sleep(5*60)

        except:
            continue
