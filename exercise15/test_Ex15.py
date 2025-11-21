import Ex15
import numpy as np
import math
import pytest


def test_define_vector():
    result = Ex15.define_vector()
    expected = np.array([1.2, 3.4, 5.24, -9.38, math.exp(-1)])
    np.testing.assert_allclose(result, expected, rtol=1e-8)


def test_zero_vector():
    result = Ex15.zero_vector()
    expected = np.zeros(100)
    np.testing.assert_allclose(result, expected, rtol=1e-8)


def test_one_vector():
    result = Ex15.one_vector()
    expected = np.ones(58)
    np.testing.assert_allclose(result, expected, rtol=1e-8)


def test_add_vector_valid_input():
    A = np.array([1.2, 3.4, 5.24, -9.38, math.exp(-1)])
    B = np.ones(5)
    result = Ex15.add_vector(A, B)
    expected = np.array([2.2, 4.4, 6.24, -8.38, 1.36787944])
    np.testing.assert_allclose(result, expected, rtol=1e-8)


def test_add_vector_invalid_input():
    A = np.array([1.2, 3.4, 5.24, -9.38, math.exp(-1)])
    B = np.ones(6)
    with pytest.raises(ValueError):
        Ex15.add_vector(A, B)

def test_add_vector_invalid_input_type():
    A = np.array([1.2, 3.4, 5.24, -9.38, math.exp(-1)])
    B = [1,2,3,4,5]
    with pytest.raises(ValueError):
        Ex15.add_vector(A, B)
        
def test_minus_vector_valid_input():
    A = np.array([1.2, 3.4, 5.24, -9.38, math.exp(-1)])
    B = np.ones(5)
    result = Ex15.minus_vector(A, B)
    expected = np.array([0.2, 2.4, 4.24, -10.38, -0.63212056])
    np.testing.assert_allclose(result, expected, rtol=1e-8)

def test_minus_vector_invalid_input():
    A = np.array([1.2, 3.4, 5.24, -9.38, math.exp(-1)])
    B = np.ones(6)
    with pytest.raises(ValueError):
        Ex15.minus_vector(A, B)
        
def test_minus_vector_invalid_input_type():
    A = np.array([1.2, 3.4, 5.24, -9.38, math.exp(-1)])
    B = [1,2,3,4,5]
    with pytest.raises(ValueError):
        Ex15.minus_vector(A, B)
        
def test_slice_vector_valid_input():
    D = np.array([1.2, 3.4, 5.24, -9.38, math.exp(-1)])
    result = Ex15.slice_vector(D)
    expected = np.array([1.2, 5.24, math.exp(-1)])
    np.testing.assert_allclose(result, expected, rtol=1e-8)
    
def test_slice_vector_invalid_input():
    D = [1,2,3,4,5]
    with pytest.raises(ValueError):
        Ex15.slice_vector(D)
        
def test_is_vector_perpendicular_valid_input():
    A = np.array([1, 0, 0])
    B = np.array([0, 1, 0])
    assert Ex15.is_vector_perpendicular(A, B)
    
def test_is_vector_perpendicular_not_array():
    A = [1, 0, 0]
    B = [0, 1, 0]
    with pytest.raises(ValueError):
        Ex15.is_vector_perpendicular(A, B)
        
def test_is_vector_perpendicular_not_vector():
    A = np.array([1, 0, 0])
    B = np.array([[0, 1, 0], [1, 0, 1]])
    with pytest.raises(ValueError):
        Ex15.is_vector_perpendicular(A, B)
        
def test_is_vector_perpendicular_different_shape():
    A = np.array([1, 0, 0])
    B = np.array([0, 1, 0, 1])
    with pytest.raises(ValueError):
        Ex15.is_vector_perpendicular(A, B)
        
def test_is_vector_perpendicular_zero_vector():
    A = np.array([0, 0, 0])
    B = np.array([1, 0, 0])
    with pytest.raises(ValueError):
        Ex15.is_vector_perpendicular(A, B)
        
def test_define_matrix():
    result = Ex15.define_matrix()
    expected = np.array([[6, 7, 8, 9], [1.2, 2.3, 3.4, 4.5], [math.sin(math.pi/6), math.cos(math.pi/4), math.log(10), math.exp(2)]])
    np.testing.assert_allclose(result, expected, rtol=1e-8)
    
def test_zero_matrix():
    result = Ex15.zero_matrix()
    expected = np.zeros((100, 200))
    np.testing.assert_allclose(result, expected, rtol=1e-8)
    
def test_one_matrix():
    result = Ex15.one_matrix()
    expected = np.ones((58, 58))
    np.testing.assert_allclose(result, expected, rtol=1e-8)
    
def test_identity_matrix_valid_input():
    n = 3
    result = Ex15.identity_matrix(n)
    expected = np.eye(n)
    np.testing.assert_allclose(result, expected, rtol=1e-8)
    
def test_identity_matrix_invalid_input():
    n = 1000
    with pytest.raises(ValueError):
        Ex15.identity_matrix(n)
        
def test_identity_matrix_invalid_input_type():
    n = "3"
    with pytest.raises(ValueError):
        Ex15.identity_matrix(n)
        
        
def test_add_matrix_valid_input():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[1, 2, 3], [4, 5, 6]])
    result = Ex15.add_matrix(A, B)
    expected = np.array([[2, 4, 6], [8, 10, 12]])
    np.testing.assert_allclose(result, expected, rtol=1e-8)
    
def test_add_matrix_invalid_input():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    with pytest.raises(ValueError):
        Ex15.add_matrix(A, B)
        
def test_add_matrix_invalid_input_type():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = [1, 2, 3, 4, 5, 6]
    with pytest.raises(ValueError):
        Ex15.add_matrix(A, B)
        
def test_minus_matrix_valid_input():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[1, 2, 3], [4, 5, 6]])
    result = Ex15.minus_matrix(A, B)
    expected = np.array([[0, 0, 0], [0, 0, 0]])
    np.testing.assert_allclose(result, expected, rtol=1e-8)
    
def test_minus_matrix_invalid_input():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    with pytest.raises(ValueError):
        Ex15.minus_matrix(A, B)
        
def test_minus_matrix_invalid_input_type():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = [1, 2, 3, 4, 5, 6]
    with pytest.raises(ValueError):
        Ex15.minus_matrix(A, B)
        
def test_minus_matrix_not_matrix():
    A = np.array([1, 2, 3])
    B = np.array([1, 2, 3])
    with pytest.raises(ValueError):
        Ex15.minus_matrix(A, B)
        
def test_minus_matrix_different_shape():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    with pytest.raises(ValueError):
        Ex15.minus_matrix(A, B)
        
def test_mul_matrix_valid_input():
    # A is 2x3 matrix
    # B is 3x4 matrix
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    result = Ex15.mul_matrix(A, B)
    expected = np.array([[38, 44, 50, 56], [83, 98, 113, 128]])
    np.testing.assert_allclose(result, expected, rtol=1e-8)
    
def test_mul_matrix_invalid_input():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    with pytest.raises(ValueError):
        Ex15.mul_matrix(A, B)
        
def test_mul_matrix_invalid_input_type():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = [1, 2, 3, 4, 5, 6]
    with pytest.raises(ValueError):
        Ex15.mul_matrix(A, B)
        
def test_mul_matrix_not_matrix():
    A = np.array([1, 2, 3])
    B = np.array([1, 2, 3])
    with pytest.raises(ValueError):
        Ex15.mul_matrix(A, B)
        