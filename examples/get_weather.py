# -*- coding: utf-8 -*-
__author__ = 'alex'
"""
Getting the Conditions for the WOEID 24553060
"""

from pyql.weather.forecast import Forecast

woeid = 24553056

print("Conecting to Yahoo....\n")

forecast = Forecast.get(woeid=woeid, u="c")

print(forecast.item.title)
print ("=======================================\n")
print("Weather:")
print ("--------------------------------------")
print("{0}º{1} {2} Code ({3})\n".format(forecast.item.condition.temp,
                                                   forecast.units.temperature,
                                                   forecast.item.condition.text,
                                                   forecast.item.condition.code))
print("Astronomy:")
print ("--------------------------------------")
print "Sunrise: {0}\nSunset: {1}\n".format(forecast.astronomy.sunrise,
                                            forecast.astronomy.sunset)

print ("Forecast:")
print ("--------------------------------------")
for single_forecast in forecast.item.forecast:
    print("{0} {1} {2} High:{3} Low:{4}".format(single_forecast["day"],
                                                single_forecast["date"],
                                                single_forecast["text"],
                                                single_forecast["high"],
                                                single_forecast["low"]))