docker-compose-run:
	docker-compose up -d

tests:
	docker-compose exec app python3 manage.py test

clean-up:
	docker-compose down --volumes