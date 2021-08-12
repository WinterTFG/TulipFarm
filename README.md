# ERGO Winter

## Quick start

> `> git clone https://github.com/WinterTFG/TulipFarm.git`<br>
> `> docker-compose -f docker-compose.dev.yml up`

## Steps
1. git clone node, stratum and proxy into folders as is (or just download jar for node, perhaps?)
1. Update ergo.conf with proper hash api (or use existing)
1. docker compose up in main folder
1. wait til node is up and server is connected and then docker restart ergoproxy

## TODO
> - heartbeat for server and proxy to connect more elegantly

