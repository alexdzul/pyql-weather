# -*- coding: utf-8 -*-
__author__ = 'Alex Dzul'
from pyql.geo.generics import PlaceTypeName
from pyql.errors import MultipleValueError
from pyql.interface import YQLConector


__all__ = ('Place', )

YQL_TABLE = "geo.places"


class Place():
    """
    Consulta la información del elemento geo.place de Yahoo YQL
    """

    def __init__(self):
        self.__Result = None
        self.__count = None
        self.__place_type_name = PlaceTypeName()
        self.__country = _Country()
        self.__admin1 = _Admin()
        self.__admin2 = _Admin()
        self.__admin3 = _Admin()
        self.__locality1 = _Locality()
        self.__locality2 = _Locality()
        self.__postal = _Postal()
        self.__centroid = _Centroid()
        self.__bounding_box = _BoundingBox()
        self.__timezone = _TimeZone()

    def as_json(self):
        """
        Devolvemos los resultados en formato JSON
        """
        return self.__Result

    @staticmethod
    def get(**kwargs):
        """
        Realizamos una consulta a la base de datos de Yahoo para obtener información de geo.place.
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
                my_response = response["query"]["results"]["place"]
                if type(my_response) is dict:  # Si es solo un elemento entonces enviamos de manera directa
                    place = Place()
                    place.__count = my_count
                    place.__Result = my_response
                    try:
                        place.__place_type_name._Result = my_response["placeTypeName"]
                    except KeyError:
                        pass
                    try:
                        place.__country._Result = my_response["country"]
                    except KeyError:
                        pass
                    try:
                        place.__admin1._Result = my_response["admin1"]
                    except KeyError:
                        pass
                    try:
                        place.__admin2._Result = my_response["admin2"]
                    except KeyError:
                        pass
                    try:
                        place.__admin3._Result = my_response["admin3"]
                    except KeyError:
                        pass
                    try:
                        place.__locality1._Result = my_response["locality1"]
                    except KeyError:
                        pass
                    try:
                        place.__locality2._Result = my_response["locality2"]
                    except KeyError:
                        pass
                    try:
                        place.__postal._Result = my_response["postal"]
                    except KeyError:
                        pass
                    try:
                        place.__centroid._Result = my_response["centroid"]
                    except KeyError:
                        pass
                    try:
                        northeast = _NorthEast()
                        northeast._Result = my_response["boundingBox"]["northEast"]
                        place.__bounding_box._north_east = northeast
                    except KeyError:
                        pass
                    try:
                        southwest = _SouthWest()
                        southwest._Result = my_response["boundingBox"]["southWest"]
                        place.__bounding_box._south_west = southwest
                    except KeyError:
                        pass
                    try:
                        place.__timezone._Result = my_response["timezone"]
                    except KeyError:
                        pass
                    return place
                if type(my_response) is list:
                    msg = 'get function returns more than 1 value, please use "filter"'
                    raise MultipleValueError(msg)
        else:
            raise Exception("No se encontraron resultados con los criterios especificados")

    @staticmethod
    def filter(**kwargs):
        """
        Realiza una consulta a la base de datos de Yahoo utilizando YQL.
        El valor retornado siempre será una lista de objetos tipo "PlaceFinder"
        """
        connect = YQLConector()
        query = connect.make_query(YQL_TABLE, **kwargs)
        response = connect.request(query)
        my_count = response["query"]["count"]
        if my_count > 0:
            if response:
                list_result = []
                responses = response["query"]["results"]["place"]
                if type(responses) is list:
                    for my_response in responses:
                        place = Place()
                        place.__count = my_count
                        place.__Result = my_response
                        try:
                            place.__place_type_name._Result = my_response["placeTypeName"]
                        except KeyError:
                            pass
                        try:
                            place.__country._Result = my_response["country"]
                        except KeyError:
                            pass
                        try:
                            place.__admin1._Result = my_response["admin1"]
                        except KeyError:
                            pass
                        try:
                            place.__admin2._Result = my_response["admin2"]
                        except KeyError:
                            pass
                        try:
                            place.__admin3._Result = my_response["admin3"]
                        except KeyError:
                            pass
                        try:
                            place.__locality1._Result = my_response["locality1"]
                        except KeyError:
                            pass
                        try:
                            place.__locality2._Result = my_response["locality2"]
                        except KeyError:
                            pass
                        try:
                            place.__postal._Result = my_response["postal"]
                        except KeyError:
                            pass
                        try:
                            place.__centroid._Result = my_response["centroid"]
                        except KeyError:
                            pass
                        try:
                            northeast = _NorthEast()
                            northeast._Result = my_response["boundingBox"]["northEast"]
                            place.__bounding_box._north_east = northeast
                        except KeyError:
                            pass
                        try:
                            southwest = _SouthWest()
                            southwest._Result = my_response["boundingBox"]["southWest"]
                            place.__bounding_box._south_west = southwest
                        except KeyError:
                            pass
                        try:
                            place.__timezone._Result = my_response["timezone"]
                        except KeyError:
                            pass
                        list_result.append(place)
                if type(responses) is dict:
                    place = Place()
                    place.__count = my_count
                    my_response = responses
                    place.__Result = my_response
                    try:
                        place.__place_type_name._Result = my_response["placeTypeName"]
                    except KeyError:
                        pass
                    try:
                        place.__country._Result = my_response["country"]
                    except KeyError:
                        pass
                    try:
                        place.__admin1._Result = my_response["admin1"]
                    except KeyError:
                        pass
                    try:
                        place.__admin2._Result = my_response["admin2"]
                    except KeyError:
                        pass
                    try:
                        place.__admin3._Result = my_response["admin3"]
                    except KeyError:
                        pass
                    try:
                        place.__locality1._Result = my_response["locality1"]
                    except KeyError:
                        pass
                    try:
                        place.__locality2._Result = my_response["locality2"]
                    except KeyError:
                        pass
                    try:
                        place.__postal._Result = my_response["postal"]
                    except KeyError:
                        pass
                    try:
                        place.__centroid._Result = my_response["centroid"]
                    except KeyError:
                        pass
                    try:
                        northeast = _NorthEast()
                        northeast._Result = my_response["boundingBox"]["northEast"]
                        place.__bounding_box._north_east = northeast
                    except KeyError:
                        pass
                    try:
                        southwest = _SouthWest()
                        southwest._Result = my_response["boundingBox"]["southWest"]
                        place.__bounding_box._south_west = southwest
                    except KeyError:
                        pass
                    try:
                        place.__timezone._Result = my_response["timezone"]
                    except KeyError:
                        pass
                    list_result.append(place)
                return list_result
        else:
            raise Exception("No se encontraron resultados con los criterios especificados")

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
        except TypeError:
            return None

    @property
    def uri(self):
        try:
            return self.__Result["uri"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def woeid(self):
        try:
            return self.__Result["woeid"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def place_type_name(self):
        return self.__place_type_name

    @property
    def name(self):
        try:
            return self.__Result["name"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def country(self):
        return self.__country

    @property
    def admin1(self):
        return self.__admin1

    @property
    def admin2(self):
        return self.__admin2

    @property
    def admin3(self):
        return self.__admin3

    @property
    def locality1(self):
        return self.__locality1

    @property
    def locality2(self):
        return self.__locality2

    @property
    def postal(self):
        return self.__postal

    @property
    def centroid(self):
        return self.__centroid

    @property
    def bounding_box(self):
        return self.__bounding_box

    @property
    def area_rank(self):
        try:
            return self.__Result["areaRank"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def pop_rank(self):
        try:
            return self.__Result["popRank"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def timezone(self):
        return self.__timezone

class _Country():

    def __init__(self):
        self._Result = None

    @property
    def code(self):
        try:
            return self._Result["code"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def type(self):
        try:
            return self._Result["type"]
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
    def content(self):
        try:
            return self._Result["content"]
        except KeyError:
            return None
        except TypeError:
            return None


class _Admin():

    def __init__(self):
        self._Result = None

    @property
    def code(self):
        try:
            return self._Result["code"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def type(self):
        try:
            return self._Result["type"]
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
    def content(self):
        try:
            return self._Result["content"]
        except KeyError:
            return None
        except TypeError:
            return None


class _Locality():

    def __init__(self):
        self._Result = None

    @property
    def type(self):
        try:
            return self._Result["type"]
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
    def content(self):
        try:
            return self._Result["content"]
        except KeyError:
            return None
        except TypeError:
            return None


class _Postal():

    def __init__(self):
        self._Result = None

    @property
    def type(self):
        try:
            return self._Result["type"]
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
    def content(self):
        try:
            return self._Result["content"]
        except KeyError:
            return None
        except TypeError:
            return None


class _Centroid():

    def __init__(self):
        self._Result = None

    @property
    def longitude(self):
        try:
            return self._Result["longitude"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def latitude(self):
        try:
            return self._Result["latitude"]
        except KeyError:
            return None
        except TypeError:
            return None


class _BoundingBox():

    def __init__(self):
        self._south_west = _SouthWest()
        self._north_east = _NorthEast()

    @property
    def south_west(self):
        return self._south_west

    @property
    def north_east(self):
        return self._north_east


class _NorthEast():

    def __init__(self):
        self._Result = None

    @property
    def longitude(self):
        try:
            return self._Result["longitude"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def latitude(self):
        try:
            return self._Result["latitude"]
        except KeyError:
            return None
        except TypeError:
            return None


class _SouthWest():

    def __init__(self):
        self._Result = None

    @property
    def longitude(self):
        try:
            return self._Result["longitude"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def latitude(self):
        try:
            return self._Result["latitude"]
        except KeyError:
            return None
        except TypeError:
            return None


class _TimeZone():

    def __init__(self):
        self._Result = None

    @property
    def type(self):
        try:
            return self._Result["type"]
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
    def content(self):
        try:
            return self._Result["content"]
        except KeyError:
            return None
        except TypeError:
            return None