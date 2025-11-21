import pytest
import numpy as np
from Ex16 import TriDiagonal  # Adjust the import according to your project structure

def test_init():
    # Valid input
    tri_diagonal = TriDiagonal(3)
    assert tri_diagonal.A.shape == (3, 3)
    assert tri_diagonal.LU is not None
    
    # Invalid input: passing a string 'a' instead of an integer
    with pytest.raises(ValueError):  # Expecting ValueError here
        TriDiagonal("a")
    
    # Invalid input: passing a negative integer
    with pytest.raises(ValueError):  # Expecting ValueError here
        TriDiagonal(-3)
        
def test_rank():
    tri_diagonal = TriDiagonal(3)
    assert tri_diagonal.rank() == 3
    
    # Invalid input: passing a string 'a' instead of an integer
    with pytest.raises(ValueError):  # Expecting ValueError here
        TriDiagonal("a")
        
def test_solve():
    tri_diagonal = TriDiagonal(3)
    b = np.array([1, 2, 3])
    x = tri_diagonal.solve(b)
    assert np.allclose(tri_diagonal.A @ x, b)

def test_check():
    tri_diagonal = TriDiagonal(3)
    b = np.array([1, 2, 3])
    x = tri_diagonal.solve(b)
    assert tri_diagonal.check(b, x)

# Additional tests for larger matrices
def test_solve_10():
    tri_diagonal = TriDiagonal(10)
    x = np.random.rand(10)
    b = tri_diagonal.A @ x
    x_sol = tri_diagonal.solve(b)
    assert np.allclose(x_sol, x)

def test_solve_100():
    tri_diagonal = TriDiagonal(100)
    x = np.random.rand(100)
    b = tri_diagonal.A @ x
    x_sol = tri_diagonal.solve(b)
    assert np.allclose(x_sol, x)

def test_solve_1000():
    tri_diagonal = TriDiagonal(1000)
    x = np.random.rand(1000)
    b = tri_diagonal.A @ x
    x_sol = tri_diagonal.solve(b)
    assert np.allclose(x_sol, x)

def test_solve_3000():
    tri_diagonal = TriDiagonal(3000)
    x = np.random.rand(3000)
    b = tri_diagonal.A @ x
    x_sol = tri_diagonal.solve(b)
    assert np.allclose(x_sol, x)
