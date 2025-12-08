import numpy as np

N = 10 

# Define the function 
def R(X):
    res = np.zeros(N)
    for i in range(N):
        res[i] = np.tanh(X[i]) + np.sqrt(X[(i+1)%N] + 1.0) - 1.0
    return res

# Define the Jacobian matrix 
def K(X):
    K = np.zeros((N, N))
    for i in range(N):
        K[i, i] = 1.0 - np.tanh(X[i])**2
        K[i, (i+1)%N] = 0.5/np.sqrt(X[(i+1)%N] + 1.0)
    return K

# Define the initial guess
X0 = np.zeros(N)

# Define the maximum number of iterations
max_iter = 200

# Define the tolerance for solution accuracy
tol = 1e-6

# Define the Newton-Raphson function
def NewtonRaphson(R, K, X0, max_iter, tol):
    # Compute the residual for the initial guess
    R0 = R(X0)
    print(f'R0 = {np.linalg.norm(R0)}')

    # Check if the initial guess is already the solution
    if np.linalg.norm(R0) < tol:
        print('The initial guess is the actual solution')
        return X0, 0, np.linalg.norm(R0)

    # Start the iteration
    Xj = X0
    for iter in range(max_iter):
        # Compute the Jacobian K at the current solution
        Kj = K(Xj)

        # Compute the change in the solution (delta X)
        dXj = -np.linalg.solve(Kj, R(Xj))

        # Update the guessed solution
        Xj = Xj + dXj

        # Compute the residual for the updated solution
        Rj = R(Xj)

        # Check if the norm of the residual is below the tolerance
        if np.linalg.norm(Rj) < tol:
            print(f'Solution found in {iter+1} iterations')
            return Xj, iter+1, np.linalg.norm(Rj)

    # If max iterations are reached without converging, return the last solution
    print('Solution not found within maximum iterations')
    return Xj, max_iter, np.linalg.norm(Rj)


X, iter, norm = NewtonRaphson(R, K, X0, max_iter, tol)

# Print 
print(f'Solution: {X}')
print(f'Number of iterations: {iter}')
print(f'Norm of the last residual: {norm}')
