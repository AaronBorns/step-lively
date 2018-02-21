from setuptools import setup, find_packages
from codes import open
from os import path

path_to_here = path.abspath(path.dirname(__file__))

with open(path.join(path_to_here, 'README.rst'), encoding='utf-8') as readme_file:
  readme = readme_file.read()

setup(
  name = 'steplively',
  packages = find_packages(exclude=('tests', 'docs')),
  version = '0.2.1',
  license=license,
  description = 'An application for sensor measurement',
  long_description=readme,
  author = 'The Step Lively team',
  url = 'https://github.com/AaronBorns/steplively',
  keywords = ['sensor', 'measurement', 'data aquisition','daq'],    
  classifiers=['License :: OSI Approved :: GPLv3 License']
  packages=find_packages(exclude=['contrib', 'docs', 'tests']),
  install_requires['matplotlib','numpy']
  extras_require={
      'dev': [''],
      'test': [''],
  },
  package_data={
      'steplively': ['package_data.dat'],
  },
  entry_points={
      'console_scripts': [
          'steplively=steplively:main'
      ],
  },
)
