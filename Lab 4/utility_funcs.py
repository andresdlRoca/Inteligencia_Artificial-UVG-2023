import numpy as np

def logistic_regression(X, y, k):
    m, n = X.shape
    theta = np.zeros(n)

    for i in range(k):
        Z = np.zeros((m, (i+1)*n))
        for j in range(i+1):
            Z[:, j*n:(j+1)*n] = np.power(X, i-j)
        U, S, V = np.linalg.svd(Z.T.dot(Z))
        S_inv = np.diag(1/S)
        theta = theta - V.T.dot(S_inv).dot(U.T).dot(Z.T).dot(sigmoid(Z.dot(theta))-y)

    return theta


def sigmoid(z):
    return 1 / (1 + np.exp(-z))