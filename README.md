# TulipFarm.one
Open source ERGO pool
## Quick start
Update config if needed:
> docker-compose[.testnet].yml

###
Start docker containers. Be sure to pass the API key for the stratum server:

> `> git clone https://github.com/WinterTFG/TulipFarm.git`<br>
> `> docker-compose up -e APIKEY HelloWorldMainnetKey`

Start on TESTNET
> `> docker-compose -f docker-compose.testnet.yml up -e APIKEY HelloWorldTestnetKey`

## Notes
1. recently rewritten to completely replace NOMP
1. localhost:8000/hello
1. stratum server is slightly modified: run tulip.js instead of start.js and the difficulty calc uses own method.

### TODO
1. Add healthcheck or similar so dependant containers connect properly (i.e. stratum check node and tulip; tulip check node is synchronized)
1. Handle restart and messaging better when ergostratul/tulip.js crashes

