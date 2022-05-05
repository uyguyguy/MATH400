"""
Created on Thu Oct 28 10:32:19 2021

@author: hboateng
"""
from numpy import array
from numpy import linalg as LA
from numpy import inf
import copy

A = array([[5, 0, -1], [0, 1, 0], [0, -3, 2]])
b = array([2, 2, 4])

m = len(b)
x = array([0.0, 0, 0])  # initial vector
tol = 1e-8

n = 0  # iteration counter
x0 = copy.copy(x)
xn = 1  # dummy initial tolerance

while xn > tol:

    x[0] = (b[0] - (A[0, 1]*x0[1]))/A[0, 0]

    for i in range(1, m-1):
        x[i] = (b[i] - (A[i, i-1]*x0[i-1] + A[i, i+1]*x0[i+1]))/A[i, i]

    x[m-1] = (b[m-1] - (A[m-1, m-2]*x0[m-2]))/A[m-1, m-1]

    #xn = LA.norm(x-x0,1)
    #xn = LA.norm(x-x0,2)
    xn = LA.norm(x-x0, inf)
    x0 = copy.copy(x)
    n = n + 1

print(f" Number of iterations for Jacobi = {n}")
print(f"approximate x = {x}")
print(f"{xn}\n{tol}")
