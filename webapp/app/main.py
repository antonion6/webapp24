#!/usr/bin/env python

#  Programa: main.py
# Propósito: Creación aplicación web Flask
#     Autor: Óscar García
#     Fecha: 09/12/2019 

import flask
import datetime
import os

# Crear el objeto que representa la aplicacion web
APP = flask.Flask(__name__)
nombre=os.environ['NAME']
contador_visitas=0


@APP.route('/')
def index():
    """ Muestra la página inicial asociada al recurso `/`
        y que estará contenida en el archivo index.html
    """
    return flask.render_template(
            'index.html',
            nombre=nombre,
            contador_visitas=contador_visitas,
            timestamp=datetime.datetime.now())


if __name__ == '__main__':
    APP.debug = True
    APP.run(host='0.0.0.0', port=os.environ['PORT'])
