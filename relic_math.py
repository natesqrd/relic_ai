import sympy as sp
from sympy.abc import *
from relic_nlp import *


"""
In sympy: derive, integrate, limit...
"""


def derive(expression, *symbols):
    return sp.diff(expression, *symbols)


def integral(expression):
    return sp.integrate(expression)


def zeros(expression, *symbols):
    return sp.solve(expression, *symbols)