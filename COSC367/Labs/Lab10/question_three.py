
def construct_perceptron(weights, bias):
    def perceptron(input):
        return 1 if (sum([(x*w) for x,w in zip(input, weights)]) + bias) >= 0 else 0
    return perceptron

weights = [2, -4]
bias = 0
perceptron = construct_perceptron(weights, bias)

print(perceptron([1, 1]))
print(perceptron([2, 1]))
print(perceptron([3, 1]))
print(perceptron([-1, -1]))
