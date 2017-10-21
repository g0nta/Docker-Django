# Docker-Django
## What's this repository
This repository is a django template project on docker.
## How to start
```
$docker-compose build
$docker-compose up -d
```
## Migration
```
$docker-compose exec web python manage.py makemigrations
$docker-compose exec web python manage.py migrate
```

## Create admin user
```
$docker-compose exec python manage.py createsuperuser
```
