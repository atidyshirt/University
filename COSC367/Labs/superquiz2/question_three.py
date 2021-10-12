def evaluate(expression, bindings):
    if type(expression) is int:
        return expression
    elif type(expression) is str:
        return bindings[expression]
    tmp = [bindings[n] if type(n) is str else n for n in expression]
    if callable(tmp[0]):
        return evaluate(expression[1:], bindings) # NOTE: I should be do something like this \\ + tmp[0](tmp[1], tmp[2])
    else:
        return sum(tmp) # FIXME: Not like this



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
