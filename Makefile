run:
	docker-compose up -d

bash:
	docker exec -it imo_api bash

make:
	docker exec -it imo_api ./manage.py makemigrations

migrate:
	docker exec -it imo_api ./manage.py migrate

admin:
	docker exec -it imo_api ./manage.py createadmin

test:
	docker exec -it imo_api ./manage.py test --keepdb

coverage:
	docker exec -it imo_api coverage run manage.py test --keepdb

html:
	docker exec -it imo_api coverage html

logs:
	docker attach imo_api
