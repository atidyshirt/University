import random

def random_expression(function_symbols, leaves, max_depth, current_depth=0):
    coin = random.randint(0,1)
    if coin == 0 or current_depth == max_depth: return random.choice(leaves)
    else: return [random.choice(function_symbols), random_expression(function_symbols, leaves, max_depth, current_depth + 1), random_expression(function_symbols, leaves, max_depth, current_depth + 1)]

def is_valid_expression(object, function_symbols, leaf_symbols) -> bool:
    if type(object) is int or (type(object) is str and object in leaf_symbols):
        return True
    elif type(object) is list and len(object) == 3 and object[0] in function_symbols:
        for node in object:
            if is_valid_expression(node, function_symbols, leaf_symbols):
                return True
    return False

function_symbols = ['f', 'g', 'h']
constant_leaves =  list(range(-2, 3))
variable_leaves = ['x', 'y', 'i']
leaves = constant_leaves + variable_leaves
max_depth = 4

for _ in range(10000):
    expression = random_expression(function_symbols, leaves, max_depth)
    if not is_valid_expression(expression, function_symbols, leaves):
        print("The following expression is not valid:\n", expression)
        break
else:
    print("OK")
