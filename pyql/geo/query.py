# -*- coding: utf-8 -*-
__author__ = 'alex'
from pyql.interface import YQLConector


def query_oceans(**kwargs):
    """
    Realizamos la consulta a la tabla geo.continents
    """
    query_base = 'select * from geo.oceans'
    full_query = YQLConector.make_query(query_base, **kwargs)
    yql_connector = YQLConector()
    data = yql_connector.request(full_query)
    return data


def query_placefinder(**kwargs):
    # query_base = 'select * from geo.placefinder where {0}="{1}" and gflags="R"'.format(field, value)
    query_base = 'select * from geo.placefinder'
    full_query = YQLConector.make_query(query_base, **kwargs)
    full_query += ' and gflags="R"'  # Se agrega esta entrada especial
    yql_connector = YQLConector()
    data = yql_connector.request(full_query)
    return data


def query_continent(**kwargs):
    """
    Realizamos la consulta a la tabla geo.continents
    """
    query_base = 'select * from geo.continents'
    full_query = YQLConector.make_query(query_base, **kwargs)
    yql_connector = YQLConector()
    data = yql_connector.request(full_query)
    return data


def query_districts(**kwargs):
    """
    Realizamos la consulta a la tabla geo.districts
    """
    query_base = 'select * from geo.districts'
    full_query = YQLConector.make_query(query_base, **kwargs)
    print full_query
    yql_connector = YQLConector()
    data = yql_connector.request(full_query)
    return data

def query_counties(**kwargs):
    """
    Realizamos la consulta a la tabla geo.districts
    """
    query_base = 'select * from geo.counties'
    full_query = YQLConector.make_query(query_base, **kwargs)
    print full_query
    yql_connector = YQLConector()
    data = yql_connector.request(full_query)
    return data


def query_countries(**kwargs):
    """
    Realizamos la consulta a la tabla geo.districts
    """
    query_base = 'select * from geo.countries'
    full_query = YQLConector.make_query(query_base, **kwargs)
    print full_query
    yql_connector = YQLConector()
    data = yql_connector.request(full_query)
    return data


def query_states(**kwargs):
    """
    Realizamos la consulta a la tabla geo.districts
    """
    query_base = 'select * from geo.states'
    full_query = YQLConector.make_query(query_base, **kwargs)
    print full_query
    yql_connector = YQLConector()
    data = yql_connector.request(full_query)
    return data


def query_seas(**kwargs):
    """
    Realizamos la consulta a la tabla geo.districts
    """
    query_base = 'select * from geo.seas'
    full_query = YQLConector.make_query(query_base, **kwargs)
    print full_query
    yql_connector = YQLConector()
    data = yql_connector.request(full_query)
    return data


def query_concordance(**kwargs):
    """
    Realizamos la consulta a la tabla geo.concordance
    """
    query_base = 'select * from geo.concordance'
    full_query = YQLConector.make_query(query_base, **kwargs)
    print full_query
    yql_connector = YQLConector()
    data = yql_connector.request(full_query)
    return data
