from pyql.geo.continents import Continent

continents = Continent.filter()

for cont in continents:
    print(cont.name)
