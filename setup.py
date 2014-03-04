#!/usr/bin/env python
from distutils.core import setup

version = "0.1"
author = "Alex Dzul"
author_email = "alexexc2@gmail.com"
mainteiner = "Alex Dzul"
mainteiner_email = "alexexc2@gmail.com"
licence = "MIT License"

setup(name='pyql-weather',
      version=version,
      description='Yahoo Weather in Python',
      license="MIT License",
      author=author,
      author_email=author_email,
      url='http://www.github.com/alexdzul/pyql-weather/',
      packages=['pyql','pyql.weather'],
     )