import numpy as np
from numpy.linalg import norm

# Check if the matrix is diagonally dominant
def is_diagonally_dominant(A):
    n = len(A)
    for i in range(n):
        row_sum = np.sum(np.abs(A[i])) - np.abs(A[i][i])
        if np.abs(A[i][i]) <= row_sum:
            return False
    return True

def gauss_seidel(A, b, X0, TOL=1e-16, N=500):
    n = len(A)
    k = 1

    if is_diagonally_dominant(A):
        print('Matrix is diagonally dominant - performing Gauss-Seidel algorithm\n')
    else:
        print('Matrix is not diagonally dominant\n')

    print("Iteration" + "\t\t\t".join([" {:>12}".format(var) for var in ["x{}".format(i) for i in range(1, len(A) + 1)]]))
    print("-----------------------------------------------------------------------------------------------")
    x = np.zeros(n, dtype=np.double)
    while k <= N:
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += A[i][j] * x[j]
            
            # Avoid division by zero or small diagonal element
            if A[i][i] == 0:
                print(f"Warning: A[{i},{i}] is zero, skipping this iteration.")
                return tuple(np.nan for _ in range(n))  # Return NaN for invalid solution

            x[i] = (b[i] - sigma) / A[i][i]

        print("{:<15} ".format(k) + "\t\t".join(["{:<15} ".format(val) for val in x]))

        if norm(x - X0, np.inf) < TOL:
            return tuple(x)

        k += 1
        X0 = x.copy()

    print("Maximum number of iterations exceeded")
    return tuple(x)


if __name__ == '__main__':
    A = np.array([[0, 1, 2], [-2, 1, 0.5], [1, -2, -0.5]])  # Example matrix with a zero diagonal element
    b = np.array([0, 4, -4])
    X0 = np.zeros_like(b)

    solution = gauss_seidel(A, b, X0)
    if np.isnan(solution[0]):
        print("Solution could not be computed due to division by zero.")
    else:
        print("\nApproximate solution:", solution)
