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

4. Take the output from the last command and access `<ip>:8000` in your web browser, where you should see a default Django page.

_* If the `docker-compose build` command hangs, we may need to investigate how to set up and use HTTP_PROXY._

### DB Initialization:

#### Initial migrations and admin setup

Run:
    
    docker-compose run web python manage.py migrate
    docker-compose run web python manage.py loaddata travel/fixtures/data_dump.json
    docker-compose run web python manage.py createsuperuser

The above will migrate the models to the database, load the dummy data, and create a super-user in the DB so that you can log into the Django administration console.

## Administration

Connect to the DB with psql:
    
```
docker-compose run db psql -h db -U postgres
```

Run management commands:

```   
docker-compose run web python manage.py <command>
```

Drop the entire database and start fresh:

```
chmod u+x wipe_db.sh
./wipe_db.sh
```

Wipe all data from database and start with original dataset (**note: this will wipe the auth tables so you will need to create a new superuser):

```
./reload_db.sh
```

## Troubleshooting

Ongoing development of the app in Docker means you need a few Docker tricks/commands.

If you add a requirement to requirements.txt, install the package via:

    docker-compose build web

If you ever get a ProtocolError during a `docker-compose build`, run:

    docker-machine restart default
    eval ($docker-machine env)

To check on whether your app containers are running (db and web):

    docker-machine ps

To start them both:

    docker-compose up -d

To restart one of them:

    docker-compose restart <db|web>

If you're trying to load the Django site in the browser and nothing is coming up, that means Django has been unable to start. You can look at Django's logs to diagnose the problem:

    docker-compose logs web
