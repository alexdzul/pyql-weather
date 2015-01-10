# -*- coding: utf-8 -*-
__author__ = 'Alex Dzul'
from pyql.errors import MultipleValueError
from pyql.interface import YQLConector
from pyql.geo.generics import PlaceTypeName


__all__ = ('PlaceType', )

YQL_TABLE = "geo.placetypes"


class PlaceType():

    def __init__(self):
        self._Result = None
        self._count = None
        self._place_type_name = PlaceTypeName()


    @staticmethod
    def get(**kwargs):
        """
        Realizamos una consulta a la base de datos de Yahoo para obtener información de geo.placetypes.
        Nota:
        Esta función devolverá solamente un objeto.
        Si se encuentran más, entonces la función devuelve el primer resultado de la lista.

        Para obtener más de 1 resultado entonces utilizar la función filter().
        """
        connect = YQLConector()
        query = connect.make_query(YQL_TABLE, **kwargs)
        response = connect.request(query)
        my_count = response["query"]["count"]
        if my_count > 0:
            if response:
                my_count = response["query"]["count"]
                my_response = response["query"]["results"]["placeType"]
                if type(my_response) is dict:  # Si es solo un elemento entonces enviamos de manera directa
                    place = PlaceType()
                    place._count = my_count
                    place._Result = my_response
                    place._place_type_name._Result = my_response["placeTypeName"]
                    return place
                if type(my_response) is list:
                    msg = 'get function returns more than 1 value, please use "filter"'
                    raise MultipleValueError(msg)
        else:
            return None

    @staticmethod
    def filter(**kwargs):
        """
        Realiza una consulta a la base de datos de Yahoo utilizando YQL.
        El valor retornado siempre será una lista de objetos tipo "Placetypes"
        """
        connect = YQLConector()
        query = connect.make_query(YQL_TABLE, **kwargs)
        response = connect.request(query)
        my_count = response["query"]["count"]
        if my_count > 0:
            if response:
                my_count = response["query"]["count"]
                list_result = []
                my_response = response["query"]["results"]["placeType"]
                if type(my_response) is list:
                    for data in my_response:
                        place = PlaceType()
                        place._Result = data
                        place._count = my_count
                        place._place_type_name._Result = data["placeTypeName"]
                        list_result.append(place)
                if type(my_response) is dict:
                    place = PlaceType()
                    place._Result = my_response
                    place._count = my_count
                    list_result.append(place)
                return list_result
        else:
            return None

    def as_json(self):
        return self._Result

    def count(self):
        """
        Devuelve el número de registros encontrados por la consulta yql
        """
        try:
            return int(self._count)
        except StandardError:
            return 0

    @property
    def lang(self):
        try:
            return self._Result["lang"]
        except KeyError:
            return None

    @property
    def uri(self):
        try:
            return self._Result["uri"]
        except KeyError:
            return None

    @property
    def place_type_name(self):
        return self._place_type_name

    @property
    def place_type_description(self):
        try:
            return self._Result["placeTypeDescription"]
        except KeyError:
            return None