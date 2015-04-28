# -*- coding: utf-8 -*-
__author__ = 'Alex Dzul'
import traceback


class InvalidYQLQueryError(Exception):
    pass


class YQLRequestError(Exception):
    pass


class MultipleValueError(Exception):
    pass


def format_sys_errors(user_sys, with_traceback=False):
    """
    Formatea el error obtenido en una función o documento
    """
    if user_sys:
        etype, value, tb = user_sys.exc_info()
        tipo_error_name = etype.__name__
        error_args = value.args
        if with_traceback:
            mensaje = "{0} {1} {2}".format(tipo_error_name, error_args, traceback.extract_tb(tb))
        else:
            traceback.print_tb(tb)
            mensaje = "{0} {1}".format(tipo_error_name, error_args)
        return mensaje
    else:
        return ""