.PHONY: all

all:
	python3 setup.py sdist bdist_wheel

test:
	python3 -m twine upload --repository testpypi dist/*

upload:
	python3 -m twine upload  dist/*
