from random import choice
import numpy as np
import matplotlib.pyplot as plt


def step_neg(x):
    return -1 if x < 0 else 1


def step(x):
    return 0 if x < 0 else 1


training_data_or = [
    (np.array([0, 0, 1]), 0),
    (np.array([0, 1, 1]), 1),
    (np.array([1, 0, 1]), 1),
    (np.array([1, 1, 1]), 1),
]

training_data_and = [
    (np.array([0, 0, 1]), 0),
    (np.array([0, 1, 1]), 0),
    (np.array([1, 0, 1]), 0),
    (np.array([1, 1, 1]), 1),
]

input = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]
                  ])

input_neg = np.array([[-1, -1],
                      [-1, 1],
                      [1, -1],
                      [1, 1]
                      ])

training_data_and_neg = [
    (np.array([-1, -1, 1]), -1),
    (np.array([-1, 1, 1]), -1),
    (np.array([1, -1, 1]), -1),
    (np.array([1, 1, 1]), 1),
]


def calc(training_data, func_act, bipolar):
    w = np.random.rand(3)
    errors = []
    eta = 0.1
    n = 1000

    for i in range(n):
        x, expected = choice(training_data)
        result = np.dot(w, x)
        error = expected - func_act(result)
        errors.append(error)
        w += eta * error * x

    for x, _ in training_data:
        result = np.dot(x, w)
        print("{}: {} -> {}".format(x[:2], result, func_act(result)))
    print("WEIGHT bias: {}  w1: {}  w2:{}".format(w[0], w[1], w[2]))

    w2, w1, b = w
    x = -b / w1
    y = -b / w2

    d = y
    c = -y / x

    plt.style.use('ggplot')

    if (bipolar):
        line_x_coords = np.array([-0.5, x])
        line_y_coords = c * line_x_coords + d
        plt.plot(line_x_coords, line_y_coords)
        plt.plot(input_neg[1:], input_neg[:-1], 'o')
        plt.axis([-2, 2, -2, 2])
    else:
        line_x_coords = np.array([-1, x])
        line_y_coords = c * line_x_coords + d
        plt.plot(line_x_coords, line_y_coords)
        plt.plot(input[1:], input[:-1], 'o')
        plt.axis([-1, 2, -1, 2])

    plt.show()


print('AND bipolar')
calc(training_data_and_neg, step_neg, True)
print('AND binar')
calc(training_data_and, step, False)
print('OR')
calc(training_data_or, step, False)

