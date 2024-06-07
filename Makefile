build-and-run:
	docker-compose up --build -d

tests:
	docker-compose exec -T app python3 manage.py test

linters:
	docker-compose exec -T app flake8 blogapp/
	docker-compose exec -T app flake8 shopapp/
	docker-compose exec -T app flake8 users/

stop:
	docker-compose down

clean-up:
	docker-compose down --volumes