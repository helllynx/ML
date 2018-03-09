from random import choice
from numpy import array, dot, random, arange
import matplotlib.pyplot as plt

unit_step = lambda x: 0 if x < 0 else 1

training_data_or = [
    (array([0,0,1]), 0),
    (array([0,1,1]), 1),
    (array([1,0,1]), 1),
    (array([1,1,1]), 1),
]

training_data_and = [
    (array([0,0,1]), 0),
    (array([0,1,1]), 0),
    (array([1,0,1]), 0),
    (array([1,1,1]), 1),
]

X = array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

def calc(training_data):
    w = random.rand(3)
    errors = []
    eta = 0.2
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

    # After your code
    plt.style.use('ggplot')

    b, w1, w2 = w
    x = -b / w1
    y = -b / w2

    d = y
    c = -y / x

    line_x_coords = array([0, x])
    line_y_coords = c * line_x_coords + d

    print(line_x_coords)
    print(line_y_coords)
    print(*X[:, 1:].T)

    # plt.plot(line_x_coords, line_y_coords)
    # plt.scatter(*X[:, 1:].T, c=[0,0,0,1], s=75)
    # plt.show()

calc(training_data_and)
# calc(training_data_or)


# After your code
plt.style.use('ggplot')

b, w1, w2 = w
x = -b / w1
y = -b / w2

d = y
c = -y / x

line_x_coords = array([0, x])
line_y_coords = c * line_x_coords + d

plt.plot(line_x_coords, line_y_coords)
plt.scatter(*input[:, 1:].T, c=target, s=75)
plt.show()


