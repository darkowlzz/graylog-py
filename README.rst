Graylog-py
----------

Interact with Graylog APIs via python.

Develop
-------

Start development by cloning the repo and creating a new virtual env.
Running `python setup.py develop` would install all the dependencies and 
graylog-py in development mode. Changes to source are instantly reflected
in the installed package.

Install pre-commit git hook:

``flake8 --install-hook``

Lint
----

``python setup.py flake8``


Tests
-----

``python setup.py test``
