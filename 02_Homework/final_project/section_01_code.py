# import math
# import numpy as np

# # 3 unknowns initial guass
# # x[0] = x, x[1] = y, x[2] = z
# x = [
#     [2],
#     [0],
#     [2]
# ]

# # 3 functions


# def f(x, y, z):
#     return x**2 + y**2 + z**2 - 10


# def g(x, y, z):
#     return x + 2*y - 2


# def h(x, y, z):
#     return x + 3*z - 9

# # Jacobi Matrix


# def fdx1(x):
#     return 2*x


# def fdx2(y):
#     return 2*y


# def fdx3(z):
#     return 2*z

# # Add more if needed


# matrixJ = [
#     [fdx1, fdx2, fdx3],
#     [1, 2, 0],
#     [1, 0, 3]
# ]

# # temp matrixJ
# matrixJtemp = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]

# # A matrix
# matrixA = [
#     [1, 1, 1],
#     [1, 2, 0],
#     [1, 0, 3]
# ]

# # initial k & b
# k, b = 0, 0

# # jacobi iteration


# def JI(matrixJ, matrixJtemp):
#     # stop iteration
#     # if (False) {
#     #     # stop
#     # }

#     # get matrixJ from guess
#     for i in matrixJ[0]:
#         matrixJtemp[0][i] = matrixJ[0][i](x[i])

#     print(matrixJtemp)
#     return 0


# print(JI(matrixJ, matrixJtemp))


# from scipy.optimize import fsolve
# import numpy as np


# def func(x):
#     return [x[0]**2 + x[1]**2 + x[2]**2 - 10,
#             x[0] + 2*x[1] + -2,
#             x[0] + 3*x[1]]


# root = fsolve(func, [2, 0, 2])

# print(root)


from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot


def jacobi(A, b, N=25, x=None):
    """Solves the equation Ax=b via the Jacobi iterative method."""
    # Create an initial guess if needed
    if x is None:
        x = zeros(len(A[0]))

    # Create a vector of the diagonal elements of A
    # and subtract them from A
    D = diag(A)
    R = A - diagflat(D)

    # Iterate for N times
    for i in range(N):
        x = (b - dot(R, x)) / D
    return x


A = array([[2.0, 1.0], [5.0, 7.0]])
b = array([11.0, 13.0])
guess = array([2, 0])

sol = jacobi(A, b, N=25, x=guess)

print("A:")
pprint(A)

print("b:")
pprint(b)

print("x:")
pprint(sol)
