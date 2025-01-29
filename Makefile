# Makefile

PROJECT_NAME = Docyuchat

help:
	@echo "Available commands:"
	@echo "make build        - Build Docker containers"
	@echo "make up           - Start containers in detached mode"
	@echo "make down         - Stop and remove containers"
	@echo "make migrate      - Run Django migrations"
	@echo "make makemigrations - Create new migrations"
	@echo "make shell        - Access Django shell"
	@echo "make test         - Run Django tests"
	@echo "make psql         - Access PostgreSQL database"
	@echo "make logs         - View container logs"
	@echo "make clean        - Remove all containers, volumes, and images"
	@echo "make createsuperuser - Create Django superuser"

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

migrate:
	docker-compose exec web python manage.py migrate

makemigrations:
	docker-compose exec web python manage.py makemigrations

shell:
	docker-compose exec web python manage.py shell

test:
	docker-compose exec web python manage.py test

psql:
	docker-compose exec db psql -U myuser -d mydb

logs:
	docker-compose logs -f

clean:
	docker-compose down -v --rmi all --remove-orphans

createsuperuser:
	docker-compose exec web python manage.py createsuperuser

startproject:
	docker-compose run web django-admin startproject $(PROJECT_NAME) .

.PHONY: help build up down migrate makemigrations shell test psql logs clean createsuperuser startproject
