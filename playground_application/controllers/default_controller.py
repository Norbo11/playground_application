import connexion
import six
import logging
import time

from flask import current_app

from playground_application.models.loaded_csv import LoadedCsv
from playground_application.models.number import Number  # noqa: E501
from playground_application import controller_util


def one_get():
    """One.

    The one.


    :rtype: Number
    """
    #raise Exception('oh damn')
    current_app.logger.info('Executed one')
    time.sleep(1)

    from pprint import pprint
    pprint(Number(1).to_dict())
    return Number(1).to_dict()


def three_get():
    """Three.

    The three.


    :rtype: Number
    """
    current_app.logger.info('Executed three ')
    time.sleep(3)
    return Number(3).to_dict()


def two_get():
    """Two.

    The two.


    :rtype: Number
    """
    current_app.logger.info('Executed two')
    time.sleep(2)
    return Number(2).to_dict()


def load():
    df = controller_util.load_large_csv()
    rows = df.to_dict()
    return LoadedCsv(rows={"1": [1.0, 2.0]}).to_dict()

