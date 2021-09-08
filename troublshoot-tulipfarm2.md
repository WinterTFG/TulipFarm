troublshoot-tulipfarm.md

Table of Contents
=== /mining/candidate
=== /info
=== node logs
=== stratum logs
=== miner 
=== config.json

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
  "currentTime": 1631068621947,
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
  "lastSeenMessageTime": 1631068611655,
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
2021-09-08 02:31:08 [POSIX]     [Connection Limit] (Safe to ignore) POSIX module not installed and resource (connection) limit was not raised
2021-09-08 02:31:08 [Master]    [CLI] CLI listening on port 17117
2021-09-08 02:31:09 [Master]    [PoolSpawner] Spawned 1 pool(s) on 1 thread(s)
2021-09-08 02:31:11 [Website]   [Server] Website started on 0.0.0.0:2127
(node:26) DeprecationWarning: (node-watch) First param in callback function  is replaced with event name since 0.5.0, use  `(evt, filename) => {}` if you want to get the filename
2021-09-08 02:31:11 [Switching] [Setup] (Thread 1) Loading last proxy state from redis
2021-09-08 02:31:11 [Pool]      [ergo] (Thread 1) Share processing setup with redis (ergoredis:6379)
invalid address length for 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG
2021-09-08 02:31:11 [Pool]      [ergo] (Thread 1) Error generating transaction output script for 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG in rewardRecipients
2021-09-08 02:31:11 [Pool]      [ergo] (Thread 1) No rewardRecipients have been setup which means no fees will be taken
2021-09-08 02:31:11 [Pool]      [ergo] (Thread 1) Stratum Pool Server Started for ergo [ERG] {blake}
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
2021-09-08 02:31:11 [Switching] [Setup] (blake) Setting proxy difficulties after pool start
2021-09-08 02:31:39 [Pool]      [ergo] (Thread 1) Unknown stratum method from 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif [::ffff:172.18.0.1]: mining.extranonce.subscribe
2021-09-08 02:31:39 [Pool]      [ergo] (Thread 1) Authorized 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif: [::ffff:172.18.0.1]
2021-09-08 02:32:06 [Pool]      [ergo] (Thread 1) No new blocks for 55 seconds - updating transactions & rebroadcasting work
2021-09-08 02:32:34 [Pool]      [ergo] (Thread 1) Share rejected: {"job":"2","ip":"::ffff:172.18.0.1","worker":"3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","difficulty":3999000000,"error":"incorrect size of extra nonce2"}
2021-09-08 02:33:01 [Pool]      [ergo] (Thread 1) No new blocks for 55 seconds - updating transactions & rebroadcasting work
2021-09-08 02:33:09 [Pool]      [ergo] (Thread 1) Share rejected: {"job":"3","ip":"::ffff:172.18.0.1","worker":"3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","difficulty":3999000000,"error":"incorrect size of extra nonce2"}
2021-09-08 02:33:52 [Pool]      [ergo] (Thread 1) Share rejected: {"job":"3","ip":"::ffff:172.18.0.1","worker":"3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","difficulty":3999000000,"error":"incorrect size of extra nonce2"}
2021-09-08 02:33:53 [Pool]      [ergo] (Thread 1) Share rejected: {"job":"3","ip":"::ffff:172.18.0.1","worker":"3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","difficulty":3999000000,"error":"incorrect size of extra nonce2"}
2021-09-08 02:33:56 [Pool]      [ergo] (Thread 1) No new blocks for 55 seconds - updating transactions & rebroadcasting work
2021-09-08 02:34:05 [Pool]      [ergo] (Thread 1) Share rejected: {"job":"4","ip":"::ffff:172.18.0.1","worker":"3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","difficulty":3999000000,"error":"incorrect size of extra nonce2"}
2021-09-08 02:34:10 [Pool]      [ergo] (Thread 1) Share rejected: {"job":"4","ip":"::ffff:172.18.0.1","worker":"3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","difficulty":3999000000,"error":"incorrect size of extra nonce2"}
2021-09-08 02:34:14 [Pool]      [ergo] (Thread 1) Share rejected: {"job":"4","ip":"::ffff:172.18.0.1","worker":"3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","difficulty":3999000000,"error":"incorrect size of extra nonce2"}
2021-09-08 02:34:23 [Pool]      [ergo] (Thread 1) Share rejected: {"job":"4","ip":"::ffff:172.18.0.1","worker":"3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","difficulty":3999000000,"error":"incorrect size of extra nonce2"}
2021-09-08 02:34:31 [Pool]      [ergo] (Thread 1) Share rejected: {"job":"4","ip":"::ffff:172.18.0.1","worker":"3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","difficulty":3999000000,"error":"incorrect size of extra nonce2"}
2021-09-08 02:34:35 [Pool]      [ergo] (Thread 1) Share rejected: {"job":"4","ip":"::ffff:172.18.0.1","worker":"3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","difficulty":3999000000,"error":"incorrect size of extra nonce2"}
2021-09-08 02:34:40 [Pool]      [ergo] (Thread 1) Share rejected: {"job":"4","ip":"::ffff:172.18.0.1","worker":"3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","difficulty":3999000000,"error":"incorrect size of extra nonce2"}
2021-09-08 02:34:51 [Pool]      [ergo] (Thread 1) No new blocks for 55 seconds - updating transactions & rebroadcasting work
2021-09-08 02:35:15 [Pool]      [ergo] (Thread 1) Share rejected: {"job":"5","ip":"::ffff:172.18.0.1","worker":"3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","difficulty":3999000000,"error":"incorrect size of extra nonce2"}
2021-09-08 02:35:46 [Pool]      [ergo] (Thread 1) No new blocks for 55 seconds - updating transactions & rebroadcasting work
# region stratum logs
?? passed through to node

# region miner logs
trm/amd
nbminer/nvidia - nbminer -a ergo -o stratum+tcp://tulipfarm.one:8118 -u 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif --verbose

# region teamredminer/amd
# region nbminer/nvidia
C:\git\ErgoWinter\ErgoMiner\nbminer>nbminer -a ergo -o stratum+tcp://73.78.145.215:8118 -u 3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif --verbose
[20:33:08] INFO - ----------------------------------------------
[20:33:08] INFO - |                                            |
[20:33:08] INFO - |                                            |
[20:33:08] INFO - |                                            |
[20:33:08] INFO - |                                            |
[20:33:08] INFO - |                                            |
[20:33:08] INFO - |                                            |
[20:33:08] INFO - |                                            |
[20:33:08] INFO - |         NBMiner - Crypto GPU Miner         |
[20:33:08] INFO - |                    38.1                    |
[20:33:08] INFO - |                                            |
[20:33:08] INFO - ----------------------------------------------
[20:33:08] INFO - ------------------- System -------------------
[20:33:08] INFO - OS:     Windows 10 Version 2009, 10.0.19042
[20:33:08] INFO - CPU:    Intel(R) Core(TM) i7-7740X CPU @ 4.30GHz
[20:33:08] INFO - RAM:    2785 MB / 16292 MB
[20:33:08] INFO - VMEM:   5899 MB / 63081 MB
[20:33:08] INFO - CU_DRV: 11.3, 466.77
[20:33:08] INFO - ------------------- Config -------------------
[20:33:08] INFO - ALGO:   ergo
[20:33:08] INFO - URL:    stratum+tcp://73.78.145.215:8118
[20:33:08] INFO - USER:   3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif
[20:33:08] INFO - TEMP:   limit 90C, start 85C
[20:33:08] INFO - ------------------- Device -------------------
[20:33:08] INFO -  |ID|PCI|  CC|Memory|CU|
[20:33:08] INFO - *| 0|  7|  86|24576M|82| NVIDIA GeForce RTX 3090
[20:33:08] INFO - ----------------------------------------------
[20:33:08] INFO - ergo - Logging in to 73.78.145.215:8118 ...
[20:33:08] INFO - ---- {"id":1,"method":"mining.subscribe","params":["NBMiner/38.1"]}
[20:33:08] INFO - ++++ {"error":null,"id":1,"result":[[["mining.set_difficulty","deadbeefcafebabe0100000000000000"],["mining.notify","deadbeefcafebabe0100000000000000"]],"28000000",4]}
[20:33:08] INFO - Set extranonce: 28000000
[20:33:08] INFO - ergo - Login succeeded.
[20:33:08] INFO - ---- {"id":2,"method":"mining.authorize","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif",""]}
[20:33:08] INFO - ---- {"id":3,"method":"mining.extranonce.subscribe","params":[]}
[20:33:08] INFO - API:  0.0.0.0:22333
[20:33:08] INFO - API server started.
[20:33:08] INFO - ++++ {"id":null,"method":"mining.set_difficulty","params":[3999000000]}
[20:33:08] INFO - ++++ {"id":null,"method":"mining.notify","params":["1",67556,"4b3c7501d48ad49a2f68f4eb1edcdca39fa5fd489a8a06ffff77b71c14407940","","",2,"34795522958335978762127250004783932329372674886972485104012150510059","",true]}
[20:33:08] INFO - ergo - New job: 73.78.145.215:8118, ID: 1, HEIGHT: 67556, DIFF: 3.328G
[20:33:08] INFO - ++++ {"error":null,"id":2,"result":true}
[20:33:11] INFO - Device 0 started, Free mem = 23336 MB.
[20:33:13] INFO - Device 0 ready for height 67556, 2.08 s.
[20:33:35] INFO - ++++ {"id":null,"method":"mining.notify","params":["2",67556,"4b3c7501d48ad49a2f68f4eb1edcdca39fa5fd489a8a06ffff77b71c14407940","","",2,"34795522958335978762127250004783932329372674886972485104012150510059","",false]}
[20:33:35] INFO - ergo - New job: 73.78.145.215:8118, ID: 2, HEIGHT: 67556, DIFF: 3.328G
[20:33:38] INFO - ==================== [v38.1] Summary 2021-09-07 20:33:38 ====================
[20:33:38] INFO - |ID|Device|Hashrate|Accept|Reject|Inv|Powr|Temp|Fan|CClk|GMClk|MUtl|Eff/Watt|
[20:33:38] INFO - | 0|  3090| 114.7 M|     0|     0|  0| 357|  71|  0|1740|10297|  69| 321.2 K|
[20:33:38] INFO - |------------------+------+------+---+----+---------------------------------|
[20:33:38] INFO - |    Total: 114.7 M|     0|     0|  0| 357| Uptime:  0D 00:00:30   CPU: 21% |
[20:33:38] INFO - =============================================================================
[20:33:38] INFO - ergo - On Pool   10m:  0.000    4h:  0.000    24h:  0.000
[20:34:03] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","2","157ce059a","00000000","2800000157ce059a"]}
[20:34:03] INFO - ++++ {"error":[20,"incorrect size of extra nonce2"],"id":4,"result":null}
[20:34:03] INFO - ergo - #1 Share rejected: {"error":[20,"incorrect size of extra nonce2"]}, 10 ms. [DEVICE 0, #1]
[20:34:08] INFO - ==================== [v38.1] Summary 2021-09-07 20:34:08 ====================
[20:34:08] INFO - |ID|Device|Hashrate|Accept|Reject|Inv|Powr|Temp|Fan|CClk|GMClk|MUtl|Eff/Watt|
[20:34:08] INFO - | 0|  3090| 115.3 M|     0|     1|  0| 351|  72|  0|1830|10297|  66| 328.6 K|
[20:34:08] INFO - |------------------+------+------+---+----+---------------------------------|
[20:34:08] INFO - |    Total: 115.3 M|     0|     1|  0| 351| Uptime:  0D 00:01:00   CPU: 21% |
[20:34:08] INFO - =============================================================================
[20:34:08] INFO - ergo - On Pool   10m:  0.000    4h:  0.000    24h:  0.000
[20:34:30] INFO - ++++ {"id":null,"method":"mining.notify","params":["3",67556,"4b3c7501d48ad49a2f68f4eb1edcdca39fa5fd489a8a06ffff77b71c14407940","","",2,"34795522958335978762127250004783932329372674886972485104012150510059","",false]}
[20:34:30] INFO - ergo - New job: 73.78.145.215:8118, ID: 3, HEIGHT: 67556, DIFF: 3.328G
[20:34:38] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","3","24c59147a","00000000","280000024c59147a"]}
[20:34:38] INFO - ++++ {"error":[20,"incorrect size of extra nonce2"],"id":4,"result":null}
[20:34:38] INFO - ergo - #2 Share rejected: {"error":[20,"incorrect size of extra nonce2"]}, 12 ms. [DEVICE 0, #2]
[20:34:38] INFO - ==================== [v38.1] Summary 2021-09-07 20:34:38 ====================
[20:34:38] INFO - |ID|Device|Hashrate|Accept|Reject|Inv|Powr|Temp|Fan|CClk|GMClk|MUtl|Eff/Watt|
[20:34:38] INFO - | 0|  3090| 115.4 M|     0|     2|  0| 360|  71|  0|1860|10297|  69| 320.6 K|
[20:34:38] INFO - |------------------+------+------+---+----+---------------------------------|
[20:34:38] INFO - |    Total: 115.4 M|     0|     2|  0| 360| Uptime:  0D 00:01:30   CPU: 21% |
[20:34:38] INFO - =============================================================================
[20:34:38] INFO - ergo - On Pool   10m:  0.000    4h:  0.000    24h:  0.000
[20:35:08] INFO - ==================== [v38.1] Summary 2021-09-07 20:35:08 ====================
[20:35:08] INFO - |ID|Device|Hashrate|Accept|Reject|Inv|Powr|Temp|Fan|CClk|GMClk|MUtl|Eff/Watt|
[20:35:08] INFO - | 0|  3090| 114.6 M|     0|     2|  0| 355|  71|  0|1875|10297|  69| 322.8 K|
[20:35:08] INFO - |------------------+------+------+---+----+---------------------------------|
[20:35:08] INFO - |    Total: 114.6 M|     0|     2|  0| 355| Uptime:  0D 00:02:00   CPU: 20% |
[20:35:08] INFO - =============================================================================
[20:35:08] INFO - ergo - On Pool   10m:  0.000    4h:  0.000    24h:  0.000
[20:35:21] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","3","371bee5dd","00000000","2800000371bee5dd"]}
[20:35:21] INFO - ++++ {"error":[20,"incorrect size of extra nonce2"],"id":4,"result":null}
[20:35:21] INFO - ergo - #3 Share rejected: {"error":[20,"incorrect size of extra nonce2"]}, 7 ms. [DEVICE 0, #3]
[20:35:21] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","3","376351611","00000000","2800000376351611"]}
[20:35:21] INFO - ++++ {"error":[20,"incorrect size of extra nonce2"],"id":4,"result":null}
[20:35:21] INFO - ergo - #4 Share rejected: {"error":[20,"incorrect size of extra nonce2"]}, 7 ms. [DEVICE 0, #4]
[20:35:25] INFO - ++++ {"id":null,"method":"mining.notify","params":["4",67556,"4b3c7501d48ad49a2f68f4eb1edcdca39fa5fd489a8a06ffff77b71c14407940","","",2,"34795522958335978762127250004783932329372674886972485104012150510059","",false]}
[20:35:25] INFO - ergo - New job: 73.78.145.215:8118, ID: 4, HEIGHT: 67556, DIFF: 3.328G
[20:35:33] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","4","3c6c0c862","00000000","28000003c6c0c862"]}
[20:35:33] INFO - ++++ {"error":[20,"incorrect size of extra nonce2"],"id":4,"result":null}
[20:35:33] INFO - ergo - #5 Share rejected: {"error":[20,"incorrect size of extra nonce2"]}, 17 ms. [DEVICE 0, #5]
[20:35:38] INFO - ==================== [v38.1] Summary 2021-09-07 20:35:38 ====================
[20:35:38] INFO - |ID|Device|Hashrate|Accept|Reject|Inv|Powr|Temp|Fan|CClk|GMClk|MUtl|Eff/Watt|
[20:35:38] INFO - | 0|  3090| 114.7 M|     0|     5|  0| 360|  71|  0|1785|10297|  71| 318.6 K|
[20:35:38] INFO - |------------------+------+------+---+----+---------------------------------|
[20:35:38] INFO - |    Total: 114.7 M|     0|     5|  0| 360| Uptime:  0D 00:02:30   CPU: 20% |
[20:35:38] INFO - =============================================================================
[20:35:38] INFO - ergo - On Pool   10m:  0.000    4h:  0.000    24h:  0.000
[20:35:39] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","4","3ea4c39ae","00000000","28000003ea4c39ae"]}
[20:35:39] INFO - ++++ {"error":[20,"incorrect size of extra nonce2"],"id":4,"result":null}
[20:35:39] INFO - ergo - #6 Share rejected: {"error":[20,"incorrect size of extra nonce2"]}, 5 ms. [DEVICE 0, #6]
[20:35:42] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","4","403c8d8c0","00000000","2800000403c8d8c0"]}
[20:35:42] INFO - ++++ {"error":[20,"incorrect size of extra nonce2"],"id":4,"result":null}
[20:35:42] INFO - ergo - #7 Share rejected: {"error":[20,"incorrect size of extra nonce2"]}, 6 ms. [DEVICE 0, #7]
[20:35:52] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","4","44623cb94","00000000","280000044623cb94"]}
[20:35:52] INFO - ++++ {"error":[20,"incorrect size of extra nonce2"],"id":4,"result":null}
[20:35:52] INFO - ergo - #8 Share rejected: {"error":[20,"incorrect size of extra nonce2"]}, 9 ms. [DEVICE 0, #8]
[20:36:00] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","4","47a60ee95","00000000","280000047a60ee95"]}
[20:36:00] INFO - ++++ {"error":[20,"incorrect size of extra nonce2"],"id":4,"result":null}
[20:36:00] INFO - ergo - #9 Share rejected: {"error":[20,"incorrect size of extra nonce2"]}, 12 ms. [DEVICE 0, #9]
[20:36:03] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","4","4910ef69b","00000000","28000004910ef69b"]}
[20:36:03] INFO - ++++ {"error":[20,"incorrect size of extra nonce2"],"id":4,"result":null}
[20:36:03] INFO - ergo - #10 Share rejected: {"error":[20,"incorrect size of extra nonce2"]}, 8 ms. [DEVICE 0, #10]
[20:36:08] INFO - ==================== [v38.1] Summary 2021-09-07 20:36:08 ====================
[20:36:08] INFO - |ID|Device|Hashrate|Accept|Reject|Inv|Powr|Temp|Fan|CClk|GMClk|MUtl|Eff/Watt|
[20:36:08] INFO - | 0|  3090| 113.2 M|     0|    10|  0| 356|  71|  0|1875|10297|  68| 318.0 K|
[20:36:08] INFO - |------------------+------+------+---+----+---------------------------------|
[20:36:08] INFO - |    Total: 113.2 M|     0|    10|  0| 356| Uptime:  0D 00:03:00   CPU: 27% |
[20:36:08] INFO - =============================================================================
[20:36:08] INFO - ergo - On Pool   10m:  0.000    4h:  0.000    24h:  0.000
[20:36:09] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","4","4b745f8a9","00000000","28000004b745f8a9"]}
[20:36:09] INFO - ++++ {"error":[20,"incorrect size of extra nonce2"],"id":4,"result":null}
[20:36:09] INFO - ergo - #11 Share rejected: {"error":[20,"incorrect size of extra nonce2"]}, 9 ms. [DEVICE 0, #11]
[20:36:20] INFO - ++++ {"id":null,"method":"mining.notify","params":["5",67556,"4b3c7501d48ad49a2f68f4eb1edcdca39fa5fd489a8a06ffff77b71c14407940","","",2,"34795522958335978762127250004783932329372674886972485104012150510059","",false]}
[20:36:20] INFO - ergo - New job: 73.78.145.215:8118, ID: 5, HEIGHT: 67556, DIFF: 3.328G
[20:36:38] INFO - ==================== [v38.1] Summary 2021-09-07 20:36:38 ====================
[20:36:38] INFO - |ID|Device|Hashrate|Accept|Reject|Inv|Powr|Temp|Fan|CClk|GMClk|MUtl|Eff/Watt|
[20:36:38] INFO - | 0|  3090| 112.6 M|     0|    11|  0| 352|  71|  0|1875|10297|  68| 319.8 K|
[20:36:38] INFO - |------------------+------+------+---+----+---------------------------------|
[20:36:38] INFO - |    Total: 112.6 M|     0|    11|  0| 352| Uptime:  0D 00:03:30   CPU: 26% |
[20:36:38] INFO - =============================================================================
[20:36:38] INFO - ergo - On Pool   10m:  0.000    4h:  0.000    24h:  0.000
[20:36:44] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","5","5a3c8c393","00000000","28000005a3c8c393"]}
[20:36:44] INFO - ++++ {"error":[20,"incorrect size of extra nonce2"],"id":4,"result":null}
[20:36:44] INFO - ergo - #12 Share rejected: {"error":[20,"incorrect size of extra nonce2"]}, 9 ms. [DEVICE 0, #12]
[20:37:08] INFO - ==================== [v38.1] Summary 2021-09-07 20:37:08 ====================
[20:37:08] INFO - |ID|Device|Hashrate|Accept|Reject|Inv|Powr|Temp|Fan|CClk|GMClk|MUtl|Eff/Watt|
[20:37:08] INFO - | 0|  3090| 111.6 M|     0|    12|  0| 354|  71|  0|1845|10297|  68| 315.4 K|
[20:37:08] INFO - |------------------+------+------+---+----+---------------------------------|
[20:37:08] INFO - |    Total: 111.6 M|     0|    12|  0| 354| Uptime:  0D 00:04:00   CPU: 26% |
[20:37:08] INFO - =============================================================================
[20:37:08] INFO - ergo - On Pool   10m:  0.000    4h:  0.000    24h:  0.000
[20:37:15] INFO - ++++ {"id":null,"method":"mining.notify","params":["6",67556,"4b3c7501d48ad49a2f68f4eb1edcdca39fa5fd489a8a06ffff77b71c14407940","","",2,"34795522958335978762127250004783932329372674886972485104012150510059","",false]}
[20:37:15] INFO - ergo - New job: 73.78.145.215:8118, ID: 6, HEIGHT: 67556, DIFF: 3.328G
[20:37:38] INFO - ==================== [v38.1] Summary 2021-09-07 20:37:38 ====================
[20:37:38] INFO - |ID|Device|Hashrate|Accept|Reject|Inv|Powr|Temp|Fan|CClk|GMClk|MUtl|Eff/Watt|
[20:37:38] INFO - | 0|  3090| 109.8 M|     0|    12|  0| 354|  71|  0|1920|10297|  59| 310.2 K|
[20:37:38] INFO - |------------------+------+------+---+----+---------------------------------|
[20:37:38] INFO - |    Total: 109.8 M|     0|    12|  0| 354| Uptime:  0D 00:04:30   CPU: 27% |
[20:37:38] INFO - =============================================================================
[20:37:38] INFO - ergo - On Pool   10m:  0.000    4h:  0.000    24h:  0.000
[20:37:44] INFO - ---- {"id":4,"method":"mining.submit","params":["3WwjaerfwDqYvFwvPRVJBJx2iUvCjD2jVpsL82Zho1aaV5R95jsG.leif","6","730d342cd","00000000","2800000730d342cd"]}
[20:37:44] INFO - ++++ {"error":[20,"incorrect size of extra nonce2"],"id":4,"result":null}
[20:37:44] INFO - ergo - #13 Share rejected: {"error":[20,"incorrect size of extra nonce2"]}, 10 ms. [DEVICE 0, #13]

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

