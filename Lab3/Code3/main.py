import numpy as np


def learn(scheme, epochs, X, Y, L):
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
        dZ = E * L  # delta Z
        Wz += H.T.dot(dZ)  # update output layer weights
        dH = dZ.dot(Wz.T) * sigmoid_(H)  # delta H
        Wh += X.T.dot(dH)  # update hidden layer weights

    print('Hidden layer: \n' + str(Wh))
    print('Output layer: \n' + str(Wz))

    print('Z: \n' + str(Z))




def gen_data():
    x = np.arange(0.1, 5, 0.1)
    x = x.reshape(x.size, 1)
    C = 0.9 * np.random.rand() + 0.1
    A = 0.9 * np.random.rand() + 0.1
    S = 0.9 * np.random.rand() + 0.1
    print('\nC = ' + str(C) + '\nA = ' + str(A) + '\nS = ' + str(S))

    # return C * np.exp(-(np.power((x - A), 2) / S)), np.array(encl([C,A,S],x.size))
    return C * np.exp(-(np.power((x - A), 2) / S)), np.array([C,A,S])

#
# def den_m():
#     P = np.zeros([100, 21])
#     T = np.zeros([3, 100])
#     x = np.arange(0.1, 5*np.exp(-2), 1)
#     for _ in range(0, 100):
#         c = 0.9 * np.random.rand() + 0.1
#         a = 0.9 * np.random.rand() + 0.1
#         s = 0.9 * np.random.rand() + 0.1
#         T[0, _] = c
#         T[1, _] = a
#         T[2, _] = s
#         P[_,:] =c * np.exp(-(np.power((x - a),2) / s))
#
#     return P,T

def encl(l ,n):
    s = []
    for i in range(0,n):
        s.append(l)
    return s

data = gen_data()
np.seterrcall(learn([1, 15, 3], 200, data[0].reshape(data[0].size, 1), data[1].T, 0.01))


