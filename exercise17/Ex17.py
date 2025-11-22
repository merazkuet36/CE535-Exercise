import numpy as np
import scipy.linalg as la


class EigenvalueAnalysis:
    def __init__(self, A: np.ndarray, B: np.ndarray = None):
        # check a is matrix and square
        if not isinstance(A, np.ndarray):
            raise RuntimeError("A must be a numpy.ndarray")
        if A.ndim != 2:
            raise RuntimeError("A must be a 2D matrix")
        if A.shape[0] != A.shape[1]:
            raise RuntimeError("A must be a square matrix")

        self.A = A

        # check if B is a numpy matrix and is square
        if B is not None:
            if not isinstance(B, np.ndarray):
                raise RuntimeError("B must be a numpy.ndarray")
            if B.ndim != 2:
                raise RuntimeError("B must be a 2D matrix")
            if B.shape != A.shape:
                raise RuntimeError("B must have the same shape as A")
            self.B = B
        else:
            self.B = None

        #Eigenvalue analysis
        if self.B is not None:
            lam, x = la.eig(self.A, self.B)      
        else:
            lam, x = np.linalg.eig(self.A)       

        # Sort lambda 
        self.lam = np.sort(lam)
        self.x = x

    def check(self, lam_i: float, x_i: np.ndarray) -> bool:
        # Type checks 
        if not np.isscalar(lam_i):
            raise RuntimeError("lam_i must be a scalar (float)")
        lam_i = float(lam_i)

        if not isinstance(x_i, np.ndarray):
            raise RuntimeError("x_i must be a numpy.ndarray")

        # Ensure x_i is a 1D vector
        if x_i.ndim == 2 and 1 in x_i.shape:
            x_i = x_i.reshape(-1)
        elif x_i.ndim != 1:
            raise RuntimeError("x_i must be a vector (1D array)")

        # Dimension check 
        if x_i.size != self.A.shape[0]:
            raise RuntimeError("Dimension mismatch between x_i and A")

        #  Compute residual 
        if self.B is None:
            
            residual = self.A @ x_i - lam_i * x_i
        else:
            
            residual = self.A @ x_i - lam_i * (self.B @ x_i)

        # compute norm and tolerance check 
        norm = np.linalg.norm(residual, ord=2)
        tol = 1e-10
        return norm < tol


