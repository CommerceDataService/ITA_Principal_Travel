# ITA_Principal_Travel

Discovery phase
* survey
* look over materials
* demo ITA central
* draft questions

## Prototype

### How to run

1. Install [Docker Toolbox](https://www.docker.com/products/docker-toolbox)
2. Run/open the Docker Quickstart Terminal
3. Run the following*:

```
eval $(docker-machine env)
docker-machine create -d virtualbox default
docker-machine start default
docker-compose build
docker-compose up
docker-machine ip
```

4. Take the output from the last command and access <ip>:8000 in your web browser, where you should see a default Django page.

_* If the `docker-compose build` command hangs, we may need to investigate how to set up and use HTTP_PROXY._

