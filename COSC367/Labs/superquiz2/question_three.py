def evaluate(expression, bindings):
    if type(expression) is int: return expression
    elif type(expression) is str: return bindings[expression]
    else: return evaluate(expression[0], bindings)(evaluate(expression[1], bindings), evaluate(expression[2], bindings))



bindings = {}
expression = 12
print(evaluate(expression, bindings))
bindings = {'x':5, 'y':10, 'time':15}
expression = 'y'
print(evaluate(expression, bindings))
bindings = {'x': 5, 'y': 10, 'time': 15, 'add': lambda x, y: x + y}
expression = ['add', 12, 'x']
print(evaluate(expression, bindings))

import operator

bindings = dict(x = 5, y = 10, blah = 15, add = operator.add)
expression = ['add', ['add', 22, 'y'], 'x']
print(evaluate(expression, bindings))
