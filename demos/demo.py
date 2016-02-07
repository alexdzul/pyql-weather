# coding=utf-8
from pyql.geo.continents import Continent
from pyql.geo.states import State
from pyql.weather.forecast import Forecast


# Ejemplo 1. Imprimimos el listado de continentes
print("========= Listado de continentes ===========")
continents = Continent.filter()

for cont in continents:
    print(cont.name)


# Ejemplo 2. Obtenemos el listado de los estados de México.
print("========= Listado de estados de México")
states = State.filter(place="México")
for state in states:
    print(state.name)


# Ejemplo 3. Consultamos el clima de un woeid en específico.
print("======== Clima del WOEID: 24553135.")
my_woeid = 24553135
forecast = Forecast.get(woeid=my_woeid, u="c")
print(forecast.location.city, forecast.location.region, forecast.location.country)
print(forecast.item.condition.temp, forecast.units.temperature, forecast.item.condition.text)
