# -*- coding: UTF-8 -*-
"""
Archivo: interface.py
Módulo que se utiliza para las consultas YQL a Yahoo para obtener información de sus servidores.
"""
__author__ = 'Alex Dzul'
import json
import sys
from pyql.settings import YAHOO_URL
from pyql.errors import YQLRequestError, format_sys_errors
from pyql.settings import MY_PY3, MY_PY2


# Importamos la librería que utilizaremos dependiendo de la versión Python.
if MY_PY2:
    from urllib2 import urlopen
if MY_PY3:
    import codecs
    from urllib.request import urlopen


class YQLConector():

    def __init__(self):
        self.__url = None
        self.__query = None

    def request(self, my_query, format_response="json"):
        """
        Realiza una consulta YQL a los servidores de Yahoo
        """
        obj = None
        url = self.yql_to_url(my_query, format_response)
        try:
            if format_response == "json":
                if MY_PY2:
                    obj = json.load(urlopen(url))
                if MY_PY3:
                    reader = codecs.getreader("utf-8")
                    obj = json.load(reader(urlopen(url)))
            if format_response == "xml":
                obj = urlopen(url).read()
            return obj
        except:
            error = "No pudismo conectarnos a los servidores de Yahoo o la consulta realizada es incorrecta. "
            error += format_sys_errors(sys, with_traceback=True)
            raise YQLRequestError(error)

    def yql_to_url(self, query, format_response="json"):
        """
        Función que se utiliza para pasar el query YQL a un link HTML para que pueda reenviarse y conectarse a los servicios
        de Yahoo.
        Obtiene 2 variables, la query a convertir, y el formato en que será devuelto; JSON ó XML.
        """
        query = query.strip()  # Quitamos los espacios a los lados
        query = query.replace(" ", "%20")  # cambiamos los espacios en blanco
        query = query.replace("=", "%3D")  # cambiamos los signos de igual "="
        query = query.replace("\"", "%22")  # Cambiamos las comillas
        query = query.replace(",", "%2C")
        url = "{0}{1}&format={2}&callback=".format(YAHOO_URL, query, format_response)
        self.__url = url
        return url

    def make_query(self, yql_table, **kwargs):
        """
        Recorre los kwargs para generar una query completa con filtros and
        :param query_base: query base para el inicio de la concatenación
        :param kwargs: Diccionario de elementos a integrar en la consulta
        :return: new_query
        """
        new_query = "Select * from {0}".format(yql_table)
        if kwargs:
            last = len(kwargs) - 1
            i_flag = 0
            new_query += ' where '
            for key, value in kwargs.items():
                if i_flag is last:  # Si es el último entonces no ponemos el "and"
                    new_query += '{0}="{1}"'.format(key, value)
                else:
                    new_query += '{0}="{1}" and '.format(key, value)
                    i_flag += 1
        self.__query = new_query
        return new_query