def is_valid_expression(object, function_symbols, leaf_symbols) -> bool:
    head = object.pop(0)
    if type(object) is int or (type(object) is str and object in leaf_symbols):
        return True
    elif type(object) is list and len(object) == 3 and head in function_symbols:
        for node in object:
            if is_valid_expression(node, function_symbols, leaf_symbols):
                return True
    return False


function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = ['f', 123, 'x']

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))
