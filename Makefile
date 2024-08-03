run:
	docker-compose up --build -d

run-test:
	docker-compose -f docker-compose.dev.yml up --build -d

entrypoint:
	python3 manage.py migrate
	python3 manage.py csu
	python3 manage.py create_moderator
	python3 manage.py ccm
	python3 manage.py cbc
	python3 manage.py collectstatic --noinput
	gunicorn --config gunicorn_config.py config.wsgi:application

tests:
	docker-compose -f docker-compose.dev.yml exec -T app python3 manage.py test

linters:
	docker-compose exec -T app flake8 blog/
	docker-compose exec -T app flake8 products/
	docker-compose exec -T app flake8 users/

stop:
	docker-compose down

clean:
	docker-compose -f docker-compose.dev.yml down --volumes