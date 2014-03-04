pyql-weather
=================
### Yahoo Weather para Python


Instalación:
------------------------------------------------------------

+ Descarga el paquete y ejecutar:

```bash
python setup.py install
```

+ A disfrutar de las consultas del clima en Yahoo!!!!


### Ejemplo de uso: (1)

```python
from pyql.weather.models import Weather

# Pasamos el WOEID:
w = Weather(24553062)
# Leemos el resultado:
print "Temperatura: %sc. Estatus: (%s) %s"%(w.get_temperature(), w.get_status_code(), w.get_status_text())

```

### Ejemplo de uso: (2)

```python
from pyql.weather.models import Weather, GeoData

# Conseguimos una lat y long
latitude = "20.982994"
longitude = "-89.617710"


# Obtenemos datos de una latitud y longitud dada:
geo = GeoData(latitude, longitude) # Inicializamos el objeto
# Pasamos en WOEID:
w = Weather(geo.get_woeid())
# Leemos el resultado:
print "Temperatura: %sc. Estatus: %s"%(w.get_temperature(), w.get_status_text())

```

Yahoo utiliza como valor importante el WOEID ( Where On Earth Identifiers).
Si no contamos con esta información, pero sí tenemos nuestra latitud y longitud, entonces la pasamos
para obtener el WOEID que desconocemos y posteriormente ya podremos consultar el clima.



La información que puedes obtener de esta librería es:
----------------------------------------------------------------------------------------------------

### Clase Weather
+ WOEID requerido para construir el objeto.

>> class Weather
Objeto que almacena los datos del clima y tiempo de un WOEID dado. Esta información es obtenida de los
servicios de Yahoo.

Methods defined here:

+ __init__(self, woeid)
       Constructor del objeto Weather, se alimenta inicialmente de un WOEID para obtener información del clima.
       Posteriomente se puede consultar más información del clima utilizando las funciones que contiene.

+ get_city(self)
       Obtiene el nombre de la ciudad que corresponde al WOEID consultado

+ get_country(self)
      Obtiene el nombre del País que corresponde al WOEID consultado

+ get_humidity(self)
       Obtiene la humedad del clima

+ get_language(self)
     Obtiene el lenguaje utilizado para la presentación de los resultados

+ get_lastBuildDate(self)
       Obtiene la fecha de la consulta

+ get_link(self)
      Obtiene el link de información del clima en Yahoo

+ get_pressure(self)
      Obtiene la presión del clima.

+ get_region(self)
      Obtiene el nombre de la Región que corresponde al WOEID consultado

+ get_status_code(self)
      Obtiene el código del estatus del clima

+ get_status_text(self)
     Obtiene la descripción del clima actual

+ get_sunrise(self)
       Obtiene la hora de salida del sol.

+ get_sunset(self)
     Obtiene la hora que se oculta el sol.

+ get_temperature(self)
     Obtiene la temperatura del clima

+ get_title(self)
      Obtiene el título de la consulta.

+ get_unit_distance(self)
      Devuelve la unidad utilizada para representar la distancia

+ get_unit_pressure(self)
      Devuelve la unidad de medida para representar la presión

+ get_unit_speed(self)
      Devuelve la unidad de medida para representar la velocidad del viento

+ get_unit_temp(self)
     Devuelve la unidad utilizada para representar la temperatura

--------------------------------------------------------------------------------------

### Clase GeoData
+ Latitud y Longitud requerido para construir el objeto

>>class GeoData
  Objeto que almacena los datos geoespaciales de una latitude y longitude dada. Éstos datos son obtenidos
  mediante la consulta de los servicios de Yahoo vía YQL

Methods defined here:

+  __init__(self, latitude, longitude)
      Constructor del modelo GeoData. Se alimenta inicialmente por una latitude y longitude, posteriormente se
      realiza una consulta para poder utilizar las funciones posteriores. Si existe algún error en la consulta, los datos
      que devuelvan las funciones serán incorrectas.

+ get_city(self)
     Devuelve la ciudad que le pertenece las coordenadas consultadas

+ get_country(self)
      Devuelve el País que le pertenece las coordenadas consultadas

+ get_quality(self)
    Devuelve la calidad de la consulta

+ get_state(self)
     Devuelve el Estado que le pertenece las coordenadas consultadas

+ get_woeid(self)
     Devuelve el Where on Earth Identifier

--------------------------------------------------------------------------------------

Autor:
-------------------------------------------------------------
Alex Dzul.
Python / Django Sr. Developer.

Página web: [alexdzul.com] (http://alexdzul.com)
Canal de Youtube: [youtube.com/alexexc2] (http://youtube.com/alexexc2)
Twitter: [@lexjs88] (http://twitter.com/alexjs88)


### Nota:

La versión de este paquete aún se encuentra en alfa por lo que
se recomienda no utilizar en entornos de producción hasta la liberación
de una versión estable.