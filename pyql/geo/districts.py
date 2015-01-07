# -*- coding: utf-8 -*-
__author__ = 'Alex Dzul'
from pyql.geo.models import GenericGeoPlace
from pyql.geo.query import query_districts


__all__ = ('Continent', )


class District(GenericGeoPlace):

    @staticmethod
    def get(**kwargs):
        """
        Realiza una consulta a la base de datos de Yahoo utilizando YQL.
        El valor retornado un solo elemento. Si la consulta retorna más entonces
        se presentará un error de múltiples resultados encontrados.
        """
        response = query_districts(**kwargs)
        return District.generic_get(response)

    @staticmethod
    def filter(**kwargs):
        """
        Realiza una consulta a la base de datos de Yahoo utilizando YQL.
        El valor retornado siempre será una lista de objetos tipo "District"
        """
        response = query_districts(**kwargs)
        return District.generic_filter(response)