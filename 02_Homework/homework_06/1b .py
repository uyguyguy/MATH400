#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 12:08:29 2022

@author: hboateng

This program provides an example of truncation and round-off error
using a forward difference approximation
"""
from matplotlib import pyplot as plt
import numpy as np

# Forward difference approximation


def fwd_diff(f, x, h):
    """
    Parameters
    ----------
    f : The function to be differentiated.

    x : TYPE: float
        The point where the derivative is needed
    h : TYPE: float
        The step/discretization size (can be a list).

    Returns
    -------
    fp : Approximation to f'(x) at x (can be a list).

    """
    return (f(x+h) - f(x))/(h)


# Define the function to be differentiated and its derivative
def f(x): return np.sin(x)
def fp(x): return np.cos(x)


# The point where the derivative is needed
x = np.pi/4
exact_deriv_value = fp(x)

# The discretization sizes
h = 2**(-np.linspace(start=1, stop=6, num=6))

# Find the forward difference approximation to the derivative f'(x) for
# different h values
fpappx = fwd_diff(f, x, h)
error = exact_deriv_value - fpappx
abserror = abs(error)
eh = error/h
eh2 = error/h**2

plt.loglog(h, abserror, 'o-')
plt.xlabel('h (step size)')
plt.ylabel('error')
plt.show()

#print('h ','fpappx','error ', 'error/h')
print("\t\t%s\t\t \t\t%s\t\t \t\t%s\t\t \t\t%s \t\t \t\t\t%s \n" %
      ("h", "fappx", "error", "error/h", "error/h^2"))
for i in range(0, len(h)):
    #print(f" {h[i]}, {error[i]}, {eh[i]}")
    print("%12.8e\t\t %12.8e\t\t %12.8e\t\t %12.8e \t\t %12.8e\n" %
          (h[i], fpappx[i], error[i], eh[i], eh2[i]))
