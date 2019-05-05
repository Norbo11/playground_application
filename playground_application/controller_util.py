import pandas as pd
import math

from playground_application.models import Number


def load_large_csv():
    df = pd.read_csv("playground_application/large.csv")
    return df


def list_comprehension():
    return [Number(math.factorial(i))
            for i
            in range(1_000)]


def throw_exception():
    raise Exception('oh damn')

