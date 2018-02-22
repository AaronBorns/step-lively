from setuptools import setup, find_packages
from codecs import open
from os import path

path_to_here = path.abspath(path.dirname(__file__))

with open(path.join(path_to_here, 'README.rst'), encoding='utf-8') as readme_file:
  readme = readme_file.read()

with open(path.join(path_to_here, 'COPYING'), encoding='utf-8') as license_file:
  license = license_file.read()


setup(
  name = 'steplively',
  version = '0.2.1',
  license=license,
  description = 'An application for sensor measurement',
  long_description = readme,
  author = ['Mohamed Abdelhady', 'Mike', 'Xavier Williams', 'Joe Ayoub', 'Aaron Borns'],
  url = 'https://github.com/AaronBorns/steplively',
  keywords = ['sensor', 'measurement', 'data aquisition','daq'],    
  classifiers = ['License :: OSI Approved :: GPLv3 License'],
  packages = find_packages(exclude=['contrib', 'docs', 'tests']),
  include_package_data = True,
  install_requires = ['matplotlib','numpy'],
  extras_require = {
      'dev': [''],
      'test': [''],
  },
  entry_points = {
      'console_scripts': [
          'steplively=steplively:main'
      ],
  },
)
