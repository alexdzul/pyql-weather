# -*- coding: utf-8 -*-
__author__ = 'Alex Dzul'
from pyql.interface import YQLConector

__all__ = ('Forecast', )

YQL_TABLE = "weather.forecast"


class Forecast:
    """
    Objeto que almacena los datos del clima y tiempo de un WOEID dado. Esta información es obtenida de los
    servicios de Yahoo.
    """

    def __init__(self):
        self.__Result = None
        self.__count = None
        self.__as_json = None
        self.__as_xml = None
        self.__item = _Item()
        self.__location = _Location()
        self.__units = _Units()
        self.__wind = _Wind()
        self.__atmosphere = _Atmosphere()
        self.__astronomy = _Astronomy()
        self.__image = _Image()

    @staticmethod
    def get(**kwargs):
        """
        Constructor del objeto Weather, se alimenta inicialmente de un WOEID para obtener información del clima.
        Posteriomente se puede consultar más información del clima utilizando las funciones que contiene.
        """
        connect = YQLConector()
        query = connect.make_query(YQL_TABLE, **kwargs)
        response = connect.request(query)
        my_count = response["query"]["count"]
        if my_count:
            if response:
                my_count = response["query"]["count"]
                channel = response["query"]["results"]["channel"]
                forecast = Forecast()
                forecast.__count = my_count
                forecast.__Result = channel
                try:
                    forecast.__item._Result = channel["item"]  # LLenamos el objeto tipo item
                except KeyError:
                    pass
                try:
                    forecast.__location._Result = channel["location"]  # Llenamos el objeto tipo location
                except KeyError:
                    pass
                try:
                    forecast.__units._Result = channel["units"]  # Llenamos el objeto tipo location
                except KeyError:
                    pass
                try:
                    forecast.__wind._Result = channel["wind"]  # Llenamos el objeto tipo location
                except:
                    pass
                try:
                    forecast.__atmosphere._Result = channel["atmosphere"]  # Llenamos el objeto tipo atmosphere
                except KeyError:
                    pass
                try:
                    forecast.__astronomy._Result = channel["astronomy"]  # Llenamos el objeto tipo astronomy
                except KeyError:
                    pass
                try:
                    forecast.__image._Result = channel["image"]  # Llenamos el objeto tipo image
                except KeyError:
                    pass
                try:
                    condition = _Condition()  # Creamos un elemento del tipo Condition
                except KeyError:
                    pass
                try:
                    condition._Result = channel["item"]["condition"]  # Inicializamos el valor de __Result
                except KeyError:
                    pass
                try:
                    forecast.__item._condition = condition  # Asignamos el objeto al objeto principal forecast
                except:
                    pass
                return forecast
        else:
            return None

    def count(self):
        """
        Retorna el número de elementos devueltos
        """
        return self.__count

    def as_json(self):
        """
        Devuelve la información en Json
        """
        return self.__Result

    @property
    def title(self):
        try:
            return self.__Result["title"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def link(self):
        try:
            return self.__Result["link"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def description(self):
        try:
            return self.__Result["description"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def language(self):
        try:
            return self.__Result["languaje"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def last_build_date(self):
        try:
            return self.__Result["lastBuildDate"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def ttl(self):
        try:
            return self.__Result["ttl"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def location(self):
        return self.__location

    @property
    def units(self):
        return self.__units

    @property
    def wind(self):
        return self.__wind

    @property
    def atmosphere(self):
        return self.__atmosphere

    @property
    def astronomy(self):
        return self.__astronomy

    @property
    def image(self):
        return self.__image

    @property
    def item(self):
        return self.__item


class _Units():

    def __init__(self):
        self._Result = None

    def as_json(self):
        """
        Devuelve la información en JSON
        """
        return self._Result

    @property
    def distance(self):
        try:
            return self._Result["distance"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def pressure(self):
        try:
            return self._Result["pressure"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def speed(self):
        try:
            return self._Result["speed"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def temperature(self):
        try:
            return self._Result["temperature"]
        except KeyError:
            return None
        except TypeError:
            return None


class _Wind():

    def __init__(self):
        self._Result = None

    def as_json(self):
        """
        Devuelve la información en JSON
        """
        return self._Result

    @property
    def chill(self):
        try:
            return self._Result["chill"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def direction(self):
        try:
            return self._Result["direction"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def speed(self):
        try:
            return self._Result["speed"]
        except KeyError:
            return None
        except TypeError:
            return None


class _Atmosphere():

    def __init__(self):
        self._Result = None

    def as_json(self):
        """
        Devuelve la información en JSON
        """
        return self._Result

    @property
    def humidity(self):
        try:
            return self._Result["humidity"]
        except KeyError:
            return None

    @property
    def pressure(self):
        try:
            return self._Result["pressure"]
        except KeyError:
            return None

    @property
    def rising(self):
        try:
            return self._Result["rising"]
        except KeyError:
            return None

    @property
    def visibility(self):
        try:
            return self._Result["visibility"]
        except KeyError:
            return None


class _Astronomy():

    def __init__(self):
        self._Result = None

    def as_json(self):
        """
        Devuelve la información en JSON
        """
        return self._Result

    @property
    def sunrise(self):
        try:
            return self._Result["sunrise"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def sunset(self):
        try:
            return self._Result["sunset"]
        except KeyError:
            return None
        except TypeError:
            return None


class _Image():

    def __init__(self):
        self._Result = None

    def as_json(self):
        """
        Devuelve la información en JSON
        """
        return self._Result

    @property
    def title(self):
        try:
            return self._Result["title"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def width(self):
        try:
            return self._Result["width"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def height(self):
        try:
            return self._Result["height"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def link(self):
        try:
            return self._Result["link"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def url(self):
        try:
            return self._Result["url"]
        except KeyError:
            return None
        except TypeError:
            return None


class _Location():

    def __init__(self):
        self._Result = None

    def as_json(self):
        """
        Devuelve la información en JSON
        """
        return self._Result

    @property
    def city(self):
        try:
            return self._Result["city"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def region(self):
        try:
            return self._Result["region"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def country(self):
        try:
            return self._Result["country"]
        except KeyError:
            return None
        except TypeError:
            return None


class _Item():

    def __init__(self):
        self._Result = None
        self._condition = _Condition()

    def as_json(self):
        """
        Devuelve la información en Json
        """
        return self._Result
    @property
    def title(self):
        try:
            return self._Result["title"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def lat(self):
        try:
            return self._Result["lat"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def long(self):
        try:
            return self._Result["long"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def link(self):
        try:
            return self._Result["link"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def pubdate(self):
        try:
            return self._Result["pubdate"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def description(self):
        try:
            return self._Result["description"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def condition(self):
        return self._condition

    @property
    def forecast(self):
        """
        Esta propiedad envía información en formato JSON del pronóstico de los siguientes 5 días.
        Los valores que podemos obtener son:
        1. code
        2. text
        3. high
        4. low
        5. date
        6. day

        Se puede acceder a ellos de la siguiente manera:

        forecast = Forecast.get(woeid)
        for day in forecast.item.forecast:
            print(day["code"])
            print(day["text])
            print(day["high])
            .....
        """
        try:
            return self._Result["forecast"]
        except KeyError:
            return None
        except TypeError:
            return None


class _Condition():

    def __init__(self):
        self._Result = None

    def as_json(self):
        """
        Devuelve la información en Json
        """
        return self._Result

    @property
    def date(self):
        try:
            return self._Result["date"]
        except KeyError:
            return None
        except TypeError:
            return None

    @property
    def text(self):
        try:
            return self._Result["text"]
        except KeyError:
            return None

    @property
    def code(self):
        try:
            return self._Result["code"]
        except KeyError:
            return None
        except TypeError:
            return None


    @property
    def temp(self):
        try:
            return self._Result["temp"]
        except KeyError:
            return None
        except TypeError:
            return None