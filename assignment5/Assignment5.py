import numpy as np

def fluid_analysis(M: np.ndarray, G: np.ndarray, rp: np.ndarray, vstar: np.ndarray):
    # Input type checks
    if not isinstance(M, np.ndarray):
        raise TypeError("M must be a numpy array")
    if M.shape[0] != M.shape[1]:
        raise ValueError("M must be a square matrix")
    
    if not isinstance(G, np.ndarray):
        raise TypeError("G must be a numpy array")
    
    if not isinstance(rp, np.ndarray):
        raise TypeError("rp must be a numpy array")
    
    if not isinstance(vstar, np.ndarray):
        raise TypeError("vstar must be a numpy array")
    
    # Dimension checks
    if G.shape[1] != M.shape[0]:
        raise ValueError("G's number of columns must match M's number of rows")
    if G.shape[0] != vstar.shape[0]:
        raise ValueError("G's number of rows must match vstar's size")
    if rp.shape[0] != G.shape[1]:
        raise ValueError("rp's size must match G's number of columns")
    
    # Ensure M is diagonal (square matrix, diagonal elements only)
    if not np.allclose(M, np.diag(np.diag(M))):
        raise RuntimeError("M must be a diagonal matrix")
    
    # Invert the diagonal matrix M
    M_inv = np.diag(1.0 / np.diag(M))
    
    # Compute the tangent matrix K = G^T * M_inv * G
    K = np.dot(np.dot(G.T, M_inv), G)
    
    # Compute the right-hand side vector b = rp - G^T * vstar
    b = rp - np.dot(G.T, vstar)
    
    # Solve for the pressure vector p using K * p = b
    try:
        p = np.linalg.solve(K, b)
    except np.linalg.LinAlgError:
        raise RuntimeError("Failed to solve for pressure vector p")
    
    # Compute the corrector velocity vector v = M_inv * G * p + vstar
    v = np.dot(M_inv, np.dot(G, p)) + vstar
    
    # Create the augmented matrix K_a
    K_augmented = np.block([[M, G], [G.T, np.zeros((G.shape[1], G.shape[1]))]])
    
    # Perform eigenvalue analysis for the augmented matrix
    lam, x = np.linalg.eig(K_augmented)
    
    # Return the results
    return p, v, lam, x
