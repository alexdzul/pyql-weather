# -*- coding: utf-8 -*-
__author__ = 'alex'
from pyql.geo.placefinder import PlaceFinder

latitude = "20.982994"
longitude = "-89.617710"
finder = PlaceFinder.filter(text="sfo")
for find in finder:
    print find.quality
    print find.name
    print find.line1
    print find.line2
