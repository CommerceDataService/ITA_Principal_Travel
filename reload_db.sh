docker-compose run web python manage.py flush --no-input && docker-compose run web python manage.py loaddata travel/fixtures/data_dump.json
