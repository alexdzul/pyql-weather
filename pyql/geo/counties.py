# -*- coding: utf-8 -*-
__author__ = 'Alex Dzul'
from pyql.geo.generics import GenericGeoPlace
from pyql.geo.query import query_counties


__all__ = ('Countie', )


class Countie(GenericGeoPlace):

    @staticmethod
    def get(**kwargs):
        """
        Realiza una consulta a la base de datos de Yahoo utilizando YQL.
        El valor retornado un solo elemento. Si la consulta retorna más entonces
        se presentará un error de múltiples resultados encontrados.
        """
        response = query_counties(**kwargs)
        return Countie.generic_get(response)

    @staticmethod
    def filter(**kwargs):
        """
        Realiza una consulta a la base de datos de Yahoo utilizando YQL.
        El valor retornado siempre será una lista de objetos tipo "Continents"
        """
        response = query_counties(**kwargs)
        return Countie.generic_filter(response)