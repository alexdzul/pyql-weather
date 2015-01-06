# -*- coding: utf-8 -*-
__author__ = 'Alex Dzul'
from pyql.interface import YQLConector


class PlaceFinder():
    """
    Consulta la información del elemento geo.placefinder de Yahoo YQL
    """

    def __init__(self):
        self.__Result = None
        self.__count = None
        self.__as_xml = None

    def as_json(self):
        """
        Devolvemos los resultados en formato JSON
        """
        return self.__Result

    @staticmethod
    def get(value, field="text"):
        """
        Realizamos una consulta a la base de datos de Yahoo para obtener información de geo.placefinder.
        Nota:
        Esta función devolverá solamente un objeto.
        Si se encuentran más, entonces la función devuelve el primer resultado de la lista.

        Para obtener más de 1 resultado entonces utilizar la función filter().
        """
        response = query_placefinder(value, field)
        if response:
            my_count = response["query"]["count"]
            my_response = response["query"]["results"]["Result"]
            place = PlaceFinder()
            place.__count = my_count
            if type(my_response) is dict:  # Si es solo un elemento entonces enviamos de manera directa
                place.__Result = my_response
            if type(my_response) is list:
                place.__Result = my_response[0]  # Si es una lista entonces enviamos solo el primer elemento
            return place

    @staticmethod
    def filter(value, field="text"):
        """
        Realiza una consulta a la base de datos de Yahoo utilizando YQL.
        El valor retornado siempre será una lista de objetos tipo "PlaceFinder"
        """
        response = query_placefinder(value, field)
        if response:
            my_count = response["query"]["count"]
            list_result = []
            my_response = response["query"]["results"]["Result"]
            if type(my_response) is list:
                for data in response:
                    place = PlaceFinder()
                    place.__Result = data
                    place.__count = my_count
                    list_result.append(place)
            if type(my_response) is dict:
                place = PlaceFinder()
                place.__Result = my_response
                place.__count = my_count
                list_result.append(place)
            return list_result

    def count(self):
        """
        Devuelve el número de registros encontrados por la consulta yql
        """
        try:
            return int(self.__count)
        except StandardError:
            return 0

    @property
    def quality(self):
        try:
            return self.__Result["quality"]
        except KeyError:
            return None

    @property
    def addressmatchtype(self):
        try:
            return self.__Result["addressMatchType"]
        except KeyError:
            return None

    @property
    def latitude(self):
        try:
            return self.__Result["latitude"]
        except KeyError:
            return None

    @property
    def longitude(self):
        try:
            return self.__Result["longitude"]
        except KeyError:
            return None

    @property
    def offsetlat(self):
        try:
            return self.__Result["offsetlat"]
        except KeyError:
            return None

    @property
    def offsetlon(self):
        try:
            return self.__Result["offsetlat"]
        except KeyError:
            return None

    @property
    def radius(self):
        try:
            return self.__Result["radius"]
        except KeyError:
            return None

    @property
    def name(self):
        try:
            return self.__Result["name"]
        except KeyError:
            return None

    @property
    def line1(self):
        try:
            return self.__Result["line1"]
        except KeyError:
            return None

    @property
    def line2(self):
        try:
            return self.__Result["line2"]
        except KeyError:
            return None

    @property
    def line3(self):
        try:
            return self.__Result["line3"]
        except KeyError:
            return None

    @property
    def line4(self):
        try:
            return self.__Result["line4"]
        except KeyError:
            return None

    @property
    def house(self):
        try:
            return self.__Result["house"]
        except KeyError:
            return None

    @property
    def street(self):
        try:
            return self.__Result["street"]
        except KeyError:
            return None

    @property
    def xstreet(self):
        try:
            return self.__Result["xstreet"]
        except KeyError:
            return None

    @property
    def unittype(self):
        return self.__Result["unittype"]

    @property
    def unit(self):
        try:
            return self.__Result["unit"]
        except KeyError:
            return None

    @property
    def postal(self):
        try:
            return self.__Result["postal"]
        except KeyError:
            return None

    @property
    def neighborhood(self):
        try:
            return self.__Result["neighborhood"]
        except KeyError:
            return None

    @property
    def city(self):
        try:
            return self.__Result["city"]
        except KeyError:
            return None

    @property
    def county(self):
        try:
            return self.__Result["county"]
        except KeyError:
            return None

    @property
    def state(self):
        try:
            return self.__Result["state"]
        except KeyError:
            return None

    @property
    def country(self):
        try:
            return self.__Result["country"]
        except KeyError:
            return None

    @property
    def countrycode(self):
        try:
            return self.__Result["countrycode"]
        except KeyError:
            return None

    @property
    def statecode(self):
        try:
            return self.__Result["statecode"]
        except KeyError:
            return None

    @property
    def countrycode(self):
        try:
            return self.__Result["countycode"]
        except KeyError:
            return None

    @property
    def uzip(self):
        try:
            return self.__Result["uzip"]
        except KeyError:
            return None

    @property
    def hash(self):
        try:
            return self.__Result["hash"]
        except KeyError:
            return None

    @property
    def woeid(self):
        try:
            return self.__Result["woeid"]
        except KeyError:
            return None

    @property
    def woetype(self):
        try:
            return self.__Result["woetype"]
        except KeyError:
            return None


def query_placefinder(value, field="text"):
    query = 'select * from geo.placefinder where {0}="{1}" and gflags="R"'.format(field, value)
    yql_conector = YQLConector()
    data = yql_conector.request(query)
    return data