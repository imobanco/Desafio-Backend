run:
	docker-compose up -d

bash:
	docker exec -it imo_api bash

make:
	docker exec -it imo_api ./manage.py makemigrations

migrate:
	docker exec -it imo_api ./manage.py migrate

logs:
	docker attach imo_api