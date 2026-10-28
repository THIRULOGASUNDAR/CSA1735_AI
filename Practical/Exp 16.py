# Feedforward Neural Network for XOR
# Without using sklearn

import math

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Input data for XOR
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

# Predefined weights and biases
def predict(x1, x2):
    h1 = sigmoid(20 * x1 + 20 * x2 - 10)
    h2 = sigmoid(-20 * x1 - 20 * x2 + 30)

    output = sigmoid(20 * h1 + 20 * h2 - 30)

    return 1 if output >= 0.5 else 0

print("Feedforward Neural Network (XOR)")

for inputs in X:
    result = predict(inputs[0], inputs[1])
    print("Input", inputs, "-> Output", result)
