#!/usr/bin/env python3

import connexion
import logging.config
from flask import Flask, after_this_request, request

from feedback_wrapper.instrument_flask import instrument_flask
from playground_application.encoder import JSONEncoder
from datetime import datetime

import os
import sys

app = connexion.App(__name__, specification_dir='./openapi/')
app.add_api('openapi.yaml', arguments={'title': 'Playground Application'})

flask_app = app.app
flask_app.json_encoder = JSONEncoder

#flask_app.config.update(
#    ENV='development',
#    DEBUG=True,
#)

logging.config.dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})

instrument_flask(flask_app, './feedback.yaml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=flask_app.config['DEBUG'])
