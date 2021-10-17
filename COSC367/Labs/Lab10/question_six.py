def construct_perceptron(weights, bias):
    def perceptron(input):
        return 1 if (sum([(x*w) for x,w in zip(input, weights)]) + bias) >= 0 else 0
    return perceptron

def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    error = 0
    for _ in range(max_epochs):
        if error: break
        error = 1
        for w, t in training_examples:
            y = 1 if (sum([(i * j) for i,j in zip(w, weights)]) + bias) >= 0 else 0
            if y != t:
                error = 0
                for i in range(len(weights)):
                    weights[i] += learning_rate * w[i] * (t - y)
                bias += learning_rate * (t - y)
    return [weights,bias]

weights = [2, -4]
bias = 0
learning_rate = 0.5
examples = [
  ((0, 0), 0),
  ((0, 1), 0),
  ((1, 0), 0),
  ((1, 1), 1),
  ]
max_epochs = 50

weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
print(f"Weights: {weights}")
print(f"Bias: {bias}\n")

perceptron = construct_perceptron(weights, bias)

print(perceptron((0,0)))
print(perceptron((0,1)))
print(perceptron((1,0)))
print(perceptron((1,1)))
print(perceptron((2,2)))
print(perceptron((-3,-3)))
print(perceptron((3,-1)))
