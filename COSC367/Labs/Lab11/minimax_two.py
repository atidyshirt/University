max_val = lambda tree: tree if type(tree) is int else max([min_val(tree[i]) for i in range(len(tree))])
min_val = lambda tree: tree if type(tree) is int else min([max_val(tree[i]) for i in range(len(tree))])

def min_action_value(tree):
    index = 0
    high = float("inf")
    if type(tree) is int:
        return (None, tree)
    for i in range(len(tree)):
        tmp = max_val(tree[i])
        if tmp < high:
            high = tmp
            index = i
    return (index, high)

def max_action_value(tree):
    index = 0
    low = float("-inf")
    if type(tree) is int:
        return (None, tree)
    for i in range(len(tree)):
        tmp = min_val(tree[i])
        if tmp > low:
            low = tmp
            index = i
    return (index, low)

game_tree = [[1, 2], [3, 4]]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)
