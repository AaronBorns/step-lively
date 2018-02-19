from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('COPYING') as f:
    license = f.read()

setup(
  name = 'steplively',
  packages = find_packages(exclude=('tests', 'docs')),
  version = '0.2.0',
  license=license,
  description = 'An application for sensor measurement',
  long_description=readme,
  author = 'Aaron Borns',
  author_email = 'aborns@outlook.com',
  url = 'https://github.com/AaronBorns/steplively',
  keywords = ['sensor', 'measurement', 'data aquisition','daq'],
)