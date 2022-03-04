import numpy as np
def perceptron_train(X,Y):
    m, n = X.shape
    weights = np.zeros(2)
    bias = 0
    for _ in range(1000):
        for x, y in zip(X,Y):
            pred = predict(x,weights)
            weights[:] = weights[:] + (y - pred) * x
            bias = bias + (y-pred) 
    #print(weights)
    #print(bias)
    return weights, bias

def perceptron_test(X,Y,w,b):
    accuracy = 0.0
    for x, y in zip(X,Y):
        sum = x[0]*w[0]+x[1]*w[1]+b
        #print(sum)
        accuracy += 1.0 if sum > y else 0.0
    return accuracy / Y.size

def predict(X, weights):
    activation = weights[0]
    for i in range(len(X)-1):
	    activation += weights[i] * X[i]
    return 1.0 if activation >= 0.0 else -1.0