#!/usr/bin/env python3

import connexion
from flask import Flask, after_this_request, request

from feedback_wrapper.instrument_flask import instrument_flask
from playground_application.encoder import JSONEncoder
from datetime import datetime

import os
import sys

app = connexion.App(__name__, specification_dir='./swagger/')
app.add_api('swagger.yaml', arguments={'title': 'Playground Application'})

flask_app = app.app
flask_app.json_encoder = JSONEncoder
flask_app.config.update(
    ENV='development',
    DEBUG=True,
)

# TODO: More robust way of providing path?

base_path = os.path.split(os.path.dirname(sys.argv[0]))[0]
instrument_flask(flask_app, base_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
