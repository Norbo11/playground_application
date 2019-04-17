import connexion
import six
import logging
import time

from flask import current_app

from playground_application.models.loaded_csv import LoadedCsv
from playground_application.models.number import Number  # noqa: E501
from playground_application import controller_util


def sleep(i):
    time.sleep(i)
    return i

def one_get():
    """One.

    The one.


    :rtype: Number
    """
    #raise Exception('oh damn')

    current_app.logger.info('Executed one')
    time.sleep(2)


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
    x = [sleep(1), sleep(1), sleep(1)]
    return Number(3).to_dict()


def two_get():
    """Two.

    The two.


    :rtype: Number
    """
    current_app.logger.info('Executed two')
    sleep(1)
    sleep(1)
    return Number(2).to_dict()


def new_function():
    return Number(1).to_dict()


def load():
    df = controller_util.something()
    rows = df.to_dict()

    return LoadedCsv(rows={"1": [1.0, 2.0]}).to_dict()


def list_comprehension():
    numbers = controller_util.list_comprehension()
    return numbers