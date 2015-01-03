# -*- coding: utf-8 -*-
__author__ = 'alexdzul'
from pyql.interface import YQLConector


class Forecast:
    """
    Objeto que almacena los datos del clima y tiempo de un WOEID dado. Esta información es obtenida de los
    servicios de Yahoo.
    """

    def __init__(self):
        self.__Result = None
        self.__count = None
        self.__as_json = None
        self.__as_xml = None
        self.__item = _Item()

    @staticmethod
    def get(value, units="c"):
        """
        Constructor del objeto Weather, se alimenta inicialmente de un WOEID para obtener información del clima.
        Posteriomente se puede consultar más información del clima utilizando las funciones que contiene.
        """
        response = query_forecast(value, units)
        if response:
            my_count = response["query"]["count"]
            channel = response["query"]["results"]["channel"]
            forecast = Forecast()
            forecast._Result = channel
            forecast.__item._Result = channel["item"]
            return forecast

    @property
    def title(self):
        try:
            return self.__Result["title"]
        except KeyError:
            return None


    @property
    def link(self):
        try:
            return self.__Result["link"]
        except KeyError:
            return None

    @property
    def description(self):
        try:
            return self.__Result["description"]
        except KeyError:
            return None

    @property
    def language(self):
        try:
            return self.__Result["languaje"]
        except KeyError:
            return None

    @property
    def lastBuildDate(self):
        try:
            return self.__Result["lastBuildDate"]
        except KeyError:
            return None

    @property
    def ttl(self):
        try:
            return self.__Result["ttl"]
        except KeyError:
            return None

    @property
    def location(self):
        try:
            return self.__Result["location"]
        except KeyError:
            return None

    @property
    def units(self):
        try:
            return self.__Result["units"]
        except KeyError:
            return None


    @property
    def wind(self):
        try:
            return self.__Result["wind"]
        except KeyError:
            return None

    @property
    def atmosphere(self):
        try:
            return self.__Result["atmosphere"]
        except KeyError:
            return None

    @property
    def astronomy(self):
        try:
            return self.__Result["astronomy"]
        except KeyError:
            return None

    @property
    def image(self):
        try:
            return self.__Result["image"]
        except KeyError:
            return None

    @property
    def item(self):
        return self.__item

    @property
    def item_title(self):
        try:
            return self.__Result["item"]["title"]
        except KeyError:
            return None

    @property
    def item_lat(self):
        try:
            return self.__Result["item"]["lat"]
        except KeyError:
            return None

    @property
    def item_long(self):
        try:
            return self.__Result["item"]["long"]
        except KeyError:
            return None

    @property
    def item_lat(self):
        try:
            return self.__Result["item"]["lat"]
        except KeyError:
            return None


class _Item():

    def __init__(self):
        self._Result = None

    @property
    def title(self):
        try:
            return self._Result["title"]
        except KeyError:
            return None

    @property
    def lat(self):
        try:
            return self._Result["lat"]
        except KeyError:
            return None

    @property
    def long(self):
        try:
            return self._Result["long"]
        except KeyError:
            return None

    @property
    def link(self):
        try:
            return self._Result["link"]
        except KeyError:
            return None

    @property
    def pubdate(self):
        try:
            return self._Result["pubdate"]
        except KeyError:
            return None

    @property
    def description(self):
        try:
            return self._Result["description"]
        except KeyError:
            return None

    @property
    def condition(self):
        try:
            return self._Result["condition"]
        except KeyError:
            return None

    @property
    def forecast(self):
        try:
            return self._Result["forecast"]
        except KeyError:
            return None


def query_forecast(value, units="c"):
    """
    Construye la query YQL y realiza la solicitud de datos a la tabla weather.forecast
    """
    query = 'select * from weather.forecast where woeid={0} AND u="{1}"'.format(value, units)
    yql_conector = YQLConector()
    data = yql_conector.request(query)
    return data