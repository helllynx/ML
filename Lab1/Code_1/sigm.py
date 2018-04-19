import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def graph(formula, x_range):
    x = np.array(x_range)
    y = formula(x)
    plt.plot(x, y)
    plt.grid()
    plt.show()


x0 = 0
x1 = 0
x2 = 0


def my_formula(x):
    return x ** x2 + x * x1 + x0

def my_formula(x):
    return x * x1 + x0


def activation_func_binary_step(x):
    return 1.0 if x >= 0.0 else 0.0


def activation_func_logistic(x):
    return 1 / (1 + np.exp(-x))

def diff_logistic_func(x):
    return np.exp(-x)/(np.exp(-x)+1)**2


def activation_func_tanh(x):
    return np.tanh(x)


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


def plot_act_func(l_rate, n_epoch, dataset, act_func, plot_x):
    weights = train_weights(dataset, l_rate, n_epoch, act_func)
    print(weights)

    global x0, x1, x2
    x0 = weights[0]
    x1 = weights[1]
    x2 = weights[2]
    graph(my_formula, np.arange(plot_x[0], plot_x[1], 0.1))

def plot_activation_func_binary_step():
    nums = np.arange(-5, 5, step=0.5)
    y = []
    for n in nums:
        y.append(activation_func_binary_step(n))
    y = np.array(y)
    plt.plot(nums, y, 'r')
    plt.axis([-6, 6, -0.5, 1.5])
    plt.grid()
    plt.show()

def plot_activation_func_logistic():
    nums = np.arange(-5, 5, step=0.5)
    plt.plot(nums, activation_func_logistic(nums), 'r')
    plt.axis([-6, 6, -0.5, 1.5])
    plt.grid()
    plt.show()


def plot_activation_diff_func_logistic():
    nums = np.arange(-5, 5, step=0.5)
    plt.plot(nums, diff_logistic_func(nums), 'r')
    plt.axis([-6, 6, -0.5, 1])
    plt.grid()
    plt.show()

def plot_activation_func_tanh():
    nums = np.arange(-5, 5, step=0.5)
    plt.plot(nums, activation_func_tanh(nums), 'r')
    plt.axis([-6, 6, -1.5, 1.5])
    plt.grid()
    plt.show()

# plot activation functions
plot_activation_func_binary_step()
plot_activation_func_tanh()
plot_activation_func_logistic()

# plot sigmoid diff
plot_activation_diff_func_logistic()

df = pd.read_csv('data.txt', header=None, names=['Exam 1', 'Exam 2', 'Admitted'])
df.head(10)


l_rate = 0.03
n_epoch = 5

print('Use Binary step activation function')
plot_act_func(l_rate, n_epoch, df.values.tolist(), activation_func_binary_step, [0, 1])

print('Use Logistic (a.k.a. Soft step) activation function')
plot_act_func(l_rate, n_epoch, df.values.tolist(), activation_func_logistic, [0.01, 1])

print('Use TanH activation function')
plot_act_func(l_rate, n_epoch, df.values.tolist(), activation_func_tanh, [-1, 1])




