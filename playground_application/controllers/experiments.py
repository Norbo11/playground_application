import connexion
import six
import logging
import time
import os
import random
import pandas as pd

import numpy as np
from flask import current_app

from playground_application.models.loaded_csv import LoadedCsv
from playground_application.models.number import Number  # noqa: E501
from playground_application import controller_util


# I/O bound
def load_large_file():
    filename = os.path.join(os.path.dirname(__file__), 'large.csv')

    df = pd.read_csv(filename)
    rows = df.to_dict()

    return LoadedCsv(rows=rows).to_dict()


# I/O bound
def sleep():
    time.sleep(3)
    return Number(42).to_dict()


# I/O bound (logging)
def log():
    for i in range(9999):
        current_app.logger.info(f"Logging number {i}")
    return Number(i).to_dict()


# CPU bound
def add_numbers():
    result = 0
    for i in range(10_000_000):
        result += random.random()

    return Number(result).to_dict()


# CPU bound
def add_numbers_numpy():
    a = np.random.randint(0, 10, size=10_000_000)
    mean = a.mean()
    std = a.std()
    variance = a.var()
    return Number(mean).to_dict()


# Exception
def throw_exception():
    raise Exception("This is an exception")
