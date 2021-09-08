troublshoot-tulipfarm.md
### Table of Contents
- /mining/candidate
- /info
- node logs
- stratum logs
- miner 
- ergo.json
- config.json

----------------------------------------------------------------------------------------------------------------------------------

# region /mining/candidate
{
  "msg": "4b3c7501d48ad49a2f68f4eb1edcdca39fa5fd489a8a06ffff77b71c14407940",
  "b": 3.479552295833598e+67,
  "h": 67556,
  "pk": "02946f31c13a75cb07571a63e860fa79ebd866278651cb1268d0c70c8c9beaaf4e"
}
# region /info
{
  "currentTime": 1631068950097,
  "name": "ergo-testnet-4.0.13",
  "stateType": "utxo",
  "difficulty": 3327787008,
  "bestFullHeaderId": "d51e0d6a1fd9829e77f8d0037e28ccf4b53b04e614e977c026ab8b9db2e6f387",
  "bestHeaderId": "d51e0d6a1fd9829e77f8d0037e28ccf4b53b04e614e977c026ab8b9db2e6f387",
  "peersCount": 6,
  "unconfirmedCount": 19,
  "appVersion": "4.0.13",
  "stateRoot": "e2306a47a9b9d5a19553cad88fce03521610d1ff5e6f27e6f21cee999798243713",
  "genesisBlockId": "78bc468ff36d5d6fa9707d382fe5b8947d6dd0ed2bc5c44707426ee12557c7fb",
  "previousFullHeaderId": "b7e5d363181d4509f40f43afcbc29f96761ff6cff804b66548b479f69b4c2106",
  "fullHeight": 67555,
  "headersHeight": 67555,
  "stateVersion": "d51e0d6a1fd9829e77f8d0037e28ccf4b53b04e614e977c026ab8b9db2e6f387",
  "fullBlocksScore": 745510496275615,
  "launchTime": 1630814393717,
  "lastSeenMessageTime": 1631068941249,
  "headersScore": 745510496275615,
  "parameters": {
    "outputCost": 100,
    "tokenAccessCost": 100,
    "maxBlockCost": 1000000,
    "height": 67456,
    "maxBlockSize": 524288,
    "dataInputCost": 100,
    "blockVersion": 2,
    "inputCost": 2000,
    "storageFeeFactor": 1250000,
    "minValuePerByte": 360
  },
  "isMining": true
}
# region node logs
2021-09-08 02:39:33 [POSIX]     [Connection Limit] (Safe to ignore) POSIX module not installed and resource (connection) limit was not raised
2021-09-08 02:39:33 [Master]    [CLI] CLI listening on port 17117
2021-09-08 02:39:33 [Master]    [PoolSpawner] Spawned 1 pool(s) on 1 thread(s)
2021-09-08 02:39:36 [Website]   [Server] Website started on 0.0.0.0:2127
(node:27) DeprecationWarning: (node-watch) First param in callback function  is replaced with event name since 0.5.0, use  `(evt, filename) => {}` if you want to get the filename
2021-09-08 02:39:36 [Switching] [Setup] (Thread 1) Loading last proxy state from redis
2021-09-08 02:39:36 [Pool]      [ergo] (Thread 1) Share processing setup with redis (ergoredis:6379)
invalid address length for 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG
2021-09-08 02:39:36 [Pool]      [ergo] (Thread 1) Error generating transaction output script for 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG in rewardRecipients
2021-09-08 02:39:36 [Pool]      [ergo] (Thread 1) No rewardRecipients have been setup which means no fees will be taken
2021-09-08 02:39:36 [Pool]      [ergo] (Thread 1) Stratum Pool Server Started for ergo [ERG] {blake}
                                                Network Connected:      Mainnet
                                                Detected Reward Type:   POW
                                                Current Block Height:   67556
                                                Current Connect Peers:  undefined
                                                Current Block Diff:     198.348535808
                                                Network Difficulty:     851913474048
                                                Network Hash Rate:      NaN KH
                                                Stratum Port(s):        8008, 8009
                                                Pool Fee Percent:       0%
                                                Block polling every:    1000 ms
2021-09-08 02:39:36 [Switching] [Setup] (blake) Setting proxy difficulties after pool start
2021-09-08 02:39:41 [Pool]      [ergo] (Thread 1) Unknown stratum method from 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]: mining.extranonce.subscribe
2021-09-08 02:39:41 [Pool]      [ergo] (Thread 1) Authorized 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif: [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
2021-09-08 02:39:57 [Pool]      [ergo] (Thread 1) Share accepted at diff 3888000000/0.774798968 by 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]
# region stratum logs
?? passed through to node

# region miner logs
trm/amd
nbminer/nvidia - nbminer -a ergo -o stratum+tcp://tulipfarm.one:8009 -u 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif --verbose

# region teamredminer/amd
# region nbminer/nvidia
C:\git\ErgoWinter\ErgoMiner\nbminer>nbminer -a ergo -o stratum+tcp://73.78.145.215:8009 -u 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif --verbose
[20:41:10] INFO - ----------------------------------------------
[20:41:10] INFO - |                                            |
[20:41:10] INFO - |                                            |
[20:41:10] INFO - |                                            |
[20:41:10] INFO - |                                            |
[20:41:10] INFO - |                                            |
[20:41:10] INFO - |                                            |
[20:41:10] INFO - |                                            |
[20:41:10] INFO - |         NBMiner - Crypto GPU Miner         |
[20:41:10] INFO - |                    38.1                    |
[20:41:10] INFO - |                                            |
[20:41:10] INFO - ----------------------------------------------
[20:41:10] INFO - ------------------- System -------------------
[20:41:10] INFO - OS:     Windows 10 Version 2009, 10.0.19042
[20:41:10] INFO - CPU:    Intel(R) Core(TM) i7-7740X CPU @ 4.30GHz
[20:41:10] INFO - RAM:    2982 MB / 16292 MB
[20:41:10] INFO - VMEM:   5889 MB / 63081 MB
[20:41:10] INFO - CU_DRV: 11.3, 466.77
[20:41:10] INFO - ------------------- Config -------------------
[20:41:10] INFO - ALGO:   ergo
[20:41:10] INFO - URL:    stratum+tcp://73.78.145.215:8118
[20:41:10] INFO - USER:   3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif
[20:41:10] INFO - TEMP:   limit 90C, start 85C
[20:41:10] INFO - ------------------- Device -------------------
[20:41:10] INFO -  |ID|PCI|  CC|Memory|CU|
[20:41:10] INFO - *| 0|  7|  86|24576M|82| NVIDIA GeForce RTX 3090
[20:41:10] INFO - ----------------------------------------------
[20:41:10] INFO - ergo - Logging in to 73.78.145.215:8118 ...
[20:41:10] INFO - ---- {"id":1,"method":"mining.subscribe","params":["NBMiner/38.1"]}
[20:41:10] INFO - ++++ {"error":null,"id":1,"result":[[["mining.set_difficulty","deadbeefcafebabe0100000000000000"],["mining.notify","deadbeefcafebabe0100000000000000"]],"18000000",4]}
[20:41:10] INFO - ++++ {"id":null,"method":"mining.set_difficulty","params":[1]}
[20:41:10] INFO - Set extranonce: 18000000
[20:41:10] INFO - ergo - Login succeeded.
[20:41:10] INFO - ---- {"id":2,"method":"mining.authorize","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif",""]}
[20:41:10] INFO - ---- {"id":3,"method":"mining.extranonce.subscribe","params":[]}
[20:41:10] INFO - API:  0.0.0.0:22333
[20:41:10] INFO - API server started.
[20:41:10] INFO - ++++ {"id":null,"method":"mining.notify","params":["1",67556,"4b3c7501d48ad49a2f68f4eb1edcdca39fa5fd489a8a06ffff77b71c14407940","","",2,"135284993262010285427150748018599928896600959960549022084399241183109392000000","",true]}
[20:41:10] INFO - ergo - New job: 73.78.145.215:8118, ID: 1, HEIGHT: 67556, DIFF:  5.000
[20:41:10] INFO - ++++ {"error":null,"id":2,"result":true}
[20:41:13] INFO - Device 0 started, Free mem = 23336 MB.
[20:41:15] INFO - Device 0 ready for height 67556, 2.10 s.
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051ff214","00000000","18000000051ff214"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051ff217","00000000","18000000051ff217"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051ff21c","00000000","18000000051ff21c"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051ff21f","00000000","18000000051ff21f"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051ff240","00000000","18000000051ff240"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051ff241","00000000","18000000051ff241"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051ff24d","00000000","18000000051ff24d"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051ff258","00000000","18000000051ff258"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051ff259","00000000","18000000051ff259"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051ff225","00000000","18000000051ff225"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051ff226","00000000","18000000051ff226"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051ff22a","00000000","18000000051ff22a"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051fe882","00000000","18000000051fe882"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051fe883","00000000","18000000051fe883"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051fe885","00000000","18000000051fe885"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051fe88e","00000000","18000000051fe88e"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051fe892","00000000","18000000051fe892"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051fe895","00000000","18000000051fe895"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051fe89b","00000000","18000000051fe89b"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051fe8a2","00000000","18000000051fe8a2"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051fe8b0","00000000","18000000051fe8b0"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051fe8d0","00000000","18000000051fe8d0"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051fe8d2","00000000","18000000051fe8d2"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051fe8d9","00000000","18000000051fe8d9"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051fe8e0","00000000","18000000051fe8e0"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051fe8e7","00000000","18000000051fe8e7"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051fe8f8","00000000","18000000051fe8f8"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051fe8f9","00000000","18000000051fe8f9"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051fe8ff","00000000","18000000051fe8ff"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051ff231","00000000","18000000051ff231"]}
[20:41:26] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","1","051ff23e","00000000","18000000051ff23e"]}
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #1 Share accepted, 13 ms. [DEVICE 0, #1]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #2 Share accepted, 17 ms. [DEVICE 0, #2]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #3 Share accepted, 17 ms. [DEVICE 0, #3]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #4 Share accepted, 21 ms. [DEVICE 0, #4]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #5 Share accepted, 23 ms. [DEVICE 0, #5]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #6 Share accepted, 26 ms. [DEVICE 0, #6]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #7 Share accepted, 28 ms. [DEVICE 0, #7]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #8 Share accepted, 33 ms. [DEVICE 0, #8]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #9 Share accepted, 35 ms. [DEVICE 0, #9]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #10 Share accepted, 36 ms. [DEVICE 0, #10]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #11 Share accepted, 40 ms. [DEVICE 0, #11]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #12 Share accepted, 41 ms. [DEVICE 0, #12]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #13 Share accepted, 43 ms. [DEVICE 0, #13]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #14 Share accepted, 44 ms. [DEVICE 0, #14]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #15 Share accepted, 49 ms. [DEVICE 0, #15]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #16 Share accepted, 49 ms. [DEVICE 0, #16]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #17 Share accepted, 64 ms. [DEVICE 0, #17]
[20:41:26] INFO - ergo - #18 Share accepted, 64 ms. [DEVICE 0, #18]
[20:41:26] INFO - ergo - #19 Share accepted, 64 ms. [DEVICE 0, #19]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #20 Share accepted, 64 ms. [DEVICE 0, #20]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #21 Share accepted, 65 ms. [DEVICE 0, #21]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #22 Share accepted, 70 ms. [DEVICE 0, #22]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #23 Share accepted, 71 ms. [DEVICE 0, #23]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #24 Share accepted, 73 ms. [DEVICE 0, #24]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #25 Share accepted, 78 ms. [DEVICE 0, #25]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #26 Share accepted, 80 ms. [DEVICE 0, #26]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #27 Share accepted, 81 ms. [DEVICE 0, #27]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #28 Share accepted, 83 ms. [DEVICE 0, #28]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #29 Share accepted, 85 ms. [DEVICE 0, #29]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #30 Share accepted, 89 ms. [DEVICE 0, #30]
[20:41:26] INFO - ++++ {"error":null,"id":4,"result":true}
[20:41:26] INFO - ergo - #31 Share accepted, 92 ms. [DEVICE 0, #31]

# region ergo.json
{
    "enabled": true,
    "coin": "ergo.json",

    // Address to where block rewards are given
    // "address": "9fEvBZmUBZsfxxXL3DH6uxdtB9WEM7gxegU6kzb7hbBGbkzLfo5", // mainnet
    "address": "3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG",

    "rewardRecipients": {
        // % to this address (i.e. 0.1 for 1%)
        // "9fEvBZmUBZsfxxXL3DH6uxdtB9WEM7gxegU6kzb7hbBGbkzLfo5": 1.0 // mainnet
        "3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG": 1.0
    },

    "paymentProcessing": {
        "enabled": false,
        "paymentInterval": 10, // seconds to check
        "minimumPayment": 10, // min coins to send payout
        "daemon": {
            "host": "ergonode",
            "port": 9052,
            "user": "ergo",
            "password": "ergo"
        }
    },

    "ports": {
        "8008": {
            "diff": 3999000000
        },

        "8009": {
            "diff": 3888000000,
            "multiplyDifficulty": true,
            "varDiff": {
                "minDiff":   1000000000,
                "maxDiff": 100000000000,
                "targetTime": 15,
                "retargetTime": 10,
                "variancePercent": 30
            }
        }
    },

    "daemons": [
        {
            "host": "ergonode",
            "port": 9052,
            "user": "ergo",
            "password": "ergo"
        }
    ],

    "p2p": {
        "enabled": false,
        "host": "ergonode",
        "port": 9052,
        "disableTransactions": true
    },

    "mposMode": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 3306,
        "user": "ergouser",
        "password": "ergopass",
        "database": "ergodb",
        "checkPassword": true,
        "autoCreateWorker": false
    }

}

# region config.json
{
    "logLevel": "debug",
    "logColors": true,

    "cliPort": 17117,

    "clustering": {
        "enabled": false,
        "forks": "auto"
    },

    "defaultPoolConfigs": {
        "blockRefreshInterval": 1000,
        "jobRebroadcastTimeout": 55,
        "connectionTimeout": 600,
        "emitInvalidBlockHashes": false,
        "validateWorkerUsername": true,
        "tcpProxyProtocol": false,
        "banning": {
            "enabled": false,
            "time": 600,
            "invalidPercent": 50,
            "checkThreshold": 500,
            "purgeInterval": 300
        },
        "redis": {
            "host": "ergoredis",
            "port": 6379
        }
    },

    "website": {
        "enabled": true,
        "host": "0.0.0.0",
        "port": 2127,
        "stratumHost": "tulipfarm.one",
        "stats": {
            "updateInterval": 60,
            "historicalRetention": 43200,
            "hashrateWindow": 300
        },
        "adminCenter": {
            "enabled": true,
            "password": "password"
        }
    },

    "redis": {
        "host": "ergoredis",
        "port": 6379
    },

    "switching": {
        "switch1": {
            "enabled": false,
            "algorithm": "sha256",
            "ports": {
                "3333": {
                    "diff": 10
                }
            }
        }
    },

    "profitSwitch": {
        "enabled": false,
        "updateInterval": 600,
        "depth": 0.90,
        "usePoloniex": false,
        "useCryptsy": false,
        "useMintpal": false,
        "useBittrex": false
    }
}

