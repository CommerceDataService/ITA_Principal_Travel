[![Stories in Ready](https://badge.waffle.io/CommerceDataService/ITA_Principal_Travel.png?label=ready&title=Ready)](https://waffle.io/CommerceDataService/ITA_Principal_Travel)
# ITA Principal Travel

## Prototype

### How to run

1. Install [Docker Toolbox](https://www.docker.com/products/docker-toolbox)
2. Run/open the Docker Quickstart Terminal
3. Run the following*:

```
docker-machine create -d virtualbox default
docker-machine start default
eval $(docker-machine env)
docker-compose build
docker-compose up -d
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

Place the ita_data.sql file (from a CDS team member-- it is .gitignored) in the /sql directory

Run:
    
    docker-compose run web python manage.py migrate
    docker-compose run db psql -h db -U postgres -f sql/ita_data.sql
    docker-compose run web python manage.py createsuperuser

The above will load the existing spreadsheet data and create a super-user in the DB so that you can log into the Django administration console.

Run:
    docker-compose run web python manage.py cities_light
    
The above will load the cities and countries from the cities_light module into the database tables so they are available for use in the form.
