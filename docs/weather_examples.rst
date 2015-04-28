*********************
Ejemplos pyql.weather
*********************

"pyql-weather" es una gran herramienta que nos permite interactuar fácilmente con los servicios del clima de Yahoo.
Aquí presentaremos algunos escenarios en el que se puede utilizar los objetos almacenados en pyql.weather


Forecast
########

Para poder completar estos ejemplos es necesario importar el objeto tipo `Forecast`::

    from pyql.weather.forecast import Forecast

Posteriormente debemos instanciar un objeto del tipo `Forecast` utilizando la función `get` pasándole el parámetro `woeid` y `u`::

    my_woeid = 24553135
    forecast = Forecast.get(woeid=my_woeid, u="c")

- Nota: El parámetro woeid es el "Where on Earth Identifiers" del lugar que deseamos obtener y el segundo parámetro "u" nos permite definir si la unidad de medida del clima deseada es en grados **Celsius** (" c ") o **Fahrenheit** (" f ").

Ya que tenemos este objeto en memoria ahora podemos utilizarlo para conocer todos los detalles del pronóstico del clima:


Location
********

Para obtener más detalle del lugar que estamos consultando el pronóstico del clima podemos utilizar lo siguiente::

    print(forecast.location.city)
    print(forecast.location.region)
    print(forecast.location.country)

**Resultado**::

    Guadalajara
    JA
    Mexico

Astronomía
**********

Podemos consultar los datos de la salida y puesta del sol de una manera muy sencilla::

    print("Salida del sol: {0}".format(forecast.astronomy.sunrise))
    print("Puesta del sol: {0}".format(forecast.astronomy.sunset))

**Resultado**::

    Salida del sol: 7:24 am
    Puesta del sol: 8:14 pm


Atmósfera
*********

Los datos atmosféricos pueden ser encontrados en la propiedad **atmosphere** y la información disponible es la siguiente::

    print("************** Atmósfera **********************")
    print("Humedad: {0}".format(forecast.atmosphere.humidity))
    print("Presión: {0}".format(forecast.atmosphere.pressure))
    print("Incremento: {0}".format(forecast.atmosphere.rising))
    print("Visibilidad: {0}".format(forecast.atmosphere.humidity))
    print("***********************************************")

**Resultado**::

    ************** Atmósfera **********************
    Humedad: 49
    Presión: 1015.92
    Incremento: 0
    Visibilidad: 49
    ***********************************************

Viento
******

Para obtener la información referente al viento podemos realizar lo siguiente::

    print("Enfriamiento: {0}".format(forecast.wind.chill))
    print("Dirección: {0}".format(forecast.wind.direction))
    print("Velocidad: {0}".format(forecast.wind.speed))

**Resultado**::

    Enfriamiento: 24
    Dirección: 190
    Velocidad: 8.05

Unidades de Medición
********************

Hemos visto en los ejemplos anteriores que la mayoría de los números se encuentran crudos y no sabemos con certeza en qué medidas están expresados. Para poder conocer esta información se debe realizar lo siguiente::

    print("Unidad de velocidad: {0}".format(forecast.units.speed))
    print("Unidad de presión: {0}".format(forecast.units.pressure))
    print("Unidad de distancia: {0}".format(forecast.units.distance))
    print("Unidad de temperatura: {0}".format(forecast.units.temperature))

**Resultado**::

    Unidad de velocidad: km/h
    Unidad de presión: mb
    Unidad de distancia: km
    Unidad de temperatura: C

Condición actual del clima
**************************

``pyql-weather`` nos permite obtener las condiciones del clima de una manera sencilla::

    print(forecast.item.condition.code)
    print(forecast.item.condition.date)
    print(forecast.item.condition.temp)
    print(forecast.item.condition.text)

**Resultado**::

    28
    Tue, 28 Apr 2015 12:53 pm CDT
    26
    Mostly Cloudy

- Esta información que hemos obtenido no nos permite entender con claridad las condiciones climatológicas actuales.

En el siguiente ejemplo uniremos varias partes de la librería para presentar la información de una manera más formal::

    ciudad = forecast.location.city
    region = forecast.location.region
    pais = forecast.location.country
    print("Condiciones del clima en {0}, {1}, {2}.\n".format(ciudad, region, pais))
    print("Fecha: {0}".format(forecast.item.condition.date))
    print("Temperatura: {0}º {1}".format(forecast.item.condition.temp, forecast.units.temperature))
    print("Condición: {0} ({1})".format(forecast.item.condition.text, forecast.item.condition.code))

**Resultado**::

    Condiciones del clima en Guadalajara, JA, Mexico.

    Fecha: Tue, 28 Apr 2015 12:53 pm CDT
    Temperatura: 26º C
    Condición: Mostly Cloudy (28)

Pronóstico 5 días.
******************

Yahoo Weather nos permite conocer el pronóstico del clima de 5 fechas continuas (incluyendo la fecha de consulta).

- Por ejemplo: Si consultamos el clima el día de hoy **28-04-2015 (día 1)**, Yahoo nos ofrecerá el pronóstico para los días **29-04-2015 (día 2)**, **30-04-2015 (día 3)**, **01-05-2015 (día 4)** y **02-05-2015 (día 5)**.

A continuación veremos un ejemplo básico para extraer el pronóstico para la ciudad de Mérida, Yuc, México::

    woeid = 133327
    forecast = Forecast.get(woeid=woeid, u="c")

    for day in forecast.item.forecast:
        print day

**Resultado**::

    {u'code': u'30', u'text': u'Partly Cloudy', u'high': u'41', u'low': u'26', u'date': u'28 Apr 2015', u'day': u'Tue'}
    {u'code': u'38', u'text': u'AM Thunderstorms', u'high': u'31', u'low': u'23', u'date': u'29 Apr 2015', u'day': u'Wed'}
    {u'code': u'39', u'text': u'AM Showers', u'high': u'28', u'low': u'21', u'date': u'30 Apr 2015', u'day': u'Thu'}
    {u'code': u'30', u'text': u'Partly Cloudy', u'high': u'32', u'low': u'19', u'date': u'1 May 2015', u'day': u'Fri'}
    {u'code': u'34', u'text': u'Mostly Sunny', u'high': u'33', u'low': u'19', u'date': u'2 May 2015', u'day': u'Sat'}


Podemos observar que el resultado que ``pyql-weather`` retorna es un arreglo de objetos en formato json los cuales podemos manipular para formatear la información de la siguiente manera::

    woeid = 133327
    forecast = Forecast.get(woeid=woeid, u="c")
    ciudad = forecast.location.city
    region = forecast.location.region
    pais = forecast.location.country
    print("Condiciones del clima para la ciudad de {0}, {1}, {2}: \n".format(ciudad, region, pais))
    for day in forecast.item.forecast:
        print("Fecha: {0} {1}".format(day['day'], day['date']))
        print("Pronóstico: {0} ({1})".format(day['text'], day['code']))
        print("Temperatura Mínima: {0}º {1}".format(day['low'], forecast.units.temperature))
        print("Temperatura Máxima: {0}º {1}".format(day['high'], forecast.units.temperature))
        print("*****************************************************************************")

**Resultado**::

    Condiciones del clima para la ciudad de Merida, YU, Mexico:

    Fecha: Tue 28 Apr 2015
    Pronóstico: Partly Cloudy (30)
    Temperatura Mínima: 26º C
    Temperatura Máxima: 41º C
    *****************************************************************************
    Fecha: Wed 29 Apr 2015
    Pronóstico: AM Thunderstorms (38)
    Temperatura Mínima: 23º C
    Temperatura Máxima: 31º C
    *****************************************************************************
    Fecha: Thu 30 Apr 2015
    Pronóstico: AM Showers (39)
    Temperatura Mínima: 21º C
    Temperatura Máxima: 28º C
    *****************************************************************************
    Fecha: Fri 1 May 2015
    Pronóstico: Partly Cloudy (30)
    Temperatura Mínima: 19º C
    Temperatura Máxima: 32º C
    *****************************************************************************
    Fecha: Sat 2 May 2015
    Pronóstico: Mostly Sunny (34)
    Temperatura Mínima: 19º C
    Temperatura Máxima: 33º C
    *****************************************************************************