#!/usr/bin/env python

#  Programa: main.py
# Propósito: Creación aplicación web Flask
#     Autor: Óscar García
#     Fecha: 09/12/2019 

import flask
import datetime
import os
import redis
# Crear el objeto que representa la aplicacion web
APP = flask.Flask(__name__)

redis_location = os.environ['REDIS_LOCATION']
redis_port = os.environ['REDIS_PORT']
redis_client = redis.Redis(host=redis_location , port=redis_port, db=0)

PREFIX = "webapp2024"
CONTADOR_BASE_KEY = "contador_visitas"
CONTADOR_KEY = "-".join([PREFIX, CONTADOR_BASE_KEY])

nombre = os.environ['NAME']

@APP.route('/')
def index():
    """ Muestra la página inicial asociada al recurso `/`
        y que estará contenida en el archivo index.html
    """


    contador_visitas = redis_client.incr(CONTADOR_KEY);
   # if not contador_visitas:
    #    contador_visitas = 1
    #else:
     #   contador_visitas = contador_visitas + 1
      #  redis_cli.set(CONTADOR_KEY, contador_visitas);

    return flask.render_template(
            'index.html',
            nombre=nombre,
            contador_visitas=contador_visitas,
            timestamp=datetime.datetime.now())


if __name__ == '__main__':
    APP.debug = True
    APP.run(host='0.0.0.0', port=os.environ['PORT'])
