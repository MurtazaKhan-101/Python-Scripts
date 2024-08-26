import numpy as np
import time

st = time.time()


def generate_random_matrix(n):
    """
    Generates a random n x n matrix with entries between -10 and 10.

    Arguments:
        n: int, size of matrix

    Returns:
        numpy.ndarray, random matrix
    """
    return np.random.randint(-10, 10, size=(n, n))


def generate_random_vector(n):
    """
    Generates a random n-dimensional vector with entries between -10 and 10.

    Arguments:
        n: int, size of vector

    Returns:
        numpy.ndarray, random vector
    """
    return np.random.randint(-10, 10, size=n)


def jacobi(A, b, x0, tol=1e-10, max_iter=200):
    """
    Solves a linear system Ax = b using the Jacobi method.

    Arguments:
        A: numpy.ndarray, coefficient matrix
        b: numpy.ndarray, right-hand side vector
        x0: numpy.ndarray, initial solution
        tol: float, tolerance for convergence
        max_iter: int, maximum number of iterations

    Returns:
        x: numpy.ndarray, solution vector
        n_iter: int, number of iterations required for convergence
    """

    D = np.diag(np.diag(A))
    R = A - D
    x = x0
    n_iter = 0

    while n_iter < max_iter:
        x_new = np.linalg.solve(D, b - np.dot(R, x))
        if np.linalg.norm(x_new - x) < tol:
            break
        x = x_new
        n_iter += 1

    return x, n_iter


# Generate a random order n for the matrix A
try:
    n = np.random.randint(2, 20)
    # Generate a random n x n matrix A and a random n-dimensional vector b
    A = generate_random_matrix(n)
    b = generate_random_vector(n)

    # Set an initial solution x0 to be the zero vector
    x0 = np.zeros(n)
    # Solve the system Ax = b using the Jacobi method
    x, n_iter = jacobi(A, b, x0)

    print("A:\n", A)
    print("b:\n", b)
    print("Solution:", x)
    print("Number of iterations:", n_iter)

    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

except np.linalg.LinAlgError:
    print("Matrix is Singular")
