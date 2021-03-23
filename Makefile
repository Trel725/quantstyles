wheel:
	python setup.py sdist bdist_wheel  

all:
	wheel

clean:
	rm -r build *.egg-info dist