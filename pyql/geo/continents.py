# -*- coding: utf-8 -*-
__author__ = 'Alex Dzul'
from pyql.errors import MultipleValueError
from pyql.interface import YQLConector


__all__ = ('Continent', )


class Continent():

    def __init__(self):
        self.__Result = None
        self.__count = None
        self.__place_type_name = _PlaceTypeName()

    def as_json(self):
        return self.__Result

    @staticmethod
    def get(**kwargs):
        response = _query_continent(**kwargs)
        my_count = response["query"]["count"]
        if my_count > 0:
            if response:
                my_response = response["query"]["results"]["place"]
                continent = Continent()
                continent.__count = my_count
                if type(my_response) is dict:  # Si es solo un elemento entonces enviamos de manera directa
                    continent.__place_type_name._Result = my_response["placeTypeName"]
                    continent.__Result = my_response
                    return continent
                if type(my_response) is list:
                    msg = 'get function returns more than 1 value, please use "filter"'
                    raise MultipleValueError(msg)
        else:
            return None

    @staticmethod
    def filter(**kwargs):
        """
        Realiza una consulta a la base de datos de Yahoo utilizando YQL.
        El valor retornado siempre será una lista de objetos tipo "Continent"
        """
        response = _query_continent(**kwargs)
        my_count = response["query"]["count"]
        if my_count > 0:
            my_count = response["query"]["count"]
            list_result = []
            my_response = response["query"]["results"]["place"]
            if type(my_response) is list:
                for data in my_response:
                    continent = Continent()
                    continent.__Result = data
                    continent.__count = my_count
                    continent.__place_type_name._Result = data["placeTypeName"]
                    list_result.append(continent)
            if type(my_response) is dict:
                continent = Continent()
                continent.__Result = my_response
                continent.__count = my_count
                list_result.append(continent)
            return list_result
        else:
            return None

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


def _query_continent(**kwargs):
    """
    Realizamos la consulta a la tabla geo.continents
    """
    query_base = 'select * from geo.continents'
    full_query = YQLConector.make_query(query_base, **kwargs)
    yql_connector = YQLConector()
    data = yql_connector.request(full_query)
    return data