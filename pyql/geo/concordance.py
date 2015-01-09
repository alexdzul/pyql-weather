# -*- coding: utf-8 -*-
__author__ = 'Alex Dzul'
from pyql.errors import MultipleValueError
from pyql.geo.query import query_concordance


__all__ = ('Concordance', )


class Concordance():

    def __init__(self):
        self.__Result = None
        self.__count = None

    def as_json(self):
        """
        Devolvemos los resultados en formato JSON
        """
        return self.__Result

    @staticmethod
    def get(**kwargs):
        """
        Realizamos una consulta a la base de datos de Yahoo para obtener información de geo.concordance.
        Nota:
        Esta función devolverá solamente un objeto.
        Si se encuentran más, entonces la función devuelve el primer resultado de la lista.

        Para obtener más de 1 resultado entonces utilizar la función filter().
        """
        response = query_concordance(**kwargs)
        my_count = response["query"]["count"]
        if my_count > 0:
            if response:
                my_response = response["query"]["results"]["concordance"]
                if type(my_response) is dict:  # Si es solo un elemento entonces enviamos de manera directa
                    place = Concordance()
                    place.__count = my_count
                    place.__Result = my_response
                    return place
                if type(my_response) is list:
                    msg = 'get function returns more than 1 value, please use "filter"'
                    raise MultipleValueError(msg)
        else:
            return None

    def count(self):
        """
        Devuelve el número de registros encontrados por la consulta yql
        """
        try:
            return int(self.__count)
        except StandardError:
            return 0

    @property
    def lang(self):
        try:
            return self.__Result["lang"]
        except KeyError:
            return None

    @property
    def xmlns(self):
        try:
            return self.__Result["xmlns"]
        except KeyError:
            return None

    @property
    def yahoo(self):
        try:
            return self.__Result["yahoo"]
        except KeyError:
            return None

    @property
    def uri(self):
        try:
            return self.__Result["uri"]
        except KeyError:
            return None

    @property
    def woeid(self):
        try:
            return self.__Result["woeid"]
        except KeyError:
            return None

    @property
    def iata(self):
        try:
            return self.__Result["iata"]
        except KeyError:
            return None

    @property
    def icao(self):
        try:
            return self.__Result["icao"]
        except KeyError:
            return None

    @property
    def faa(self):
        try:
            return self.__Result["faa"]
        except KeyError:
            return None

    @property
    def geonames(self):
        try:
            return self.__Result["geonames"]
        except KeyError:
            return None

    @property
    def osm(self):
        try:
            return self.__Result["osm"]
        except KeyError:
            return None