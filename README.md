pyql-weather
============

Wrapper escrito en Python para realizar consultar YQL y obtener información de los servidores de Yahoo.

Compatibilidad
--------------

Pyql-Weather tiene compatibilidad con las versiones 2 y 3 de Python.

Requerimientos
--------------

Gracias a que utiliza las librerías estándar de Python, ``pyql-weather`` no necesita de ninguna otra dependencia 
más que el lenguaje Python instalado en el equipo que será ejecutado.

Instalación
-----------

La manera fácil de instalar la librería es a través de la herramienta pip::

    pip install pyql-weather

o de igual manera se puede descargar directamente desde el repositorio de Github::

    1. https://github.com/alexdzul/pyql-weather/tree/0.2.x

y ejecutar el siguiente comando::

    python setup.py install


Acceso a tablas
---------------

Se tiene disponible el acceso a las siguientes tablas:


* geo.continents
* geo.counties
* geo.countries
* geo.seas
* geo.placetypes
* geo.placefinder
* geo.places
* geo.concordance
* geo.states
* geo.oceans
* geo.districs
* weather.forecast

Características adicionales:
----------------------------

Adicional a estas tablas, existe un objeto llamado:

   + YQLConnector

El cual nos permite ejecutar consultas YQL personalizadas a Yahoo.


Documentación
-------------

Si deseas leer más sobre esta librería, te recomiendo ingresar a:

* http://pyql-weather.readthedocs.org


Autor
=====

Alex Dzul

* Python & Django Developer.

1. http://alexdzul.com
2. http://github.com/alexdzul
3. http://twitter.com/alexjs88

Licencia MIT
============

``pyql-weather`` mantiene la licencia MIT la cual define::

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.