# -*- coding: utf-8 -*-
__author__ = 'alex'
from pyql.geo.continents import Continent


continent = Continent.get(name="Africa")
print continent.name
print continent.lang
print continent.woeid


continents = Continent.filter()
for cont in continents:
    print cont.name