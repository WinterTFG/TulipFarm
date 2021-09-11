import redis, uvicorn
# import re, requests, json
import time #, sys, os
from fastapi import FastAPI

import logging
logging.basicConfig(format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s", datefmt='%m-%d %H:%M', level=logging.DEBUG)

api = 'localhost' # localhost
rds = '6379'
coin = 'ergo'

app = FastAPI()
red = redis.StrictRedis(host=api, port=rds, db=0, charset="utf-8", decode_responses=True)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/share/{miner}/{height}/{difficulty}")
async def get_share(miner: str, height: int, difficulty: int):
    logging.info(f'share found by: {miner}, at block {height}')
    if difficulty > 0:
        red.hincrbyfloat(f'{coin}:shares:roundCurrent', miner, 1.0)
        red.hincrby(f'{coin}:stats', 'validShares', 1)
        red.lpush(f'{coin}:pplns{height}', miner.split('.')[0])
    else:
        red.hincrbyfloat(f'{coin}:stats', 'invalidShares', 1.0)
    epoch = time.time()
    red.zadd(f'{coin}:hashrate', epoch, f'{miner}:{epoch}:{difficulty}')

@app.get("/block/{miner}/{height}/{isValid}")
async def get_block(miner: str, height: int, isValid):
    logging.info(f'block found by: {miner}, at block {height}')
    if isValid:
        red.rename(f'{coin}:shares:roundCurrent', f'{coin}:shares:round{height}')
        red.sadd(f'{coin}:blocksPending', f'{miner}:{height}')
        red.hincrby(f'{coin}:stats', 'invalidBlocks', 1)
    else:
        red.hincrby(f'{coin}:stats', 'invalidBlocks', 1)

### MAIN
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
