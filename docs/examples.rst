***********************
Ejemplos y casos de uso
***********************

"pyql-weather" es una gran herramienta que nos permite interactuar fácilmente con los servicios del clima de Yahoo.
Aquí presentaremos algunos escenarios en el que se puede utilizar la herramienta.


Continentes
###########


Enlistar todos los Continentes
******************************

1. Lo primero que necesitamos será importar el objeto `Continent` de la siguiente manera::

    from pyql.geo.continents import Continent

2. Instanciamos un objeto del tipo Continent utilizando la función filter la cual nos devolverá una lista de elementos::

    continents = Continent.filter()

3. Recorremos la lista de objetos y podremos acceder a las propiedades de cada continente de la siguiente manera::

    for cont in continents:
        print cont.name

Obtener un Continente en específico
***********************************

1. Importamos de nuevo el objeto `Continent`::

    from pyql.geo.continents import Continent

2. Iniciamos un nuevo objeto pero en esta ocasión utilizaremos la función `get` la cual nos devuelve solamente un objeto y no una lista::

    print(continent.name)
    print(continent.lang)
    print(continent.woeid)


Lista de propiedades de Continent
*********************************

Del objeto tipo Continent podemos obtener la siguiente información:

* lang
* uri
* woeid
* placeTypeName
    * code
    * content
* name