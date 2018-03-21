import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x): return 1 / (1 + np.exp(-x))  # activation function


def sigmoid_(x): return x * (1 - x)  # derivative of sigmoid


Wh = np.array([])
Wz = np.array([])
E = np.array([])


def learn(scheme, epochs, data_count, gen_data, learning_rate):
    inputLayerSize, hiddenLayerSize, outputLayerSize = scheme

    # weights on layer inputs
    global Wh, Wz, E
    Wh = np.random.uniform(size=(inputLayerSize, hiddenLayerSize))
    Wz = np.random.uniform(size=(hiddenLayerSize, outputLayerSize))

    for __ in range(data_count):
        data = gen_data()
        X, Y = data[0].reshape(data[0].size, 1), data[1].T

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

        print('\nZ: \n' + str(Z[-1:]))
        print('\nError: \n'+str(E[-1:]))


def check_error():
    sum_e = np.array([])
    for e in E:
        sum_e = np.append(sum_e, sum(np.abs(e)))
    x = np.arange(sum_e.size)
    plt.plot(x, sum_e)
    plt.title('Error graph')
    plt.grid(True)
    plt.show()


def gen_data():
    x = np.arange(1, 10, 0.2)
    x = x.reshape(x.size, 1)
    C = 0.9 * np.random.rand() + 0.1
    A = 0.9 * np.random.rand() + 0.1
    S = 0.9 * np.random.rand() + 0.1
    print('\nC = ' + str(C) + '\nA = ' + str(A) + '\nS = ' + str(S))

    return C * np.exp(-(np.power((x - A), 2) / S)), np.array([C, A, S])


# learn([1, 15, 3], 200, data[0].reshape(data[0].size, 1), data[1].T, 0.01)
learn([1, 1, 3], 1000, 10, gen_data, 0.01)


check_error()