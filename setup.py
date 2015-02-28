#!/usr/bin/env python
from distutils.core import setup

version = "0.2.1"
author = "Alex Dzul"
author_email = "alexexc2@gmail.com"
mainteiner = "Alex Dzul"
mainteiner_email = "alexexc2@gmail.com"
licence = "MIT License"

setup(name='pyql-weather',
      version=version,
      description='Yahoo Weather in Python v.%s' % version,
      long_description=open('README.md').read(),
      license="MIT License",
      author=author,
      author_email=author_email,
      url='http://www.github.com/alexdzul/pyql-weather/',
      packages=['pyql', 'pyql.weather', 'pyql.geo'],
      data_files=[('', ['README.md', 'LICENSE'])],
      keywords=['pyql', 'yahoo', 'weather'],
      classifiers=["Development Status :: 4 - Beta",
                   "Environment :: Console",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 2.7",
                   "Topic :: Software Development",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   ]
      )