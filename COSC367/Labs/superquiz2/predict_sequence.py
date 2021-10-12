import random

class SequencePredicter:
    def __init__(self, sequence):
        self.bindings = {
            '*': lambda x, y: x * y,
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
        }
        self.sequence = sequence
        self.predicted_sequence = self.predict_rest()

    def predict_rest(self) -> list:
        function_symbols = ['*', '+', '-']
        leaves = [-2, -1, 0, 1, 2, 'i', 'x', 'y']
        current = []
        expression = []
        while current != self.sequence:
            expression = self.random_expression(function_symbols, leaves, 3)
            current = self.sequence[:2] + self.generate_rest(self.sequence[:2], expression, len(self.sequence) - 2)
        return self.generate_rest(current, expression, 5)

    def random_expression(self, function_symbols, leaves, max_depth, current_depth=0):
        coin = random.randint(0,1)
        if coin == 0 or current_depth == max_depth: return random.choice(leaves)
        else: return [random.choice(function_symbols), self.random_expression(function_symbols, leaves, max_depth, current_depth + 1), self.random_expression(function_symbols, leaves, max_depth, current_depth + 1)]

    def is_valid_expression(self, object, function_symbols, leaf_symbols):
        if type(object) is int or (type(object) is str and object in leaf_symbols):
            return True
        elif type(object) is list and len(object) == 3 and object[0] in function_symbols:
            for node in object:
                if self.is_valid_expression(node, function_symbols, leaf_symbols):
                    return True
        return False

    def evaluate(self, expression, bindings):
        if type(expression) is int: return expression
        elif type(expression) is str: return bindings[expression]
        else: return self.evaluate(expression[0], bindings)(self.evaluate(expression[1], bindings), self.evaluate(expression[2], bindings))

    def generate_rest(self, initial_sequence, expression, length):
        initial_size = len(initial_sequence)
        for i in range(initial_size, initial_size + length):
            self.bindings['i'] = i
            self.bindings['x'] = initial_sequence[-2]
            self.bindings['y'] = initial_sequence[-1]
            val = self.evaluate(expression, self.bindings)
            initial_sequence.append(val)
        return initial_sequence[initial_size:]

    def depth(self, expression):
        if type(expression) is int or (type(expression) is str):
            return 0
        else:
            return 1 + max(self.depth(element) for element in expression)
