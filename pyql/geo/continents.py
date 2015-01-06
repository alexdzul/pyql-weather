# -*- coding: utf-8 -*-
__author__ = 'Alex Dzul'
from pyql.interface import YQLConector

class Continent():

    def __init__(self):
        self.__Result = None
        self.__count = None
        self.__place_type_name = _PlaceTypeName()

    def as_json(self):
        return self.__Result

    @staticmethod
    def get(**kwargs):
        response = query_continent(**kwargs)
        if response:
            my_count = response["query"]["count"]
            my_response = response["query"]["results"]["place"]
            continent = Continent()
            continent.__count = my_count
            if type(my_response) is dict:  # Si es solo un elemento entonces enviamos de manera directa
                continent.__place_type_name._Result = my_response["placeTypeName"]
                continent.__Result = my_response
            if type(my_response) is list:
                continent.__Result = my_response[0]  # Si es una lista entonces enviamos solo el primer elemento
                continent.__place_type_name._Result = my_response[0]["placeTypeName"]
            return continent

    @property
    def place_type_name(self):
        return self.__place_type_name

    @property
    def lang(self):
        try:
            return self.__Result["lang"]
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
    def name(self):
        try:
            return self.__Result["name"]
        except KeyError:
            return None


class _PlaceTypeName():

    def __init__(self):
        self._Result = None

    def as_json(self):
        """
        Retorna la información en json
        """
        return self._Result

    @property
    def code(self):
        try:
            return self._Result["code"]
        except KeyError:
            return None

    @property
    def content(self):
        try:
            return self._Result["content"]
        except KeyError:
            return None


def query_continent(**kwargs):
    """
    Realizamos la consulta a la tabla geo.continents
    """
    query_base = 'select * from geo.continents'
    if kwargs:
        last = len(kwargs) - 1
        i_flag = 0
        query_base += ' where '
        for key, value in kwargs.items():
            if i_flag is last:  # Si es el último entonces no ponemos el "and"
                query_base += '{0}={1}'.format(key, value)
            else:
                query_base += '{0}={1} and '.format(key, value)
    yql_connector = YQLConector()
    data = yql_connector.request(query_base)
    return data