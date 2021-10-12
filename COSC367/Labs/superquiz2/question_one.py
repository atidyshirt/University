def is_valid_expression(object, function_symbols, leaf_symbols) -> bool:
    if type(object) is int or (type(object) is str and object in leaf_symbols):
        return True
    elif type(object) is list and len(object) == 3 and object[0] in function_symbols:
        for node in object:
            if is_valid_expression(node, function_symbols, leaf_symbols):
                return True
    return False


function_symbols = ['f', '+']
leaf_symbols = ['x', 'y', -1, 0, 1]
expression = ['f', 0, ['f', 0, ['f', 0, ['f', 0, 'x']]]]

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))
