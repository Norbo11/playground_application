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


def report_running_time(f):
    def wrapped():
        start_time = time.time()
        f()
        end_time = time.time()
        return Number(end_time - start_time).to_dict()

    return wrapped


# I/O bound
@report_running_time
def load_large_file():
    filename = os.path.join(os.path.dirname(__file__), 'large.csv')

    df = pd.read_csv(filename)
    rows = df.to_dict()


# I/O bound
@report_running_time
def sleep():
    time.sleep(3)


# I/O bound (logging)
@report_running_time
def log():
    for i in range(9999):
        current_app.logger.info(f"Logging number {i}")


# CPU bound
@report_running_time
def add_numbers():
    result = 0
    for i in range(10_000_000):
        result += random.random()


# CPU bound
@report_running_time
def add_numbers_numpy():
    a = np.random.randint(0, 10, size=10_000_000)
    mean = a.mean()
    std = a.std()
    variance = a.var()


# Exception
@report_running_time
def throw_exception():
    raise Exception("This is an exception")
