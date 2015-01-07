# -*- coding: utf-8 -*-
from pyql.geo.placefinder import PlaceFinder
from pyql.weather.forecast import Forecast

latitude = "20.982994"
longitude = "-89.617710"
woeid = '24553056'


def main():
    print ("=================================")
    print ("obteniendo datos geoespaciales (%s, %s) ...." % (latitude, longitude))
    print ("=================================")
    lat_long = latitude+","+longitude
    find_place = PlaceFinder.get(lat_long)
    print ("{0}: {1}".format(find_place.woeid, find_place.city))
    print ("=================================")
    print ("obteniendo Información del clima de woeid: {0}".format(find_place.woeid))
    print ("=================================")
    forecast = Forecast.get(woeid)
    print forecast.astronomy.sunrise
    print forecast.astronomy.sunset
    for day in forecast.item.forecast:
        print (day["text"])


main()