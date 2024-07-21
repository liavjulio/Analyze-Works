"""
Liav Huli 314917808
Yehuda Harush 324023332
Tamir Refael 
Sagi Lidani 211451091
"""
# question 1:
# import numpy as np
# from scipy.linalg import lu, lu_solve, lu_factor

# # Define the matrix A
# A = np.array([
#     [1, 4, -3],
#     [-2, 1, 5],
#     [3, 2, 1]
# ])

# # Define the right-hand side vector b
# b = np.array([1, 2, 3])

# # Perform LU decomposition
# P, L, U = lu(A)

# print("L matrix:")
# print(L)

# print("\nU matrix:")
# print(U)

# # Factorize the matrix A for solving
# lu, piv = lu_factor(A)

# # Solve the system Ax = b using the LU decomposition
# x = lu_solve((lu, piv), b)

# print("\nSolution x:")
# print(x)

# question 2:


# import numpy as np

# def lu_decomposition(A):
#     """
#     Perform LU decomposition of matrix A.
#     Returns matrices L (lower triangular) and U (upper triangular).
#     """
#     n = len(A)
#     L = np.zeros((n, n))
#     U = np.zeros((n, n))

#     for i in range(n):
#         L[i][i] = 1  # Set the diagonal of L to 1
#         for j in range(i, n):
#             U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
#         for j in range(i + 1, n):
#             L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

#     return L, U

# def forward_substitution(L, b):
#     """
#     Solve the system L * y = b using forward substitution.
#     """
#     y = np.zeros_like(b)
#     for i in range(len(b)):
#         y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))
#     return y

# def backward_substitution(U, y):
#     """
#     Solve the system U * x = y using backward substitution.
#     """
#     x = np.zeros_like(y)
#     for i in range(len(y) - 1, -1, -1):
#         x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, len(y)))) / U[i][i]
#     return x

# def solve_system(A, b):
#     """
#     Solve the system of linear equations A * x = b using LU decomposition.
#     """
#     L, U = lu_decomposition(A)
#     y = forward_substitution(L, b)
#     x = backward_substitution(U, y)
#     return x

# def inverse_via_elementary_matrices(A):
#     """
#     Find the inverse of matrix A using elementary row operations.
#     """
#     n = len(A)
#     I = np.eye(n)  # Identity matrix
#     AI = np.hstack((A, I))  # Augmented matrix [A | I]

#     for i in range(n):
#         # Normalize the row to make the diagonal element 1
#         AI[i] = AI[i] / AI[i, i]

#         # Eliminate the other elements in the current column
#         for j in range(n):
#             if i != j:
#                 AI[j] = AI[j] - AI[j, i] * AI[i]

#     inv_A = AI[:, n:]  # Extract the right half as the inverse matrix
#     return inv_A

# if __name__ == "__main__":
#     # Example coefficient matrix A and vector b
#     A = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]], dtype=float)
#     b = np.array([7, 8, 9], dtype=float)

#     # Display the coefficient matrix A
#     print("Matrix A:")
#     print(A)

#     # Perform LU decomposition
#     L, U = lu_decomposition(A)
#     print("L matrix:")
#     print(L)
#     print("U matrix:")
#     print(U)

#     # Solve the system A * x = b
#     x = solve_system(A, b)
#     print("Solution vector x:")
#     print(x)

#     # Find the inverse of matrix A
#     inv_A = inverse_via_elementary_matrices(A)
#     print("Inverse of matrix A:")
#     print(inv_A)

