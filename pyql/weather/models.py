# -*- coding: UTF-8 -*-
"""
Archivo: models.py
En este archivo se encuentran los modelos (Objetos) que almacenan la información obtenida de las consultas a Yahoo vía YQL.
"""
__author__ = 'Alex Dzul'
from interface import get_geo_data, get_weather_data

class GeoData:
    """
    Objeto que almacena los datos geoespaciales de una latitude y longitude dada. Éstos datos son obtenidos
    mediante la consulta de los servicios de Yahoo vía YQL
    """

    def __init__(self, latitude, longitude):
        """
        Constructor del modelo GeoData. Se alimenta inicialmente por una latitude y longitude, posteriormente se
        realiza una consulta para poder utilizar las funciones posteriores. Si existe algún error en la consulta, los datos
        que devuelvan las funciones serán incorrectas.
        """
        self.latitude = latitude
        self.longitude = longitude
        self.obj = get_geo_data(self.latitude, self.longitude)

    def get_woeid(self):
        """
        Devuelve el Where on Earth Identifier
        """
        return self.obj["query"]["results"]["Result"]["woeid"]

    def get_country(self):
        """
        Devuelve el País que le pertenece las coordenadas consultadas
        """
        return self.obj["query"]["results"]["Result"]["country"]

    def get_state(self):
        """
        Devuelve el Estado que le pertenece las coordenadas consultadas
        """
        return self.obj["query"]["results"]["Result"]["state"]

    def get_city(self):
        """
        Devuelve la ciudad que le pertenece las coordenadas consultadas
        """
        return self.obj["query"]["results"]["Result"]["city"]

    def get_quality(self):
        """
        Devuelve la calidad de la consulta
        """
        return self.obj["query"]["results"]["Result"]["quality"]


class Weather:
    """
    Objeto que almacena los datos del clima y tiempo de un WOEID dado. Esta información es obtenida de los
    servicios de Yahoo.
    """
    def __init__(self, woeid):
        """
        Constructor del objeto Weather, se alimenta inicialmente de un WOEID para obtener información del clima.
        Posteriomente se puede consultar más información del clima utilizando las funciones que contiene.
        """
        self.woeid = woeid
        self.unit_temp = "c"
        self.obj = get_weather_data(self.woeid, self.unit_temp)

    def get_title(self):
        """
        Obtiene el título de la consulta.
        """
        return self.obj["query"]["results"]["channel"]["title"]

    def get_city(self):
        """
        Obtiene el nombre de la ciudad que corresponde al WOEID consultado
        """
        return self.obj["query"]["results"]["channel"]["location"]["city"]

    def get_country(self):
        """
        Obtiene el nombre del País que corresponde al WOEID consultado
        """
        return self.obj["query"]["results"]["channel"]["location"]["country"]

    def get_region(self):
        """
        Obtiene el nombre de la Región que corresponde al WOEID consultado
        """
        return self.obj["query"]["results"]["channel"]["location"]["region"]

    def get_link(self):
        """
        Obtiene el link de información del clima en Yahoo
        """
        return self.obj["query"]["results"]["channel"]["link"]

    def get_language(self):
        """
        Obtiene el lenguaje utilizado para la presentación de los resultados
        """
        return self.obj["query"]["results"]["channel"]["lenguage"]

    def get_lastBuildDate(self):
        """
        Obtiene la fecha de la consulta
        """
        return self.obj["query"]["results"]["channel"]["lastBuildDate"]

    def get_temperature(self):
        """
        Obtiene la temperatura del clima
        """
        return self.obj["query"]["results"]["channel"]["item"]['condition']['temp']

    def get_status_code(self):
        """
        Obtiene el código del estatus del clima
        """
        return self.obj["query"]["results"]["channel"]["item"]['condition']['code']

    def get_status_text(self):
        """
        Obtiene la descripción del clima actual
        """
        return self.obj["query"]["results"]["channel"]["item"]['condition']['text']

    def get_sunrise(self):
        """
        Obtiene la hora de salida del sol.
        """
        return self.obj["query"]["results"]["channel"]["astronomy"]["sunrise"]

    def get_sunset(self):
        """
        Obtiene la hora que se oculta el sol.
        """
        return self.obj["query"]["results"]["channel"]["astronomy"]["sunset"]

    def get_humidity(self):
        """
        Obtiene la humedad del clima
        """
        return self.obj["query"]["results"]["channel"]["atmosphere"]["humidity"]

    def get_pressure(self):
        """
        Obtiene la presión del clima.
        """
        return self.obj["query"]["results"]["channel"]["atmosphere"]["pressure"]

    def get_unit_temp(self):
        """
        Devuelve la unidad utilizada para representar la temperatura
        """
        return self.obj["query"]["results"]["channel"]["units"]["temperature"]

    def get_unit_distance(self):
        """
        Devuelve la unidad utilizada para representar la distancia
        """
        return self.obj["query"]["results"]["channel"]["units"]["distance"]

    def get_unit_speed(self):
        """
        Devuelve la unidad de medida para representar la velocidad del viento
        """
        return self.obj["query"]["results"]["channel"]["units"]["speed"]

    def get_unit_pressure(self):
        """
        Devuelve la unidad de medida para representar la presión
        """
        return self.obj["query"]["results"]["channel"]["units"]["pressure"]