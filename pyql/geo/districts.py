# -*- coding: utf-8 -*-
__author__ = 'Alex Dzul'
from pyql.geo.generics import GenericGeoPlace
from pyql.interface import YQLConector


__all__ = ('Continent', )

YQL_TABLE = "geo.districts"


class District(GenericGeoPlace):

    @staticmethod
    def get(**kwargs):
        """
        Realiza una consulta a la base de datos de Yahoo utilizando YQL.
        El valor retornado un solo elemento. Si la consulta retorna más entonces
        se presentará un error de múltiples resultados encontrados.
        """
        connect = YQLConector()
        query = connect.make_query(YQL_TABLE, **kwargs)
        response = connect.request(query)
        if response["query"]["count"] > 0:
            return District.generic_get(response)
        else:
            raise Exception("No se encontraron resultados con los criterios especificados")

    @staticmethod
    def filter(**kwargs):
        """
        Realiza una consulta a la base de datos de Yahoo utilizando YQL.
        El valor retornado siempre será una lista de objetos tipo "District"
        """
        connect = YQLConector()
        query = connect.make_query(YQL_TABLE, **kwargs)
        response = connect.request(query)
        return District.generic_get(response)