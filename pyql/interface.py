# -*- coding: UTF-8 -*-
"""
Archivo: interface.py
Módulo que se utiliza para las consultas YQL a Yahoo para obtener información de sus servidores.
"""
__author__ = 'Alex Dzul'
import json
import urllib2

from pyql.settings import YAHOO_URL
from pyql.errors import YQLRequestError

class YQLConector():

    def __init__(self):
        self.url = None

    def request(self, my_query, format_response="json"):
        """
        Realiza una consulta YQL a los servidores de Yahoo
        :param my_query:
        :return:
        """
        obj = None
        self.url = self.yql_to_url(my_query, format_response)
        try:
            format_response = "json"
            if format_response == "json":
                obj = json.load(urllib2.urlopen(self.url))
            if format_response == "xml":
                obj = urllib2.urlopen(self.url).read()
            return obj
        except:
            error = "No pudismo conectarnos a los servidores de Yahoo"
            raise YQLRequestError(error)

    @staticmethod
    def yql_to_url(query, format_response="json"):
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
        return url

    @staticmethod
    def make_query(query_base, **kwargs):
        new_query = query_base
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
        return new_query