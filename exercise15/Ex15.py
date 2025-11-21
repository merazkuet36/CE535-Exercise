import numpy as np
import math

# 1. Define a Vector
def define_vector():
    return np.array([1.2, 3.4, 5.24, -9.38, math.exp(-1)])

# 2. Zero Vector
def zero_vector():
    return np.zeros(100)

# 3. One Vector
def one_vector():
    return np.ones(58)

# 4. Vector Addition
def add_vector(A, B):
    if isinstance(A, np.ndarray) and isinstance(B, np.ndarray):
        if A.shape == B.shape and A.ndim == 1:  
            return A + B
        else:
            raise ValueError("Vectors must have the same dimensions")
    else:
        raise ValueError("e1")

# 5. Vector Subtraction
def minus_vector(A, B):
    if isinstance(A, np.ndarray) and isinstance(B, np.ndarray):
        if A.shape == B.shape and A.ndim == 1: 
            return A - B
        else:
            raise ValueError("Vectors must have the same dimensions and be 1D")
    else:
        raise ValueError("Both inputs must be numpy arrays")

# 6. Slicing a Vector
def slice_vector(D):
    if isinstance(D, np.ndarray) and D.ndim == 1:
        return D[::2]  
    else:
        raise ValueError("Input must be a 1D numpy array")

# 7. Perpendicular Check
def is_vector_perpendicular(A, B):
    if isinstance(A, np.ndarray) and isinstance(B, np.ndarray):
        if A.shape == B.shape and A.ndim == 1:  
            if np.all(A == 0) or np.all(B == 0): 
                raise ValueError("Perpendicular check is invalid for zero vectors")
            dot_product = np.dot(A, B)
            if np.abs(dot_product) < 1e-10:  
                return True
            else:
                return False
        else:
            raise ValueError("Vectors must have the same dimensions and be 1D")
    else:
        raise ValueError("Both inputs must be numpy arrays")


# 8. Define Matrix
def define_matrix():
    return np.array([[6, 7, 8, 9], 
                     [1.2, 2.3, 3.4, 4.5], 
                     [math.sin(math.pi / 6), math.cos(math.pi / 4), math.log(10), math.exp(2)]])

# 9. Zero Matrix
def zero_matrix():
    return np.zeros((100, 200))

# 10. One Matrix
def one_matrix():
    return np.ones((58, 58))

# 11. Identity Matrix
def identity_matrix(n):
    if isinstance(n, int) and n > 0 and n < 1000:
        return np.eye(n)
    else:
        raise ValueError("n must be an integer greater than 0 and less than 1000")

# 12. Matrix Addition
def add_matrix(A, B):
    if isinstance(A, np.ndarray) and isinstance(B, np.ndarray):
        if A.ndim == 2 and B.ndim == 2:  # Check if both are 2D matrices
            if A.shape == B.shape:  # Check if matrices have the same dimensions
                return A + B
            else:
                raise ValueError("Matrices must have the same dimensions")
        else:
            raise ValueError("Both inputs must be 2D matrices")
    else:
        raise ValueError("Both inputs must be numpy arrays")

# 13. Matrix Subtraction
def minus_matrix(A, B):
    if isinstance(A, np.ndarray) and isinstance(B, np.ndarray):
        if A.ndim == 2 and B.ndim == 2:  # Check if both are 2D matrices
            if A.shape == B.shape:  # Check if matrices have the same dimensions
                return A - B
            else:
                raise ValueError("Matrices must have the same dimensions")
        else:
            raise ValueError("Both inputs must be 2D matrices")
    else:
        raise ValueError("Both inputs must be numpy arrays")

# 14. Matrix Multiplication
def mul_matrix(A, B):
    if isinstance(A, np.ndarray) and isinstance(B, np.ndarray):
        if A.ndim == 2 and B.ndim == 2:  # Check if both are 2D matrices
            if A.shape[1] == B.shape[0]:  # Columns of A must match rows of B
                return np.dot(A, B)  # Matrix multiplication
            else:
                raise ValueError("Matrix dimensions must be compatible for multiplication")
        else:
            raise ValueError("Both inputs must be 2D matrices")
    else:
        raise ValueError("Both inputs must be numpy arrays")
