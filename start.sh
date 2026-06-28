#!/bin/sh

python manage.py migrate --noinput

gunicorn config.wsgi:application \
    --bind 0.0.0.0:8080 \
    --workers 3