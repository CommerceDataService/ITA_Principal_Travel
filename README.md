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

### Administration

Connect to the DB with psql:
    docker-compose run db psql -h db -U postgres

Run management commands:
   docker-compose run web python manage.py <command>

Wipe the database and start fresh:
    chmod u+x wipe_db.sh
    ./wipe_db.sh

## DB Initialization:

Place the ita_data.sql file in the /sql directory

Run:
    
    docker-compose run db python manage.py migrate
    docker-compose run db psql -h db -U postgres -f sql/ita_data.sql
    docker-compose run db python manage.py createsuperuser

_Note: The ita_data.sql is being .gitignored. Get the file from a CDS team member._
