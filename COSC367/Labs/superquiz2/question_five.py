""" Question

Sequence definition: a[0], a[1], ..., a[i]

in a sequence if i > 1, we have a[i] = f(x,y,i) where x=a[i-2], y = a[i-1]

if f is a function (expression invulving i,x or y) then the function describes the pattern of the sequence

Examples:

The sequence [0, 1, 2, 3, 4, 5, 6,...] can be described by f(x, y, i) = i or f(x, y, i)=y+1

The sequence [1, 4, 9, 16, 25,...] can be described by f(x, y, i) = (i+1)*(1+i).

The sequence [0, 1, 1, 2, 3, 5, 8, 13, ...] the Fibonacci sequence, can be described by f(x, y, i) = x + y.

Task:

Write a function generate_rest(initial_sequence, expression, length) that takes an initial sequence of
numbers, an expression, and a specified length, and returns a list of integers with the specified length
that is the continuation of the initial list according to the given expression

NOTE: It is recommended that you use your implementation of the evaluate function.
      This would allow you to implement this function in about 11 lines of code
"""

def evaluate(expression, bindings):
    if type(expression) is int: return expression
    elif type(expression) is str: return bindings[expression]
    else: return evaluate(expression[0], bindings)(evaluate(expression[1], bindings), evaluate(expression[2], bindings))

def generate_rest(initial_sequence, expression, length):
    initial_size = len(initial_sequence)
    bindings = {
        '*': lambda x, y: x * y,
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
    }
    for i in range(initial_size, initial_size + length):
        bindings['i'] = i
        bindings['x'] = initial_sequence[-2]
        bindings['y'] = initial_sequence[-1]
        val = evaluate(expression, bindings)
        initial_sequence.append(val)
    return initial_sequence[initial_size:]

# Test cases
initial_sequence = [0, 1, 2]
expression = 'i'
length_to_generate = 5
print(generate_rest(initial_sequence,
                    expression,
                    length_to_generate))

initial_sequence = [4, 6, 8, 10]
expression = ['*', ['+', 'i', 2], 2]
length_to_generate = 5
print(generate_rest(initial_sequence,
                    expression,
                    length_to_generate))
