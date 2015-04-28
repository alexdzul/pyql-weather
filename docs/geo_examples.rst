*****************
Ejemplos pyql.geo
*****************

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

Iniciamos un nuevo objeto pero en esta ocasión utilizaremos la función `get` la cual nos devuelve solamente un objeto
y no una lista::

    continent = Continent.get(name="Africa")

    print(continent.name)
    print(continent.lang)
    print(continent.woeid)

**Resultado**::

    Africa
    en-US
    24865670

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

**Resultado**::

    Guadalajara, Mexico ZIP: 44940 | WOEID:24553135


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

**Resultado**::

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

States
######

1. Para poder consultar los estados de una región, es requisito construir el objeto pasando como argumento la
llave "place" la cual es el nombre del País que deseamos conocer.

2. Para poder completar estos ejemplos es necesario importar el objeto tipo `State`::

    from pyql.geo.states import State


Obtener todos los estados de México
***********************************

Generamos la consulta con el place "Mexico" e imprimimos el resultado en un ciclo for::

    states = State.filter(place="Mexico")
    for state in states:
        print(state.name)

**Resultado**::


    Zacatecas
    Aguascalientes
    San Luis Potosi
    Nuevo Leon
    Durango
    Guanajuato
    Nayarit
    Jalisco
    Tamaulipas
    Queretaro de Arteaga
    Coahuila de Zaragoza
    Hidalgo
    Michoacan de Ocampo
    Mexico
    Colima
    Distrito Federal
    Sinaloa
    Tlaxcala
    Morelos
    Puebla
    Veracruz-Llave
    Chihuahua
    Guerrero
    Oaxaca
    Baja California Sur
    Tabasco
    Sonora
    Chiapas
    Campeche
    Yucatan
    Baja California
    Quintana Roo

Obtener información del estado de Yucatán, México
*************************************************

Para este ejemplo utilizamos la función `get` en lugar de `filter` para que el resultado sea solamente un objeto
y no necesiten recorrerlo en un ciclo::

    state = State.get(place="Mexico", name="Yucatan")
    print(state.name, state.woeid)


Sea
###

Para poder completar estos ejemplos es necesario importar el objeto tipo `Sea`::

    from pyql.geo.seas import Sea

Listado completo de mares
*************************

La forma más sencilla de obtener el listado completo de todos los mares del mundo es utilizando la función **filter** sin pasar ningún parámetro como filtro::

    sea_list = Sea.filter()
    for sea in sea_list:
        print("Nombre: {0} | woeid: {1}".format(sea.name, sea.woeid))

**Resultado**::

    Nombre: Mediterranean Sea | woeid: 55959718
    Nombre: Gulf of Aqaba | woeid: 55959677
    Nombre: Red Sea | woeid: 55959678
    Nombre: English Channel | woeid: 55959688
    Nombre: Irish Sea | woeid: 28742112
    Nombre: Black Sea | woeid: 55959689
    Nombre: North Sea | woeid: 55959673
    Nombre: Arabian Sea | woeid: 55959681
    Nombre: Persian Gulf | woeid: 55959679
    Nombre: Baltic Sea | woeid: 55961436
    Nombre: Gulf of Oman | woeid: 55959680
    Nombre: Norwegian Sea | woeid: 55959691
    Nombre: Denmark Strait | woeid: 55959692
    Nombre: Greenland Sea | woeid: 55959685
    Nombre: Caribbean Sea | woeid: 55959687
    Nombre: Labrador Sea | woeid: 55959684
    Nombre: Barents Sea | woeid: 55961429
    Nombre: Bay of Bengal | woeid: 55959674
    Nombre: Davis Strait | woeid: 55959683
    Nombre: Gulf of Mexico | woeid: 55959686
    Nombre: Andaman Sea | woeid: 55959713
    Nombre: Hudson Bay | woeid: 55959682
    Nombre: Strait of Malacca | woeid: 55959714
    Nombre: Nares Strait | woeid: 55959690
    Nombre: Kara Sea | woeid: 55961432
    Nombre: Gulf of Thailand | woeid: 55959699
    Nombre: Java Sea | woeid: 55959715
    Nombre: Gulf of Tonkin | woeid: 55959700
    Nombre: South China Sea | woeid: 55959698
    Nombre: Bali Sea | woeid: 55960587
    Nombre: Flores Sea | woeid: 55960586
    Nombre: Savu Sea | woeid: 55960588
    Nombre: Laptev Sea | woeid: 55961431
    Nombre: Taiwan Strait | woeid: 55959701
    Nombre: Bohai Sea | woeid: 55959695
    Nombre: Timor Sea | woeid: 55959706
    Nombre: Yellow Sea | woeid: 55959696
    Nombre: East China Sea | woeid: 55959694
    Nombre: Korea Strait | woeid: 55959697
    Nombre: Arafura Sea | woeid: 55959716
    Nombre: Great Australian Bight | woeid: 55959703
    Nombre: Beaufort Sea | woeid: 55959708
    Nombre: Gulf of Carpentaria | woeid: 55959705
    Nombre: East Sea/Sea of Japan | woeid: 55959693
    Nombre: Gulf of Alaska | woeid: 55959710
    Nombre: Coral Sea | woeid: 55959704
    Nombre: Sea of Okhotsk | woeid: 55961433
    Nombre: East Siberian Sea | woeid: 55961430
    Nombre: Chukchi Sea | woeid: 55961435
    Nombre: Tasman Sea | woeid: 55959702
    Nombre: Bering Sea | woeid: 55961434


Búsqueda con filtros.
*********************

Ahora veremos un ejemplo similar al anterior pero aplicando un filtro. Realizaremos la búsqueda de los mares del continente de África::

    african_seas = Sea.filter(place="Africa")

    for sea in african_seas:
        print(sea.name)

**Resultado**::

    Red Sea
    Gulf of Aqaba
    Mediterranean Sea
    Arabian Sea

District
########

Devuelve información sobre los lugares que son áreas administrativas de tercer nivel dentro de un país. Tenga en cuenta que el término "**distrito**" se refiere a cualquier área administrativa que subdivide una zona administrativa de segundo nivel, como los distritos, comunas, municipios.

Para poder completar estos ejemplos es necesario importar el objeto tipo `District`::

    from pyql.geo.districts import District

Listado de distritos
********************

Para realizar una búsqueda de los distritos de "Greater London" escribimos lo siguiente::

    districts = District.filter(place="Greater London")

    for element in districts:
        print(element.name)

**Resultado**::

    City of Westminster
    City of London
    Royal Borough of Kensington and Chelsea
    London Borough of Camden
    London Borough of Islington
    London Borough of Lambeth
    London Borough of Southwark
    London Borough of Hammersmith and Fulham
    London Borough of Hackney
    London Borough of Tower Hamlets
    London Borough of Wandsworth
    London Borough of Haringey
    London Borough of Lewisham
    London Borough of Brent
    London Borough of Merton
    London Borough of Newham
    London Borough of Waltham Forest
    London Borough of Greenwich
    London Borough of Barnet
    London Borough of Ealing
    London Borough of Richmond upon Thames
    London Borough of Enfield
    London Borough of Hounslow
    London Borough of Redbridge
    London Borough of Sutton
    London Borough of Croydon
    London Borough of Harrow
    Royal Borough of Kingston upon Thames
    London Borough of Barking and Dagenham
    London Borough of Bromley
    London Borough of Bexley
    London Borough of Hillingdon
    London Borough of Havering

