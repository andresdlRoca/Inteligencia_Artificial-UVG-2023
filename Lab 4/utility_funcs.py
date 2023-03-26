import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def logistic_regression(X, y, learning_rate=0.01, num_iterations=1000):
    m, n = X.shape
    weights = np.zeros((n, 1))
    bias = 0
    for i in range(num_iterations):

        #Propagacion
        y_pred = sigmoid(np.dot(X, weights) + bias)
        
        # Costos
        cost = (-1/m) * np.sum(y * np.log(y_pred) + (1-y) * np.log(1-y_pred))
        
        # Calculo de gradiente
        dw = (1/m) * np.dot(X.T, (y_pred-y))
        db = (1/m) * np.sum(y_pred-y)
        

        weights = weights - learning_rate * dw
        bias = bias - learning_rate * db
        
        # Costos cada 100 iteraciones
        if i % 100 == 0:
            print("Cost despues de iteracion %i: %f" % (i, cost))
    
    return weights, bias