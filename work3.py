import numpy as np

def is_diagonally_dominant(a):
    n = len(a)
    for i in range(n):
        sum_row = sum(abs(a[i][j]) for j in range(n) if j != i)
        if abs(a[i][i]) <= sum_row:
            return False
    return True

def jacobi(a, b, tolerance=0.001, max_iterations=1000):
    n = len(a)
    x = np.zeros(n)
    new_x = np.zeros(n)
    
    if not is_diagonally_dominant(a):
        return "Matrix is not diagonally dominant"
    
    for _ in range(max_iterations):
        for i in range(n):
            s = sum(a[i][j] * x[j] for j in range(n) if j != i)
            new_x[i] = (b[i] - s) / a[i][i]
        
        if np.allclose(x, new_x, atol=tolerance):
            return new_x
        
        x = np.copy(new_x)
    
    return new_x

def gauss_seidel(a, b, tolerance=0.001, max_iterations=1000):
    n = len(a)
    x = np.zeros(n)
    
    if not is_diagonally_dominant(a):
        return "Matrix is not diagonally dominant"
    
    for _ in range(max_iterations):
        x_old = np.copy(x)
        for i in range(n):
            s = sum(a[i][j] * x[j] for j in range(i)) + sum(a[i][j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - s) / a[i][i]
        
        if np.allclose(x, x_old, atol=tolerance):
            return x
    
    return x

def main():
    A = np.array([
        [4, 1, 2],
        [3, 5, 1],
        [1, 1, 3]
    ])
    b = np.array([4, 7, 3])
    
    print("Jacobi Method Solution:")
    jacobi_solution = jacobi(A, b)
    print(jacobi_solution)
    
    print("\nGauss-Seidel Method Solution:")
    gauss_seidel_solution = gauss_seidel(A, b)
    print(gauss_seidel_solution)

if __name__ == "__main__":
    main()
