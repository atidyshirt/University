def construct_perceptron(weights, bias):
    def perceptron(input):
        return 1 if (sum([(x*w) for x,w in zip(input, weights)]) + bias) >= 0 else 0
    return perceptron

def accuracy(classifier, inputs, expected_outputs):
    count = 0
    for n, g in zip(inputs, expected_outputs):
        print(n, g)
        if classifier(n) == g:
            count += 1
    return count/len(expected_outputs)

perceptron = construct_perceptron([-1, 3], 2)
inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
targets = [0, 1, 1, 0]

print(accuracy(perceptron, inputs, targets))
