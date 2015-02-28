***********************
Ejemplos y casos de uso
***********************

"pyql-weather" es una gran herramienta que nos permite interactuar fácilmente con los servicios del clima de Yahoo.
Aquí presentaremos algunos escenarios en el que se puede utilizar la herramienta.


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


Oceans
######

Para poder completar estos ejemplos es necesario importar el objeto tipo `Ocean`::

    from pyql.geo.oceans import Ocean


Obtener el listado completo de océanos
**************************************

Obtener todos los océanos e imprimir sus números `woeid`::

    oceans = Ocean.filter()
    for ocean in oceans:
        info = "{0}, woeid: {1}".format(ocean.name, ocean.woeid)
        print(info)

El resultado sería el siguiente::

    Atlantic Ocean, woeid: 55959709
    Southern Ocean, woeid: 55959676
    Indian Ocean, woeid: 55959675
    Pacific Ocean, woeid: 55959717
    Arctic Ocean, woeid: 55959707


Obtener la información de un océano en específico:
**************************************************

Para obtener solamente un objeto del tipo `Ocean` se requiere utilizar la función `get` seguida de los criterios
de búsqueda::

    ocean = Ocean.get(name="Atlantic Ocean")

    print(ocean.name)
    print(ocean.woeid)
    print(ocean.lang)

