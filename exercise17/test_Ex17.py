from Ex17 import EigenvalueAnalysis
import numpy as np
import pytest


def test_valid_input_A():
    A = np.array([[4, 2], [2, 4]])
    eigenvalue_analysis = EigenvalueAnalysis(A)
    print(eigenvalue_analysis.lam)
    print(eigenvalue_analysis.x)
    assert np.allclose(eigenvalue_analysis.lam, np.array([2, 6]))
    assert np.allclose(eigenvalue_analysis.x, np.array(
        [[0.70710678, -0.70710678], [0.70710678, 0.70710678]]))


def test_invalid_input_A():
    A = [1, 2, 3]
    with pytest.raises(RuntimeError):
        EigenvalueAnalysis(A)


def test_invalid_input_A_not_square():
    A = np.array([[4, 2], [2, 4], [3, 3]])
    with pytest.raises(RuntimeError):
        EigenvalueAnalysis(A)


def test_invalid_input_A_3D_array():
    A = np.array([[[4, 2], [2, 4]], [[3, 3], [3, 3]]])
    with pytest.raises(RuntimeError):
        EigenvalueAnalysis(A)


def test_check_with_valid_A():
    A = np.array([[4, 2], [2, 4]])
    eigenvalue_analysis = EigenvalueAnalysis(A)
    assert eigenvalue_analysis.check(2, np.array([0.70710678, -0.70710678]))
    assert eigenvalue_analysis.check(6, np.array([0.70710678, 0.70710678]))


def test_check_with_incorrect_lam_i():
    A = np.array([[4, 2], [2, 4]])
    eigenvalue_analysis = EigenvalueAnalysis(A)
    assert not eigenvalue_analysis.check(
        1, np.array([0.70710678, -0.70710678]))
    assert not eigenvalue_analysis.check(
        7, np.array([0.70710678, -0.70710678]))


def test_check_with_incorrect_x_i():
    A = np.array([[4, 2], [2, 4]])
    eigenvalue_analysis = EigenvalueAnalysis(A)
    assert not eigenvalue_analysis.check(2, np.array([1, 2]))
    assert not eigenvalue_analysis.check(6, np.array([1, 2]))


def test_check_with_different_size_x_i():
    A = np.array([[4, 2], [2, 4]])
    eigenvalue_analysis = EigenvalueAnalysis(A)
    with pytest.raises(RuntimeError):
        eigenvalue_analysis.check(2, np.array([1, 2, 3]))
    with pytest.raises(RuntimeError):
        eigenvalue_analysis.check(6, np.array([1, 2, 3]))


def test_check_with_valid_B():
    A = np.array([[4, 2], [2, 4]])
    B = np.array([[1, 0], [0, 1]])
    eigenvalue_analysis = EigenvalueAnalysis(A, B)
    assert eigenvalue_analysis.check(2, np.array([0.70710678, -0.70710678]))
    assert eigenvalue_analysis.check(6, np.array([0.70710678, 0.70710678]))


def test_invalid_input_B_not_square():
    A = np.array([[4, 2], [2, 4]])
    B = np.array([[1, 0], [0, 1], [1, 1]])
    with pytest.raises(RuntimeError):
        EigenvalueAnalysis(A, B)


def test_check_with_valid_A_another():
    A = np.array([[3, 1], [1, 3]])
    eigenvalue_analysis = EigenvalueAnalysis(A)
    # Known eigenpairs:
    # Eigenvalues: 2, 4
    # Eigenvectors: [0.70710678, -0.70710678] and [0.70710678, 0.70710678]
    assert eigenvalue_analysis.check(2, np.array([0.70710678, -0.70710678]))
    assert eigenvalue_analysis.check(4, np.array([0.70710678, 0.70710678]))


def test_lam_sorted():
    A = np.array([[3, 1], [1, 3]])
    eigenvalue_analysis = EigenvalueAnalysis(A)
    assert np.allclose(eigenvalue_analysis.lam, np.array([2, 4]))

def test_check_with_valid_B_another():
    A = np.array([[3, 1], [1, 3]])
    B = np.array([[1, 0], [0, 1]])
    eigenvalue_analysis = EigenvalueAnalysis(A, B)
    assert eigenvalue_analysis.check(2, np.array([0.70710678, -0.70710678]))
    assert eigenvalue_analysis.check(4, np.array([0.70710678, 0.70710678]))