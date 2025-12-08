from Ex23 import NewtonRaphson
import numpy as np

def test_NewtonRaphson():
    R = lambda X: np.array(
        [X[0]**2 + 2*X[1]**3 + X[0] + 3*X[1] - 7.0, 
         4*X[0]**2 + X[1]**3 + 3*X[0] + 2*X[1] - 10.0])
    K = lambda X: np.array([[2*X[0]+1, 6*X[1]**2 + 3], 
                            [8*X[0]+3, 3*X[1]**2 + 2]])
    X0 = np.array([0.0, 0.0])
    max_iter = 100
    tol = 1e-6
    X, iter, norm = NewtonRaphson(R, K, X0, max_iter, tol)
    assert abs(norm) < tol

def test_NewtonRaphson_3x3_system1():
    """Test with a 3x3 system: x^2 + y^2 = 2, y^2 + z^2 = 3, z^2 + x^2 = 4"""
    R = lambda X: np.array([
        X[0]**2 + X[1]**2 - 2.0,
        X[1]**2 + X[2]**2 - 3.0,
        X[2]**2 + X[0]**2 - 4.0
    ])
    K = lambda X: np.array([
        [2*X[0], 2*X[1], 0.0],
        [0.0, 2*X[1], 2*X[2]],
        [2*X[0], 0.0, 2*X[2]]
    ])
    X0 = np.array([1.0, 1.0, 1.0])
    max_iter = 100
    tol = 1e-6
    X, iter, norm = NewtonRaphson(R, K, X0, max_iter, tol)
    assert abs(norm) < tol

def test_NewtonRaphson_3x3_system2():
    """Test with a 3x3 system: x^2 + y = 5, y^2 + z = 7, z^2 + x = 6"""
    R = lambda X: np.array([
        X[0]**2 + X[1] - 5.0,
        X[1]**2 + X[2] - 7.0,
        X[2]**2 + X[0] - 6.0
    ])
    K = lambda X: np.array([
        [2*X[0], 1.0, 0.0],
        [0.0, 2*X[1], 1.0],
        [1.0, 0.0, 2*X[2]]
    ])
    X0 = np.array([1.0, 1.0, 1.0])
    max_iter = 100
    tol = 1e-6
    X, iter, norm = NewtonRaphson(R, K, X0, max_iter, tol)
    assert abs(norm) < tol

def test_NewtonRaphson_3x3_system3():
    """Test with a 3x3 system: x^3 + y^2 = 2, y^3 + z^2 = 3, z^3 + x^2 = 4"""
    R = lambda X: np.array([
        X[0]**3 + X[1]**2 - 2.0,
        X[1]**3 + X[2]**2 - 3.0,
        X[2]**3 + X[0]**2 - 4.0
    ])
    K = lambda X: np.array([
        [3*X[0]**2, 2*X[1], 0.0],
        [0.0, 3*X[1]**2, 2*X[2]],
        [2*X[0], 0.0, 3*X[2]**2]
    ])
    X0 = np.array([1.0, 1.0, 1.0])
    max_iter = 100
    tol = 1e-6
    X, iter, norm = NewtonRaphson(R, K, X0, max_iter, tol)
    assert abs(norm) < tol

def test_NewtonRaphson_3x3_system4():
    """Test with a 3x3 system: x*y + z = 3, y*z + 2*x = 4, z*x + 3*y = 5"""
    R = lambda X: np.array([
        X[0]*X[1] + X[2] - 3.0,
        X[1]*X[2] + 2*X[0] - 4.0,
        X[2]*X[0] + 3*X[1] - 5.0
    ])
    K = lambda X: np.array([
        [X[1], X[0], 1.0],
        [2.0, X[2], X[1]],
        [X[2], 3.0, X[0]]
    ])
    X0 = np.array([1.0, 1.0, 1.0])
    max_iter = 100
    tol = 1e-6
    X, iter, norm = NewtonRaphson(R, K, X0, max_iter, tol)
    assert abs(norm) < tol

def test_NewtonRaphson_3x3_system5():
    """Test with a 3x3 system: exp(x) + y^2 = 2, exp(y) + z^2 = 3, exp(z) + x^2 = 4"""
    R = lambda X: np.array([
        np.exp(X[0]) + X[1]**2 - 2.0,
        np.exp(X[1]) + X[2]**2 - 3.0,
        np.exp(X[2]) + X[0]**2 - 4.0
    ])
    K = lambda X: np.array([
        [np.exp(X[0]), 2*X[1], 0.0],
        [0.0, np.exp(X[1]), 2*X[2]],
        [2*X[0], 0.0, np.exp(X[2])]
    ])
    X0 = np.array([0.0, 0.0, 0.0])
    max_iter = 100
    tol = 1e-6
    X, iter, norm = NewtonRaphson(R, K, X0, max_iter, tol)
    assert abs(norm) < tol

def test_NewtonRaphson_3x3_system6():
    """Test with a 3x3 system: x^2 + y^3 + z = 6, x + y^2 + z^3 = 8, x^3 + y + z^2 = 10"""
    R = lambda X: np.array([
        X[0]**2 + X[1]**3 + X[2] - 6.0,
        X[0] + X[1]**2 + X[2]**3 - 8.0,
        X[0]**3 + X[1] + X[2]**2 - 10.0
    ])
    K = lambda X: np.array([
        [2*X[0], 3*X[1]**2, 1.0],
        [1.0, 2*X[1], 3*X[2]**2],
        [3*X[0]**2, 1.0, 2*X[2]]
    ])
    X0 = np.array([1.0, 1.0, 1.0])
    max_iter = 100
    tol = 1e-6
    X, iter, norm = NewtonRaphson(R, K, X0, max_iter, tol)
    assert abs(norm) < tol

def test_NewtonRaphson_10x10_sin_cos():
    """Test with a 10x10 system using sin and cos functions"""
    R = lambda X: np.array([
        np.sin(X[0]) + X[1]**2 + X[2] - 1.5,
        np.cos(X[1]) + X[2]**2 + X[3] - 1.5,
        np.sin(X[2]) + X[3]**2 + X[4] - 1.5,
        np.cos(X[3]) + X[4]**2 + X[5] - 1.5,
        np.sin(X[4]) + X[5]**2 + X[6] - 1.5,
        np.cos(X[5]) + X[6]**2 + X[7] - 1.5,
        np.sin(X[6]) + X[7]**2 + X[8] - 1.5,
        np.cos(X[7]) + X[8]**2 + X[9] - 1.5,
        np.sin(X[8]) + X[9]**2 + X[0] - 1.5,
        np.cos(X[9]) + X[0]**2 + X[1] - 1.5
    ])
    K = lambda X: np.array([
        [np.cos(X[0]), 2*X[1], 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, -np.sin(X[1]), 2*X[2], 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, np.cos(X[2]), 2*X[3], 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, -np.sin(X[3]), 2*X[4], 1.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, np.cos(X[4]), 2*X[5], 1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, -np.sin(X[5]), 2*X[6], 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, np.cos(X[6]), 2*X[7], 1.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -np.sin(X[7]), 2*X[8], 1.0],
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, np.cos(X[8]), 2*X[9]],
        [2*X[0], 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -np.sin(X[9])]
    ])
    X0 = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
    max_iter = 200
    tol = 1e-6
    X, iter, norm = NewtonRaphson(R, K, X0, max_iter, tol)
    assert abs(norm) < tol

def test_NewtonRaphson_10x10_exp_log():
    """Test with a 10x10 system using exp and log functions"""
    R = lambda X: np.array([
        np.exp(X[0]) + np.log(X[1] + 2.0) - 2.0,
        np.exp(X[1]) + np.log(X[2] + 2.0) - 2.0,
        np.exp(X[2]) + np.log(X[3] + 2.0) - 2.0,
        np.exp(X[3]) + np.log(X[4] + 2.0) - 2.0,
        np.exp(X[4]) + np.log(X[5] + 2.0) - 2.0,
        np.exp(X[5]) + np.log(X[6] + 2.0) - 2.0,
        np.exp(X[6]) + np.log(X[7] + 2.0) - 2.0,
        np.exp(X[7]) + np.log(X[8] + 2.0) - 2.0,
        np.exp(X[8]) + np.log(X[9] + 2.0) - 2.0,
        np.exp(X[9]) + np.log(X[0] + 2.0) - 2.0
    ])
    K = lambda X: np.array([
        [np.exp(X[0]), 1.0/(X[1] + 2.0), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, np.exp(X[1]), 1.0/(X[2] + 2.0), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, np.exp(X[2]), 1.0/(X[3] + 2.0), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, np.exp(X[3]), 1.0/(X[4] + 2.0), 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, np.exp(X[4]), 1.0/(X[5] + 2.0), 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, np.exp(X[5]), 1.0/(X[6] + 2.0), 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, np.exp(X[6]), 1.0/(X[7] + 2.0), 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, np.exp(X[7]), 1.0/(X[8] + 2.0), 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, np.exp(X[8]), 1.0/(X[9] + 2.0)],
        [1.0/(X[0] + 2.0), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, np.exp(X[9])]
    ])
    X0 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    max_iter = 200
    tol = 1e-6
    X, iter, norm = NewtonRaphson(R, K, X0, max_iter, tol)
    assert abs(norm) < tol

def test_NewtonRaphson_10x10_abs():
    """Test with a 10x10 system using abs function"""
    def sign_safe(x):
        return np.sign(x) if x != 0 else 1.0
    
    R = lambda X: np.array([
        np.abs(X[0]) + X[1]**2 + X[2] - 1.5,
        np.abs(X[1]) + X[2]**2 + X[3] - 1.5,
        np.abs(X[2]) + X[3]**2 + X[4] - 1.5,
        np.abs(X[3]) + X[4]**2 + X[5] - 1.5,
        np.abs(X[4]) + X[5]**2 + X[6] - 1.5,
        np.abs(X[5]) + X[6]**2 + X[7] - 1.5,
        np.abs(X[6]) + X[7]**2 + X[8] - 1.5,
        np.abs(X[7]) + X[8]**2 + X[9] - 1.5,
        np.abs(X[8]) + X[9]**2 + X[0] - 1.5,
        np.abs(X[9]) + X[0]**2 + X[1] - 1.5
    ])
    K = lambda X: np.array([
        [sign_safe(X[0]), 2*X[1], 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, sign_safe(X[1]), 2*X[2], 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, sign_safe(X[2]), 2*X[3], 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, sign_safe(X[3]), 2*X[4], 1.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, sign_safe(X[4]), 2*X[5], 1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, sign_safe(X[5]), 2*X[6], 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, sign_safe(X[6]), 2*X[7], 1.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, sign_safe(X[7]), 2*X[8], 1.0],
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, sign_safe(X[8]), 2*X[9]],
        [2*X[0], 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, sign_safe(X[9])]
    ])
    X0 = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
    max_iter = 200
    tol = 1e-6
    X, iter, norm = NewtonRaphson(R, K, X0, max_iter, tol)
    assert abs(norm) < tol

def test_NewtonRaphson_10x10_mixed_functions():
    """Test with a 10x10 system mixing sin, cos, exp, log, abs, and polynomials"""
    def sign_safe(x):
        return np.sign(x) if x != 0 else 1.0
    
    R = lambda X: np.array([
        np.sin(X[0]) + np.exp(X[1]) + X[2] - 2.5,
        np.cos(X[1]) + np.log(X[2] + 2.0) + X[3] - 1.5,
        np.exp(X[2]) + np.abs(X[3]) + X[4] - 2.5,
        np.log(X[3] + 2.0) + X[4]**2 + X[5] - 1.5,
        np.abs(X[4]) + np.sin(X[5]) + X[6] - 1.5,
        np.cos(X[5]) + np.exp(X[6]) + X[7] - 2.5,
        np.sin(X[6]) + np.log(X[7] + 2.0) + X[8] - 1.5,
        np.exp(X[7]) + np.abs(X[8]) + X[9] - 2.5,
        np.log(X[8] + 2.0) + np.cos(X[9]) + X[0] - 1.5,
        np.abs(X[9]) + X[0]**2 + X[1] - 1.5
    ])
    K = lambda X: np.array([
        [np.cos(X[0]), np.exp(X[1]), 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, -np.sin(X[1]), 1.0/(X[2] + 2.0), 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, np.exp(X[2]), sign_safe(X[3]), 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0/(X[3] + 2.0), 2*X[4], 1.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, sign_safe(X[4]), np.cos(X[5]), 1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, -np.sin(X[5]), np.exp(X[6]), 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, np.cos(X[6]), 1.0/(X[7] + 2.0), 1.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, np.exp(X[7]), sign_safe(X[8]), 1.0],
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0/(X[8] + 2.0), -np.sin(X[9])],
        [2*X[0], 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, sign_safe(X[9])]
    ])
    X0 = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
    max_iter = 200
    tol = 1e-6
    X, iter, norm = NewtonRaphson(R, K, X0, max_iter, tol)
    assert abs(norm) < tol

def test_NewtonRaphson_10x10_tanh_sqrt():
    """Test with a 10x10 system using tanh and sqrt functions"""
    R = lambda X: np.array([
        np.tanh(X[0]) + np.sqrt(X[1] + 1.0) - 1.0,
        np.tanh(X[1]) + np.sqrt(X[2] + 1.0) - 1.0,
        np.tanh(X[2]) + np.sqrt(X[3] + 1.0) - 1.0,
        np.tanh(X[3]) + np.sqrt(X[4] + 1.0) - 1.0,
        np.tanh(X[4]) + np.sqrt(X[5] + 1.0) - 1.0,
        np.tanh(X[5]) + np.sqrt(X[6] + 1.0) - 1.0,
        np.tanh(X[6]) + np.sqrt(X[7] + 1.0) - 1.0,
        np.tanh(X[7]) + np.sqrt(X[8] + 1.0) - 1.0,
        np.tanh(X[8]) + np.sqrt(X[9] + 1.0) - 1.0,
        np.tanh(X[9]) + np.sqrt(X[0] + 1.0) - 1.0
    ])
    K = lambda X: np.array([
        [1.0 - np.tanh(X[0])**2, 0.5/np.sqrt(X[1] + 1.0), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 1.0 - np.tanh(X[1])**2, 0.5/np.sqrt(X[2] + 1.0), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0 - np.tanh(X[2])**2, 0.5/np.sqrt(X[3] + 1.0), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0 - np.tanh(X[3])**2, 0.5/np.sqrt(X[4] + 1.0), 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 1.0 - np.tanh(X[4])**2, 0.5/np.sqrt(X[5] + 1.0), 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0 - np.tanh(X[5])**2, 0.5/np.sqrt(X[6] + 1.0), 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0 - np.tanh(X[6])**2, 0.5/np.sqrt(X[7] + 1.0), 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0 - np.tanh(X[7])**2, 0.5/np.sqrt(X[8] + 1.0), 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0 - np.tanh(X[8])**2, 0.5/np.sqrt(X[9] + 1.0)],
        [0.5/np.sqrt(X[0] + 1.0), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0 - np.tanh(X[9])**2]
    ])
    X0 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    max_iter = 200
    tol = 1e-6
    X, iter, norm = NewtonRaphson(R, K, X0, max_iter, tol)
    assert abs(norm) < tol

def test_NewtonRaphson_10x10_complex_mix():
    """Test with a 10x10 system using a complex mix of all functions"""
    def sign_safe(x):
        return np.sign(x) if x != 0 else 1.0
    
    R = lambda X: np.array([
        np.sin(X[0]) + np.tanh(X[1]) + X[2]**2 + X[3] - 2.0,
        np.cos(X[1]) + np.log(np.abs(X[2]) + 2.0) + np.abs(X[3]) + X[4] - 2.0,
        np.tanh(X[2]) + np.sqrt(np.abs(X[3]) + 1.0) + np.sin(X[4]) + X[5] - 2.0,
        np.log(np.abs(X[3]) + 2.0) + np.cos(X[4]) + X[5]**2 + X[6] - 2.0,
        np.abs(X[4]) + np.tanh(X[5]) + np.sin(X[6]) + X[7] - 2.0,
        np.cos(X[5]) + np.log(np.abs(X[6]) + 2.0) + np.sqrt(np.abs(X[7]) + 1.0) + X[8] - 2.0,
        np.sin(X[6]) + np.abs(X[7]) + np.tanh(X[8]) + X[9] - 2.0,
        np.cos(X[7]) + np.tanh(X[8]) + X[9]**2 + X[0] - 2.0,
        np.sqrt(np.abs(X[8]) + 1.0) + np.sin(X[9]) + np.log(np.abs(X[0]) + 2.0) + X[1] - 2.0,
        np.abs(X[9]) + np.cos(X[0]) + np.tanh(X[1]) + X[2] - 2.0
    ])
    K = lambda X: np.array([
        [np.cos(X[0]), 1.0 - np.tanh(X[1])**2, 2*X[2], 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, -np.sin(X[1]), sign_safe(X[2])/(np.abs(X[2]) + 2.0), sign_safe(X[3]), 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0 - np.tanh(X[2])**2, 0.5*sign_safe(X[3])/np.sqrt(np.abs(X[3]) + 1.0), np.cos(X[4]), 1.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, sign_safe(X[3])/(np.abs(X[3]) + 2.0), -np.sin(X[4]), 2*X[5], 1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, sign_safe(X[4]), 1.0 - np.tanh(X[5])**2, np.cos(X[6]), 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, -np.sin(X[5]), sign_safe(X[6])/(np.abs(X[6]) + 2.0), 0.5*sign_safe(X[7])/np.sqrt(np.abs(X[7]) + 1.0), 1.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, np.cos(X[6]), sign_safe(X[7]), 1.0 - np.tanh(X[8])**2, 1.0],
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -np.sin(X[7]), 1.0 - np.tanh(X[8])**2, 2*X[9]],
        [sign_safe(X[0])/(np.abs(X[0]) + 2.0), 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5*sign_safe(X[8])/np.sqrt(np.abs(X[8]) + 1.0), np.cos(X[9])],
        [-np.sin(X[0]), 1.0 - np.tanh(X[1])**2, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, sign_safe(X[9])]
    ])
    X0 = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
    max_iter = 200
    tol = 1e-6
    X, iter, norm = NewtonRaphson(R, K, X0, max_iter, tol)
    assert abs(norm) < tol
    