# ERGO Winter

## Quick start

> `> git clone https://github.com/WinterTFG/TulipFarm.git`<br>
> `> docker-compose up`

Start on TESTNET
> `> docker-compose -f docker-compose.testnet.yml up`

## Notes
1. The DEV and TESTNET compose scripts map the local volumes and change entrypoint to use nodemon for quicker development.  Be sure to npm INSIDE the docker if you are in dev since the Dockerfile node_modules will be hidden.
1. ergoredis, ergonode, and ergopool are all valid names ONLY WITHIN thier containers when they are started from the docker compose.
1. The PaymentProcessor has been disabled and will be rebuilt outside this work (perhaps included in separate docker).

## TODO
> - Heartbeat for server and proxy to connect more elegantly
> - Stratum server: Add vardiff
> - Payment Processor: Add PPLNS optional functionality
> - Website: IP auth for min payouts
> - Website: Search by worker name, not just Erg address
> - Website: Better responsive tables for mobile, and obfuscicate worker addresses
> - Website: Add block effort calculations for home page and worker page
> - Website: Auto-generate config files for popular mining software (NBMiner, T-Rex, TeamRedMiner, lolminer)
> - Website: Worker page only show list of workers searched for, not all workers
> - Website: Add clean error handling for search, undisplayed data, and loading visual

