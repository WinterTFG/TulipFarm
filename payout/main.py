from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Tulip": "Farm"}

# check redis for any new blocks that pool has mined
@app.get("/get/blocks")
def getBlockInfo():
    return {"get": "blocks"}

# get transactions with rewards
@app.get("/get/transactions")
def getBlockInfo():
    return {"get": "transactions"}

# move new blocks to waiting status
@app.get("/set/blocks/waiting")
def getBlockInfo():
    return {"set": "blocks.waiting"}

# assign payments to miners from waiting blocks
@app.get("/set/miners/pending")
def getBlockInfo():
    return {"set": "miners.pending"}

# pay miners
@app.get("/set/miners/payout")
def getBlockInfo():
    return {"set": "miners.payout"}

# validate miners were paid
@app.get("/set/miners/paid")
def getBlockInfo():
    return {"set": "miners.paid"}

