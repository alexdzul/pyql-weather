#!/usr/bin/env python
from distutils.core import setup
from pyql import __author__, __version__, __email__, __license__, __maintainer__

long_description = open('README.md').read()

setup(name='pyql-weather',
      version=__version__,
      description='YQL Queries and Yahoo Weather in Python v.%s' % __version__,
      long_description=long_description,
      license=__license__,
      author=__author__,
      author_email=__email__,
      maintainer=__maintainer__,
      maintainer_email=__email__,
      url='http://www.github.com/alexdzul/pyql-weather/',
      packages=['pyql', 'pyql.weather', 'pyql.geo'],
      data_files=[('', ['README.md', 'LICENSE'])],
      keywords=['pyql', 'yahoo', 'weather'],
      platforms='any',
      classifiers=["Development Status :: 4 - Beta",
                   "Environment :: Console",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.3",
                   "Programming Language :: Python :: 3.4",
                   "Topic :: Software Development",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   ]
      )