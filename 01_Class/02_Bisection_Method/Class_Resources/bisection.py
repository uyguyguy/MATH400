"""
Created on Tue Aug 31 10:32:06 2021

@author: hboateng
bisection method
"""
import math
import sys
import numpy as np


def bisection(f, a, b, delta, return_x_list=False):
    """
    bisection method for finding the root of a 
    function f(x)

    Parameters
    ----------
    f : The function whose root we want to find.
    a : left hand side of initial interval
    b : right hand side of initial interval
    delta : error tolerance
    return_x_list : If True returns a list of
        all estimates during the iteration. 
        The default is False.

    Returns
    -------
    The estimate of the root and the number of
    iterations

    """

    fa = f(a)
    fb = f(b)  # initial values of f(a) and f(b)
    if fa*fb > 0:
        print("Error! f must have different signs at the endpoints. Aborting")
        sys.exit(1)

    print("initial interval: ", "a =", a,
          " b =", b, " f(a)=", fa, " f(b) =", fb)

    iteration_counter = 1
    if return_x_list:
        x_list = []

    while(abs(b-a) > 2*delta):  # while the size  of interval is
        # larger  than the tolerance
        c = (b+a)/2             # set c to the midpoint of the interval

        fc = f(c)               # calculate the value of f at c

        if fc*fb < 0:  # if f(c) and f(b) have different signs
            a = c
            fa = fc   # assign midpoint to a
        else:
            b = c
            fb = fc   # assign midpoint to b

        print("a =", a, " b =", b, "c =", c, " f(a) =",
              fa, " f(b) =", fb, " f(c) =", fc)

        iteration_counter += 1
        if return_x_list:
            x_list.append(c)

    if return_x_list:
        return x_list, iteration_counter
    else:
        return c, iteration_counter


def f(x):
    return x**2-3  # (5.0-x)*math.exp(x)-5


solution, no_iterations = bisection(f, 1, 2, 1e-3)
print("Number of iterations = ", no_iterations)
print("An estimate of the root is ", solution)
