import numpy as np
 
 
def fluid_analysis(M: np.ndarray, G: np.ndarray,
                   rp: np.ndarray, vstar: np.ndarray):
    

    
    
    # TODO: check if M is a numpy matrix and is square
    if not isinstance(M, np.ndarray):
        raise ValueError('The input should be a vector')
        
    if M.ndim != 2 or M.shape[0] != M.shape[1]:
        raise RuntimeError('M must be a square matrix')
        
 
    # TODO: check if G is a numpy matrix
    if not isinstance(G, np.ndarray):
        raise ValueError('G must be a square matrix') 
 
    # TODO: check if rp is a numpy vector
    if not isinstance(rp, np.ndarray):
        raise RuntimeError('rp must be a numpy array')
    if rp.ndim != 1:
        raise RuntimeError('rp must be a 1D vector') 
 
    # TODO: check if vstar is a numpy vector
    if not isinstance(vstar, np.ndarray):
        raise RuntimeError('vstar must be a numpy array')
    if rp.ndim != 1:
        raise RuntimeError('vstar must be a 1D vector')  
 
    # TODO: check if M and G have same number of rows
    if M.shape[0] != G.shape[0]:
        raise RuntimeError('M and G must have the same number of rows') 
 
    # TODO: check if number of rows of G is equal to the size of vstar vector
    if G.shape[0] != vstar.size:
        raise RuntimeError('Number of rows of G must equal size of vstar')
 
    # TODO: check if size of rp is equal to the number of columns of G
    if rp.size != G.shape[1]:
        raise RuntimeError('Size of rp must equal number of columns of G')
        
    # TODO: check if M is a diagonal matrix
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if i != j and M[i, j] != 0.0:
                raise RuntimeError('M must be a diagonal matrix')
 
    # TODO: invert the diagonal values of M
    M_inv = np.zeros((M.shape[0], M.shape[1]))
    for i in range(M.shape[0]):
        M_inv[i, i] = 1.0 / M[i, i]
        
    # TODO: compute the tangent matrix
    K = (G.T)@M_inv@G
 
    # TODO: compute the right hand side vector
    b = rp - ((G.T)@vstar)
 
    # TODO: solve for the pressure vector
    p = np.linalg.solve(K,b)
 
    # TODO: compute the corrector velocity vector
    v = M_inv@(G@p)+vstar
    
    # TODO: create augmented matrix 
    # [K, G]
    # [G.T, 0]
    zero_block = np.zeros((G.shape[1], G.shape[1]), dtype=float)
    K_augmented = np.block([[M,    G], [G.T, zero_block]])
    
    
    # TODO: perform eigenvalue analysis for the augmented matrix
    lam, x = np.linalg.eig(K_augmented)
 
    return p, v, lam, x