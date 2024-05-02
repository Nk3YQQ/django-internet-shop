tests:
	docker run --rm ${{ env.TEST_TAG }} python3 manage.py test