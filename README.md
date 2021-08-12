# ERGO Winter

## Quick start

> `> git clone https://github.com/WinterTFG/TulipFarm.git`<br>
> `> docker-compose up`

Start on TESTNET
> `> docker-compose -f docker-compose.testnet.yml up`

## Notes
1. The DEV and TESTNET compose scripts map the local volumes and change entrypoint to use nodemon for quicker development.  Be sure to npm INSIDE the docker if you are in dev since the Dockerfile node_modules will be hidden.
1. ergoredis, ergonode, and ergopool are all valid names ONLY WITHIN thier containers when they are started from the docker compose.

## TODO
> - heartbeat for server and proxy to connect more elegantly

