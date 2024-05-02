tests:
	docker run --rm $(TEST_TAG) python3 manage.py test