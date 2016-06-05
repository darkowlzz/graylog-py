from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='graylog-py',
      version='0.1',
      description='Graylog APIs for python',
      long_description=readme(),
      author='darkowlzz',
      author_email='me@darkowlzz.space',
      license='MIT',
      packages=['graylog'],
      install_requires=['requests'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
