import numpy as np


def leanr_xor(scheme, epochs):
    epochs = 20000  # Number of iterations
    inputLayerSize, hiddenLayerSize, outputLayerSize = scheme
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

    print('Hidden layer: \n' + str(Wh))
    print('Output layer: \n' + str(Wz))

    print('Z: \n' + str(Z))


leanr_xor([2, 3, 1], 20000)

#
#

#
# from numpy import exp, array, random, dot
#
#
# class NeuralNetwork():
#     def __init__(self, n=3, m=1):
#         # Create a simple neural network with one layer of n neurons at input and 1 output
#         random.seed(1)
#         self.synaptic_weights = {}
#         self.num_layers = 1
#         self.synaptic_weights[self.num_layers] = 2 * random.random((n, m)) - 1
#         ## Assign weights randomly
#
#
#
#     # The Sigmoid function, which describes an S shaped curve.
#     def sigmoid(self, x, derive=False):
#         if (derive == True):
#             return x * (1 - x)
#         return 1 / (1 + exp(-x))
#
#     # Using gradient Descent to train the network
#     def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
#         for iteration in range(number_of_training_iterations):
#             # Forward Propagation of Signal
#             output = self.think(training_set_inputs)
#
#             # Calculate the error (The difference between the desired output
#             # and the predicted output).
#             error = (training_set_outputs - output)
#
#             # Backpropagation of error
#             adjustment = dot(training_set_inputs.T, error * self.sigmoid(output, derive=True))
#
#             # Adjust the weights.
#             self.synaptic_weights[self.num_layers] += adjustment
#
#     # Function used to calculate ouput for any given input.
#     def think(self, inputs):
#         return self.sigmoid(dot(inputs, self.synaptic_weights[self.num_layers]))
#
# if __name__ == "__main__":
#     # Intialize a single neuron neural network with 2 neurons + 1 threshold (reated as input set to 1) and 1 layer.
#     neural_network = NeuralNetwork()
#
#     print("Random starting synaptic weights: ")
#     print(neural_network.synaptic_weights)
#
#     # The training set. We have 4 examples, each consisting of 2 input values
#     # and 1 threshold input set to 1.
#     training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
#     training_set_outputs = array([[0, 1, 1, 0]]).T
#     # Train the neural network using a training set.
#     # Do it 10,000 times and make small adjustments each time.
#     neural_network.train(training_set_inputs, training_set_outputs, 10000)
#
#     print("New synaptic weights after training: ")
#     print(neural_network.synaptic_weights)
#
#     # Test the neural network with a some input.
#     print("Considering new situation [1, 0, 1] -> ?: ")
# print(neural_network.think(array([1, 0, 1])))