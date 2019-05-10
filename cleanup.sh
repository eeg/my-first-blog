#!/bin/bash

rm -rf db.sqlite3 mysite/__pycache__/ pubs/migrations/00* pubs/migrations/__pycache__ traits/migrations/00* traits/migrations/__pycache__

# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
# python manage.py runserver
