# -*- coding: utf-8 -*-
__author__ = 'Alex Dzul'
import sys


# Obtenemos la versió de Python que estamos ejecutando
MY_PY2 = sys.version_info[0] == 2
MY_PY3 = sys.version_info[0] == 3


YAHOO_URL = "http://query.yahooapis.com/v1/public/yql?q="