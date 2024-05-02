docker-compose-run:
	docker-compose up --build --abort-on-container-exit

tests:
	docker-compose exec app python3 manage.py test

clean-up:
	docker-compose down --volumes