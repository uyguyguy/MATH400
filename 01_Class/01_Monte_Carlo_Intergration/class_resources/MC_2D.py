#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:59:53 2022

@author: hboateng
"""
# This function is adapted from the book Programming for Computations - Python
import numpy as np


def MonteCarlo_double(f, g, x0, x1, y0, y1, n):
    """
    Monte Carlo integration of f over a domain g, embedded in a rectangle [x0, x1] x [y0, y1].
    The number of random points is n**2

    """
    # Draw n random points in the rectangle
    x = np.random.uniform(x0, x1, n)
    y = np.random.uniform(y0, y1, n)
    # Compute sum of f values inside the integration domain
    f_sum = 0.0
    num_inside = 0  # number of points inside domain (g)
    for i in range(n):
        for j in range(n):
            if g(x[i], y[j]):
                num_inside += 1
                f_sum += f(x[i], y[j])
    area = (x1-x0)*(y1-y0)  # Area of rectangle
    fav = f_sum/float(n**2)  # Average of function
    return area * fav


def g(x, y):
    return (True if (x**2 + y**2 <= 4) else False)


I = MonteCarlo_double(lambda x, y: np.e**(x**2+y**2), g, -2, 2, -2, 2, 2000)

print(f"The value of the integral is {I}")
