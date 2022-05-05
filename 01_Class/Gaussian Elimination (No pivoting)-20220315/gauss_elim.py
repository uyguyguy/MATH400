import copy
import numpy as np

"""
%GAUSS_ELIM   solve the linear system Ax = b using Gaussian elimination
%             with back substitution
%             
%     calling sequences:
%             x = gauss_elim ( A, b )
%             gauss_elim ( A, b )
%
%     inputs:
%             A       coefficient matrix for linear system
%                     (matrix must be square)
%             b       right-hand side vector
%
%     output:
%             x       solution vector (i.e., vector for which Ax = b)
%

%
"""


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
b = np.array([[8.438], [8.888], [35.20]])
A = np.array([[4, -1, -1], [-1, 4, -1], [-1, -1, 4]])

x = gauss_elim(A.copy(), b.copy())

print(f"Result:\n{x}\n")
