# TODO: use sparseness

import numpy as np
from numpy import linalg as LA
from numpy import inf
import copy

A = [
    [4, -1, 0, -2, 0, 0],
    [-1, 4, -1, 0, -2, 0],
    [0, -1, 4, 0, 0, -2],
    [-1, 0, 0, 4, -1, 0],
    [0, -1, 0, -1, 4, -1],
    [0, 0, -1, 0, -1, 4]
]

b = [-1, 0, 1, -2, 1, 2]


def sumAbs(numArray):
    sumAbs = 0
    for i in range(0, len(numArray)):
        sumAbs = sumAbs + abs(numArray[i])
    return sumAbs


def normInf(matrix):
    norm = 0
    for i in range(0, len(matrix)):
        # print("i:", i)
        if (isinstance(matrix[i], list)):
            norm = max(norm, sumAbs(matrix[i]))
        else:
            norm = max(norm, abs(matrix[i]))
    return norm


def jacobi(A, xk0, b, tol):
    # value of x1 ~ x6 of k+1
    xk1 = xk0[:]  # make a copy of xk0
    E = [1, 1, 1, 1, 1, 1]  # E = x^(k+1) - x^k
    e = 1  # e = ||E||
    numIteration = 0
    while (e > tol):
        # count iteration times
        numIteration = numIteration + 1

        # x1
        xk1[0] = (b[0] - (A[0][1]*xk0[1] + A[0][2]*xk0[2] + A[0][3] *
                          xk0[3] + A[0][4]*xk0[4] + A[0][5]*xk0[5])) / A[0][0]
        # x2
        xk1[1] = (b[1] - (A[1][0]*xk0[0] + A[1][2]*xk0[2] + A[1][3] *
                          xk0[3] + A[1][4]*xk0[4] + A[1][5]*xk0[5])) / A[1][1]
        # x3
        xk1[2] = (b[2] - (A[2][0]*xk0[0] + A[2][1]*xk0[1] + A[2][3] *
                          xk0[3] + A[2][4]*xk0[4] + A[2][5]*xk0[5])) / A[2][2]
        # x4
        xk1[3] = (b[3] - (A[3][0]*xk0[0] + A[3][1]*xk0[1] + A[3][2] *
                          xk0[2] + A[3][4]*xk0[4] + A[3][5]*xk0[5])) / A[3][3]
        # x5
        xk1[4] = (b[4] - (A[4][0]*xk0[0] + A[4][1]*xk0[1] + A[4][2] *
                          xk0[2] + A[4][3]*xk0[3] + A[4][5]*xk0[5])) / A[4][4]
        # x6
        xk1[5] = (b[5] - (A[5][0]*xk0[0] + A[5][1]*xk0[1] + A[5][2] *
                          xk0[2] + A[5][3]*xk0[3] + A[5][4]*xk0[4])) / A[5][5]

        # Error Bound
        for i in range(0, len(E)):
            E[i] = xk1[i] - xk0[i]

        # Norm of Error Bound
        e = normInf(E)

        # replace xk0 by xk1
        xk0 = copy.copy(xk1)

        # print each iteration result
        # print(f"---- k = {numIteration} ----")
        # print(f"approximate x:\n{xk0}\n")

    return xk1, numIteration


def gaussSeidel(A, xk0, b, tol):
    # value of x1 ~ x6 of k+1
    xk1 = xk0[:]  # make a copy of x0
    E = [1, 1, 1, 1, 1, 1]  # E = x^(k+1) - x^k
    e = 1  # e = ||E||
    numIteration = 0
    while (e > tol):
        # count iteration times
        numIteration = numIteration + 1

        # x1
        xk1[0] = (b[0] - (A[0][1]*xk1[1] + A[0][2]*xk1[2] + A[0][3] *
                          xk1[3] + A[0][4]*xk1[4] + A[0][5]*xk1[5])) / A[0][0]
        # x2
        xk1[1] = (b[1] - (A[1][0]*xk1[0] + A[1][2]*xk1[2] + A[1][3] *
                          xk1[3] + A[1][4]*xk1[4] + A[1][5]*xk1[5])) / A[1][1]
        # x3
        xk1[2] = (b[2] - (A[2][0]*xk1[0] + A[2][1]*xk1[1] + A[2][3] *
                          xk1[3] + A[2][4]*xk1[4] + A[2][5]*xk1[5])) / A[2][2]
        # x4
        xk1[3] = (b[3] - (A[3][0]*xk1[0] + A[3][1]*xk1[1] + A[3][2] *
                          xk1[2] + A[3][4]*xk1[4] + A[3][5]*xk1[5])) / A[3][3]
        # x5
        xk1[4] = (b[4] - (A[4][0]*xk1[0] + A[4][1]*xk1[1] + A[4][2] *
                          xk1[2] + A[4][3]*xk1[3] + A[4][5]*xk1[5])) / A[4][4]
        # x6
        xk1[5] = (b[5] - (A[5][0]*xk1[0] + A[5][1]*xk1[1] + A[5][2] *
                          xk1[2] + A[5][3]*xk1[3] + A[5][4]*xk1[4])) / A[5][5]

        # Error Bound
        for i in range(0, len(E)):
            E[i] = xk1[i] - xk0[i]

        # Norm of Error Bound
        e = normInf(E)

        # replace xk0 by xk1
        xk0 = copy.copy(xk1)

        # print each iteration result
        # print(f"---- k = {numIteration} ----")
        # print(f"approximate x:\n{xk1}\n")

    return xk1, numIteration


# Jacobi Method
print("====================== Jacobi Method ========================\n")
# value of x1 ~ x6 of k
x0 = [0, 0, 0, 0, 0, 0]
k = 0

x0, k = jacobi(A, x0, b, 5e-6)

print("number of iteration:", k)
print(f"approximate x = {x0}\n")

# Gauss-Seidel Method
print("==================== Gauss-Seidel Method ====================\n")

# value of x1 ~ x6 of k
x0 = [0, 0, 0, 0, 0, 0]
k = 0

x0, k = gaussSeidel(A, x0, b, 5e-6)

print("number of iteration:", k)
print("approximate x = ", x0)
