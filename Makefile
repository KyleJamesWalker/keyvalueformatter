clean:
	@rm -rf env2/ env3/ build/ *.egg-info *.egg
	@find . -name '*.pyc' -delete
	@find . -name '__pycache__' -delete

env2:
	virtualenv --python=python2 env2
	env2/bin/pip install --upgrade pip setuptools pbr
	env2/bin/pip install -e .

tests2: env2
	env2/bin/python setup.py test

env3:
	virtualenv --python=python3 env3
	env3/bin/pip install --upgrade pip setuptools pbr
	env3/bin/pip install -e .

tests3: env3
	env3/bin/python setup.py test

tests: tests2 tests3

build:
	env3/bin/python setup.py build
