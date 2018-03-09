#   XOR.py-A very simple neural network to do exclusive or.
#   sigmoid activation for hidden layer, no (or linear) activation for output

import numpy as np
import matplotlib.pyplot as plt

epochs = 20000  # Number of iterations
inputLayerSize, hiddenLayerSize, outputLayerSize = 2, 3, 1
L = 0.1  # learning rate

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([[0], [1], [1], [0]])


def sigmoid(x): return 1 / (1 + np.exp(-x))  # activation function


def sigmoid_(x): return x * (1 - x)  # derivative of sigmoid


# weights on layer inputs
Wh = np.random.uniform(size=(inputLayerSize, hiddenLayerSize))
Wz = np.random.uniform(size=(hiddenLayerSize, outputLayerSize))

for _ in range(epochs):
    H = sigmoid(np.dot(X, Wh))  # hidden layer results
    Z = np.dot(H, Wz)  # output layer, no activation
    E = Y - Z  # error
    dZ = E * L  # delta Z
    Wz += H.T.dot(dZ)  # update output layer weights
    dH = dZ.dot(Wz.T) * sigmoid_(H)  # delta H
    Wh += X.T.dot(dH)  # update hidden layer weights
#
#
# def plto_solve_line(w1, w2):
#     x = np.array()
#     y = x*w1+w2
#     plt.plot(x, y)
#     plt.grid()
#     plt.show()


print(Z)  # what have we learnt?

