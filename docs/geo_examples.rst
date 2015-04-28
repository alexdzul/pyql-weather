************************************
**pyql.geo** Ejemplos y casos de uso
************************************

"pyql-weather" es una gran herramienta que nos permite interactuar fácilmente con los servicios del clima de Yahoo.
Aquí presentaremos algunos escenarios en el que se puede utilizar los objetos almacenados en pyql.geo


Continents
##########

Para poder completar estos ejemplos es necesario importar el objeto tipo `Continent`::

    from pyql.geo.continents import Continent

Enlistar todos los Continentes
******************************

1. Instanciamos un objeto del tipo Continent utilizando la función filter la cual nos devolverá una lista de elementos::

    continents = Continent.filter()

3. Recorremos la lista de objetos y podremos acceder a las propiedades de cada continente de la siguiente manera::

    for cont in continents:
        print cont.name

Obtener un Continente en específico
***********************************

Iniciamos un nuevo objeto pero en esta ocasión utilizaremos la función `get` la cual nos devuelve solamente un objeto y no una lista::

    continent = Continent.get(name="Africa")

    print(continent.name)
    print(continent.lang)
    print(continent.woeid)


PlaceFinder
###########

Para poder completar estos ejemplos es necesario importar el objeto tipo `PlaceFinder`::

    from pyql.geo.placefinder import PlaceFinder

Obtener información de un lugar vía Latitude / Longitude
********************************************************

Realizamos la búsqueda de la siguientea manera::

    latitude = "20.632784"
    longitude = "-103.359375"
    lat_long = "{0},{1}".format(latitude, longitude)

    finder = PlaceFinder.get(text=lat_long, gflags="R")
    place_info = "{0}, {1} ZIP: {2} | WOEID:{3}".format(finder.city,
                                                        finder.country,
                                                        finder.uzip,
                                                        finder.woeid)
    print(place_info)

Obtener lugar pasando parte de su nombre
****************************************

Podemos de igual manera pasar una parte del nombre del lugar y obtener el mismo resultado::


    find = PlaceFinder.get(text="sfo")
    print(find.quality)
    print(find.name)
    print(find.line1)
    print(find.line2)
