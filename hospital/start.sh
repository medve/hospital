#!/bin/sh

apt-get install django
python manage.py runserver 0.0.0.0:80
firefox 0.0.0.0:80
