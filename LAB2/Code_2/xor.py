import numpy as np


def leanr_xor(scheme, X, Y, epochs, learning_rate):
    inputLayerSize, hiddenLayerSize, outputLayerSize = scheme

    def sigmoid(x): return 1 / (1 + np.exp(-x))  # activation function

    def sigmoid_(x): return x * (1 - x)  # derivative of sigmoid

    # weights on layer inputs
    Wh = np.random.uniform(size=(inputLayerSize, hiddenLayerSize))
    Wz = np.random.uniform(size=(hiddenLayerSize, outputLayerSize))

    for _ in range(epochs):
        H = sigmoid(np.dot(X, Wh))  # hidden layer results
        Z = np.dot(H, Wz)  # output layer, no activation
        E = Y - Z  # error
        dZ = E * learning_rate  # delta Z
        Wz += H.T.dot(dZ)  # update output layer weights
        dH = dZ.dot(Wz.T) * sigmoid_(H)  # delta H
        Wh += X.T.dot(dH)  # update hidden layer weights

    print('\nHidden layer: \n' + str(Wh))
    print('\nOutput layer: \n' + str(Wz))

    print('\nZ: \n' + str(Z))


X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([[0], [1], [1], [0]])

leanr_xor([2, 3, 1], X, Y, 20000, 0.1)
