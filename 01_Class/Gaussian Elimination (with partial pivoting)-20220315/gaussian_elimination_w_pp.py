import copy
import numpy as np

"""
%GAUSS_ELIM   solve the linear system Ax = b using Gaussian elimination
%             with back substitution
%             This version has partial pivoting
%     calling sequences:
%             x = part_piv_ge_1 ( A, b )
%             part_piv_ge_1 ( A, b )
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


def part_piv_ge(A, b):

    nrow = A.shape[0]
    ncol = A.shape[1]
    GE_count = 1

    #    Gaussian elimination

    for i in range(ncol-1):  # loop over columns
        col_i = abs(A[i:nrow, i])  # isolate column i
        pivot = max(col_i)
        t, = np.where(col_i == pivot)[0]  # find pivot i and its index
        t = t + i

        # interchanging i^th row with pivot row
        temp = A[i, :].copy()
        tb = b[i].copy()
        A[i, :] = A[t, :]
        b[i] = b[t]
        A[t, :] = temp
        b[t] = tb

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

x = part_piv_ge(A.copy(), b.copy())

print(f"Result:\n{x}\n")
