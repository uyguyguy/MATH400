import copy
import numpy as np


def gauss_elim(A, b):

    nrow = A.shape[0]
    ncol = A.shape[1]

    #    Gaussian elimination
    GE_count = 1
    for i in range(ncol-1):  # loop over columns

        aii = A[i, i]

        for j in range(i+1, nrow):  # loop over rows below column i
            m = -A[j, i] / aii  # multiplier
            A[j, i] = 0
            A[j, i+1:nrow] = A[j, i+1:nrow] + m*A[i, i+1:nrow]
            b[j] = b[j] + m*b[i]

            print(f"============Intermediate Matrix: {GE_count}============\n")
            print(f"Coefficient Matrix:\n{A}\n")
            print(f"Right-hand Side Vector:\n{b}\n")
            GE_count = GE_count+1

    #  back substitution

    x = np.zeros((nrow))  # initialize vector of zeros

    nrow = nrow - 1
    x[nrow] = b[nrow] / A[nrow, nrow]

    for i in range(nrow - 1, -1, -1):
        #dot = np.dot(x[i+1:nrow+1], A[i, i+1:nrow+1])
        dot = A[i, i+1:nrow+1] @ x[i+1:nrow+1]
        x[i] = (b[i] - dot) / A[i, i]

    return x


# -------Example-------------------------
b = np.array([[8.438], [8.888], [35.20], [26.14]])
A = np.array([[0.2115, 2.296, 2.715, 3.215], [0.4371, 3.916, 1.683, 2.852], [
             6.099, 4.324, 23.20, 1.578], [4.623, 0.8926, 15.32, 5.305]])

x = gauss_elim(A.copy(), b.copy())

print(f"Result:\n{x}\n")
