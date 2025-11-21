from Assignment5 import fluid_analysis
import numpy as np
import pytest

M = np.diag([1000.0, 1200.0, 2000.0, 1500.0, 850.0, 998.0])
G = np.array([[2.0, -1.0, 0.0],
              [-1.0, 1.5, 0.5],
              [0.0, 0.5, 3.2],
              [0.0, -2.2, 0.16],
              [1.5, 0.0, 0.16],
              [-0.16, 0.0, 0.3]])
rp = np.array([0.03, 0.4, 0.13])
vstar = np.array([-0.4, -0.3, -0.02, 0.001, -1.1, 0.25])


def test_pressure_vector():
    p, v, lam, x = fluid_analysis(M, G, rp, vstar)
    assert np.allclose(p, np.array([421.16792282, 287.79313103, 32.7671688]))


def test_corrector_velocity_vector():
    p, v, lam, x = fluid_analysis(M, G, rp, vstar)
    assert np.allclose(v, np.array(
        [0.15454271, -0.27757887,  0.10437575, -0.41760143, -0.35059455,  0.19232794]))


def test_eigenvalues():
    p, v, lam, x = fluid_analysis(M, G, rp, vstar)
    assert np.allclose(lam, np.array([2.00000524e+03, 1.50000324e+03,
                                      1.20000292e+03, 8.50002677e+02,
                                      1.00000500e+03, 9.98000116e+02,
                                      -1.03467091e-02, -5.60463897e-03,
                                      -3.24693417e-03]))


def test_eigenvectors():
    p, v, lam, x = fluid_analysis(M, G, rp, vstar)
    x_expected = np.array(
        [[2.50001290e-07, -2.93335729e-06, -1.45833282e-05, -2.35286642e-05,
          9.99997487e-01, 1.59928371e-04, 2.13122393e-03, 5.70250068e-04,
          3.64077819e-04],
         [-1.46873943e-06, 7.15552939e-06, 9.99998785e-01, 4.77279229e-06,
          1.75003125e-05, -1.53492576e-06, -1.49888511e-03, 2.79961860e-04,
          3.24745599e-04],
         [-9.99998689e-01, -7.84015854e-07, -2.44789151e-06, -5.23803326e-07,
          5.00092769e-07, -9.59909524e-07, -4.54896115e-04, 1.50626650e-03,
          -3.83023727e-04],
            [5.87999630e-07, -9.99998919e-01, 8.94446309e-06, -4.62135927e-08,
             -4.39984054e-06, -9.65214266e-08, 9.20446761e-04, -1.41537260e-04,
             -1.13807132e-03],
            [-2.22605745e-07, -2.62761029e-08, -3.38103738e-06, 9.99998425e-01,
             1.99995261e-05, -1.29665611e-06, 1.28026408e-03, 8.19496165e-04,
             9.15909202e-04],
            [-4.79037784e-07, -6.37412118e-08,  1.27886938e-06, 1.52618351e-06,
             -1.59608075e-04, 9.99999929e-01, -1.74817256e-04, 2.16541989e-04,
             -1.96495310e-04],
            [8.55737576e-10, -8.70095366e-09, -8.33358997e-04, 1.76463628e-03,
             2.00002301e-03, -1.60000525e-04, -7.45135458e-01, -3.66684780e-01,
             -5.57052590e-01],
            [-2.50000890e-04, 1.46667076e-03, 1.24999018e-03, 3.59147352e-08,
             -9.99956307e-04, -1.62823996e-07, 6.40975062e-01, -1.63116295e-01,
             -7.50026179e-01],
            [-1.59999412e-03, -1.06665624e-04, 4.16659681e-04, 1.88235770e-04,
             -3.50358445e-08, 3.00597076e-04, 1.84159189e-01, -9.15932277e-01,
             3.56581809e-01]])
    assert np.allclose(x, x_expected)


def test_invalid_input_M():
    with pytest.raises(RuntimeError):
        fluid_analysis(np.array([[1, 2], [3, 4], [5, 6]]), G, rp, vstar)


def test_invalid_input_G():
    with pytest.raises(RuntimeError):
        fluid_analysis(M, np.zeros((6, 4)), rp, vstar)


def test_invalid_input_rp():
    with pytest.raises(RuntimeError):
        fluid_analysis(M, G, np.zeros(4), vstar)


def test_invalid_input_vstar():
    with pytest.raises(RuntimeError):
        fluid_analysis(M, G, rp, np.zeros(8))


def test_invalid_input_M_not_diagonal():
    with pytest.raises(RuntimeError):
        fluid_analysis(np.ones((6, 6)), G, rp, vstar)