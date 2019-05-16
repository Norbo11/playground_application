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
    current_app.logger.info('Executed one (woke up at {})', str(time.time()))
    time.sleep(1)
    return Number(1).to_dict()


def two_get():
    """Two.

    The two.


    :rtype: Number
    """
    current_app.logger.info('Executed two')
    sleep(1)
    sleep(1)
    sleep(0.5)
    controller_util.throw_exception()
    return Number(2).to_dict()


def three_get():
    """Three.

    The three.

    :rtype: Number
    """
    current_app.logger.info('Executed three')
    x = [sleep(1), sleep(1), sleep(1)]
    return Number(3).to_dict()


def load():
    df = controller_util.something()
    rows = df.to_dict()

    return LoadedCsv(rows={"1": [1.0, 2.0]}).to_dict()


def branch():
    import random

    x = random.random()
    y = 0

    sleep(0.5)

    if x < 0.7:
        y = random.random()

        if y < 0.8:
            sleep(1)
        else:
            sleep(1)

        if y < 0.4:
            sleep(1)

    sleep(1)
    return {
        'first': Number(x).to_dict(),
        'second': Number(y).to_dict()
    }


def list_comprehension():
    numbers = controller_util.list_comprehension()
    return numbers