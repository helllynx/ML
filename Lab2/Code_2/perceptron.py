import numpy as np
import matplotlib.pyplot as plt


def plot_line(w, data):
    x = np.arange(min(w), max(w), 0.2)
    y = line_formula(x, w)
    print(normalize(y))
    print(normalize(x))
    plt.plot(normalize(x), normalize(y))
    plt.plot(get_encl_list_elem(data, 0), get_encl_list_elem(data, 1),  marker='o', linestyle='')
    plt.show()



def get_encl_list_elem(l, st):
    res = []
    for i in l:
        res.append(i[st])
    return res

def normalize(x):
    return (x - min(x)) / (max(x) - min(x))


def line_formula(w, data):
    x = -w[0] / w[1]
    y = -w[0] / w[2]
    d = y
    c = -y /x
    x_l = np.arange(0, x)
    y_l = c*x_l+d
    print(x_l)
    print(y_l)
    plt.plot(x_l, y_l)
    plt.show()


class Perceptron(object):
    """Implements a perceptron network"""

    def __init__(self, input_size, lr=1, epochs=200):
        self.W = np.zeros(input_size + 1)
        # add one for bias
        self.epochs = epochs
        self.lr = lr

    def activation_fn(self, x):
        # return (x >= 0).astype(np.float32)
        return 1 if x >= 0 else 0

    def predict(self, x):
        z = self.W.T.dot(x)
        a = self.activation_fn(z)
        return a

    def fit(self, X, d):
        for _ in range(self.epochs):
            for i in range(d.shape[0]):
                x = np.insert(X[i], 0, 1)
                y = self.predict(x)
                e = d[i] - y
                self.W = self.W + self.lr * e * x


if __name__ == '__main__':
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    # d = np.array([0, 0, 0, 1])
    d = np.array([0, 1, 1, 1])

    perceptron = Perceptron(input_size=2)
    perceptron.fit(X, d)
    print(perceptron.W)
    # plot_line(perceptron.W, X)
    line_formula(perceptron.W, X)
