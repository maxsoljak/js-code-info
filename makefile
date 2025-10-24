all:

dev-deps:
	pip3 install pytest-playwright==0.7.1 && playwright install

test:
	pytest
