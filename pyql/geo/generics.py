# -*- coding: utf-8 -*-
__author__ = 'Alex Dzul'
from pyql.errors import MultipleValueError

__all__ = ('GenericGeoPlace',)


class GenericGeoPlace():
    """
    Modelo genérico que se utiliza para las tablas de Yahoo que tienen la estructura del tipo:
    place: [
                {
                lang: "en-US",
                uri: "http://where.yahooapis.com/v1/place/12695819",
                woeid: "12695819",
                placeTypeName: {
                code: "10",
                content: "Local Administrative Area"
                },
                name: "City of Westminster"
                },
            ]
    """
    def __init__(self):
        self._Result = None
        self._count = None
        self._place_type_name = PlaceTypeName()

    @staticmethod
    def generic_get(response):
        my_count = response["query"]["count"]
        if my_count > 0:
            if response:
                my_response = response["query"]["results"]["place"]
                generic = GenericGeoPlace()
                generic._count = my_count
                if type(my_response) is dict:  # Si es solo un elemento entonces enviamos de manera directa
                    generic._place_type_name._Result = my_response["placeTypeName"]
                    generic._Result = my_response
                    return generic
                if type(my_response) is list:
                    msg = 'get function returns more than 1 value, please use "filter"'
                    raise MultipleValueError(msg)
        else:
            raise Exception("No se encontraron resultados con los criterios especificados")

    @staticmethod
    def generic_filter(response):
        my_count = response["query"]["count"]
        if my_count > 0:
            my_count = response["query"]["count"]
            list_result = []
            my_response = response["query"]["results"]["place"]
            if type(my_response) is list:
                for data in my_response:
                    generic = GenericGeoPlace()
                    generic._Result = data
                    generic._count = my_count
                    generic._place_type_name._Result = data["placeTypeName"]
                    list_result.append(generic)
            if type(my_response) is dict:
                generic = GenericGeoPlace()
                generic.__Result = my_response
                generic.__count = my_count
                list_result.append(generic)
            return list_result
        else:
            return None

    def as_json(self):
        return self._Result

    @property
    def place_type_name(self):
        return self._place_type_name

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
        except TypeError:
            return None

    @property
    def uri(self):
        try:
            return self._Result["uri"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def woeid(self):
        try:
            return self._Result["woeid"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def name(self):
        try:
            return self._Result["name"]
        except KeyError:
            return None
        except TypeError:
            return None


class PlaceTypeName():

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
        except TypeError:
            return None

    @property
    def content(self):
        try:
            return self._Result["content"]
        except KeyError:
            return None
        except TypeError:
            return None