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
      long_description=open('README.txt').read(),
      license="MIT License",
      author=author,
      author_email=author_email,
      url='http://www.github.com/alexdzul/pyql-weather/',
      packages=['pyql','pyql.weather'],
      classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Topic :: Software Development",
            "Topic :: Software Development :: Libraries :: Python Modules"
            ]
     )