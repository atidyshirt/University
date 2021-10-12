def depth(expression):
    if type(expression) is int or (type(expression) is str): # if is leaf
        return 0
    else:
        return 1 + max(depth(element) for element in expression)
