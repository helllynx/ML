import numpy as np
import matplotlib.pyplot as plt


# import pandas as pd

def activation_func_logistic(x):
    return 1 / (1 + np.exp(-x))


# Make a prediction with weights
def predict(row, weights, act_func):
    activation = weights[0]
    for i in range(len(row) - 1):
        activation += weights[i + 1] * row[i]
    return act_func(activation)


# Estimate Perceptron weights using stochastic gradient descent
def train_weights(train, l_rate, n_epoch, act_func):
    weights = [0.0 for _ in range(len(train[0]))]
    for epoch in range(n_epoch):
        sum_error = 0.0
        for row in train:
            prediction = predict(row, weights, act_func)
            error = row[-1] - prediction
            sum_error += error ** 2
            weights[0] = weights[0] + l_rate * error
            for i in range(len(row) - 1):
                weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
    print('>> epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
    return weights


def plot_decisive_line(w0, w1, data, title):
    x = np.arange(min(w0, w1), max(w0, w1))
    y = my_formula(x, w0, w1)  # <- note now we're calling the function 'formula' with x
    plt.plot(x, y)
    x_check = np.array(w0) * np.array(get_encl_list_elem(data, 0))
    y_check = np.array(w1) * np.array(get_encl_list_elem(data, 1))
    plt.plot(x_check, y_check, marker='o', linestyle='')
    plt.grid(True)
    plt.title(title)
    plt.show()


def my_formula(x, w0, w1):
    return x * w1 - w0


def get_encl_list_elem(l, st):
    res = []
    for i in l:
        res.append(i[st])
    return res


l_rate = 1
n_epoch =  30

data_and = [[0, 0, 0],
            [0, 1, 0],
            [1, 0, 0],
            [1, 1, 1]]

data_or = [[0, 0, 0],
           [0, 1, 1],
           [1, 0, 1],
           [1, 1, 1]]

print('OR')
w_or = train_weights(data_or, l_rate, n_epoch, activation_func_logistic)
print(w_or)

print('AND')
w_and = train_weights(data_and, l_rate, n_epoch, activation_func_logistic)
print(w_and)

plot_decisive_line(w_and[0], w_and[1], data_and, 'AND')

plot_decisive_line(w_or[0], w_or[1], data_or, 'OR')
