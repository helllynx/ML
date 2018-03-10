from random import choice
from numpy import array, dot, random
import matplotlib.pyplot as plt

unit_step = lambda x: 0 if x < 0 else 1

training_data_or = [
    (array([0, 0, 1]), 0),
    (array([0, 1, 1]), 1),
    (array([1, 0, 1]), 1),
    (array([1, 1, 1]), 1),
]

training_data_and = [
    (array([0, 0, 1]), 0),
    (array([0, 1, 1]), 0),
    (array([1, 0, 1]), 0),
    (array([1, 1, 1]), 1),
]



input = array([ [0,0],
            [0,1],
            [1,0],
            [1,1]
          ])



def calc(training_data):
    w = random.rand(3)
    errors = []
    eta = 0.5
    n = 100

    for i in range(n):
        x, expected = choice(training_data)
        result = dot(w, x)
        error = expected - unit_step(result)
        errors.append(error)
        w += eta * error * x

    for x, _ in training_data:
        result = dot(x, w)
        print("{}: {} -> {}".format(x[:2], result, unit_step(result)))
    print("WEIGHT bias: {}  w1: {}  w2:{}".format(w[0], w[1], w[2]))

    plt.style.use('ggplot')

    w2, w1, b = w
    x = -b / w1
    y = -b / w2

    d = y
    c = -y / x

    line_x_coords = array([0, x])
    line_y_coords = c * line_x_coords + d

    plt.plot(line_x_coords, line_y_coords)
    plt.plot(input[1:], input[:-1], 'o')
    plt.axis([-1, 2, -1, 2])
    plt.show()




calc(training_data_and)
calc(training_data_or)
