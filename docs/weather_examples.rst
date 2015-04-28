****************************************
**pyql.weather** Ejemplos y casos de uso
****************************************

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

El resultado en la terminal arrojará la siguiente información::

    Guadalajara
    JA
    Mexico

Astronomía
**********

Podemos consultar los datos de la salida y puesta del sol de una manera muy sencilla::

    print("Salida del sol: {0}".format(forecast.astronomy.sunrise))
    print("Puesta del sol: {0}".format(forecast.astronomy.sunset))

El resultado será algo similar a::

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

El resultado de este ejemplo en la terminal será algo similar al siguiente::

    ************** Atmósfera **********************
    Humedad: 49
    Presión: 1015.92
    Incremento: 0
    Visibilidad: 49
    ***********************************************



