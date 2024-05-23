docker-compose-run:
	docker-compose up --build -d

tests:
	docker-compose exec -T app python3 manage.py test

clean-up:
	docker-compose down --volumes