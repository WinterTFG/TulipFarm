import redis, uvicorn
# import re, requests, json, uuid
import time, os #, sys

from payout import *

from datetime import datetime, timedelta
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from typing import Optional

#region LOGGING
import logging
logging.basicConfig(format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s", datefmt='%m-%d %H:%M', level=logging.DEBUG)
#endregion LOGGING

#region INIT
api = os.environ.get('REDISHOST') # ergoredis
rds = os.environ.get('REDISPORT') # '6379'
coin = os.environ.get('COIN') # 'ergo'
coins = {
    'ergo': {
        'symbol': 'ERG',
        'algorithm': 'autolykos2'
    }
}
secInDay = 24*60*60 # 1 day
today = time.time()
# timewindow1 = today - oneday # 1 day
# timewindow3 = today - 3*oneday # 1 day

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

red = redis.StrictRedis(host=api, port=rds, db=0, charset="utf-8", decode_responses=True)
#endregion INIT

@app.get("/hello")
async def root():
    return {"Tulip": "Farm"}

#region PAYOUT API
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
#@app.get("/payout/miner/{id}")
#async def MinerInfo(id):
#    return GetMinerInfo(id)
#
## miner earnings
#@app.get("/payout/miner/earnings/{id}")
#async def MinerEarnings(id, minute: Optional[int] = None):
#    return GetMinerEarnings(id, minute)
#
## all miner/rig combos
#@app.get("/payout/miners")
#async def Miners():
#    return GetMiners()

# site last blocks
@app.get("/stats/blocks/{startRow}/{endRow}")
async def StatsBlocks(startRow, endRow):
    return GetStatsBlocks(startRow, endRow)
#endregion PAYOUT API

#region SHARE API
@app.get("/share/{miner}/{height}/{difficulty}")
async def get_share(miner: str, height: int, difficulty: int):
    logging.info(f'share found by: {miner}, at block {height}')
    if difficulty > 0:
        red.hincrbyfloat(f'{coin}:shares:roundCurrent', miner, 1.0)
        red.hincrby(f'{coin}:stats', 'validShares', 1)
        red.lpush(f'{coin}:pplns:round{height}', miner.split('.')[0])
    else:
        red.hincrbyfloat(f'{coin}:stats', 'invalidShares', 1.0)
    epoch = time.time()
    red.zadd(f'{coin}:hashrate', {f'{difficulty}:{miner}:{epoch}': epoch})

@app.get("/block/{miner}/{height}/{isValid}")
async def get_block(miner: str, height: int, isValid):
    logging.info(f'block found by: {miner}, at block {height}')
    if isValid:
        red.rename(f'{coin}:shares:roundCurrent', f'{coin}:shares:round{height}')
        red.delete('ergo:stats') # shares/blocks current block
        red.sadd(f'{coin}:blocksPending', f'{miner}:{height}')
        red.hincrby(f'{coin}:stats', 'invalidBlocks', 1)
    else:
        red.hincrby(f'{coin}:stats', 'invalidBlocks', 1)
#endregion

#region STATS API
@app.get("/api/pool_stats")
async def get_poolstats():
    workers = {}
    workerCount = {}
    stats = red.zrangebyscore('ergo:hashrate', today-secInDay, '+inf')
    for stat in stats:
        h, w, e = stat.split(':')
        if w in workers: 
            workers[w] += int(h)
            workerCount[w] += 1
        else: 
            workers[w] = int(h)
            workerCount[w] = 1

    hashrate = {}
    totalHashrate = 0
    for w in workers:
        hashrate[w] = workers[w] / workerCount[w]
        totalHashrate += hashrate[w]

    res = {
        "time": int(time.time()), # ??
        "pools": {
            "ergo": {
                "hashrate": totalHashrate,
                "workerCount": len(workers.keys()),
                "blocks": {
                    "pending": 0,
                    "confirmed": 0,
                    "orphaned": 0
                }
            }
        }
    }

    return res

def GetPrettyHash(hashrate):
    units = ["H", "K", "M", "G", "T", "P", "E", "Y", "Z"]
    i = 0
    try:
        h = float(hashrate)
        while h > 1000.0 and i <= 8:
            i += 1
            h /= 1000.0
    except:
        pass
    return f'{h:0.2f}{units[i]}H/s'
    

@app.get("/api/stats")
async def get_stats():
    red.zremrangebyscore('ergo:hashrate', '-inf', today-3*secInDay) # cleanup
    stats = red.hgetall('ergo:stats')
    round = red.hgetall('ergo:shares:roundCurrent')
    hashrates = red.zrangebyscore('ergo:hashrate', today-secInDay, '+inf')
    workers = {}
    workerCount = {}    
    for hashrate in hashrates:
        h, w, e = hashrate.split(':')
        if w in workers: 
            workers[w] += float(h)
            workerCount[w] += 1
        else: 
            workers[w] = float(h)
            workerCount[w] = 1

    hashrate = {}
    totalHashrate = 0
    algoHashrate = 0
    poolHashrate = 0
    workerList = {}
    # for coin in coins ...
    for w in workers:
        hashrate[w] = workers[w] / workerCount[w]
        totalHashrate += hashrate[w]
        # if coin == coin: algoHashrate += hashrate[w]
        # if pool == pool: poolHashrate += hashrate[w]
        workerList[w] = {
            "shares": int(round[w] if w in round else 0),
            "invalidshares": 0,
            "hashrateString": GetPrettyHash(hashrate[w])
        }
    res = {
        "time": int(time.time()), # ??
        "global": {
            "workers": len(workers.keys()),
            "hashrate": totalHashrate
        },
        "algos": {
            "blake": {
                "workers": len(workers.keys()),
                "hashrate": totalHashrate,
                "hashrateString": GetPrettyHash(totalHashrate) # algoHashrate
            }
        },
        "pools": {
            coin: {
                "name": coin,
                "symbol": coins[coin]['symbol'],
                "algorithm": coins[coin]['algorithm'],
                "poolStats": {
                    "validShares": stats['validShares'] if 'validShares' in stats else '',
                    "validBlocks": stats['validBlocks'] if 'validBlocks' in stats else '',
                    "invalidShares": stats['invalidShares'] if 'invalidShares' in stats else '',
                    "totalPaid": stats['invalidBlocks'] if 'invalidBlocks' in stats else ''
                },
                "blocks": {
                    "pending": 0,
                    "confirmed": 0,
                    "orphaned": 0
                },
                "workers": workerList,
                "hashrate": totalHashrate,
                "workerCount": len(workers.keys()),
                "hashrateString": GetPrettyHash(totalHashrate) # poolHashrate
            }
        },        
    }

    return res
#endregion 

#region MAIN
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
#endregion
