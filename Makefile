docker-compose-run:
	docker-compose up --build
	docker-compose exec app python manage.py runserver 0.0.0.0:8000

tests:
	docker-compose exec app python3 manage.py test

clean-up:
	docker-compose down --volumes