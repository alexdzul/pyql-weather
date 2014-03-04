# -*- coding: UTF-8 -*-
"""
Archivo: interface.py
Módulo que se utiliza para las consultas YQL a Yahoo para obtener información de sus servidores.
"""
__author__ = 'Alex Dzul'
import simplejson
import urllib2
yahoo_url = "http://query.yahooapis.com/v1/public/yql?q="




def get_geo_data(latitude,longitude):
    """
    Función que se utiliza para la obtención de datos geográficos de una latitude y longitude recibida.
    El resultado es un objeto tipo JSON
    """
    query = "select * from geo.placefinder where text=\"%s,%s\" and gflags=\"R\"" % (latitude, longitude)
    url = yql_to_url(query)
    obj = simplejson.load(urllib2.urlopen(url))
    return obj


def get_weather_data(woeid, unit_temp="c"):
    """
    Función que se utiliza para obtener información del tiempo y Clima de un WOEID recibido.
    El resultado es un objeto tipo JSON.
    """
    if unit_temp == "c":
        query = "select * from weather.forecast where woeid=%s AND u=\"%s\""%(woeid, unit_temp)
    if unit_temp == "f":
        query = "select * from weather.forecast where woeid=%s AND u=\"%s\""%(woeid, unit_temp)
    url = yql_to_url(query)
    obj = simplejson.load(urllib2.urlopen(url))
    return obj


def yql_to_url(query, format="json"):
    """
    Función que se utiliza para pasar el query YQL a un link HTML para que pueda reenviarse y conectarse a los servicios
    de Yahoo.
    Obtiene 2 variables, la query a convertir, y el formato en que será devuelto; JSON ó XML.
    """
    if format == "json":
        format_data = "format=json"
    if format == "xml":
        format_data = "format=xml"
    #Quitamos los espacios a los lados
    query = query.strip()
    # cambiamos los espacios en blanco
    query =  query.replace(" ","%20")
    #cambiamos los signos de igual "="
    query = query.replace("=","%3D")
    #Cambiamos las comillas
    query = query.replace("\"","%22")
    query = query.replace(",","%2C")
    nQuery = yahoo_url+query
    nQuery = "%s%s&%s&callback="%(yahoo_url, query, format_data)
    return nQuery