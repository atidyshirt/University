from math import inf

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

# [2, [-1, 5], [1, 3], 4]

pruned_tree = [
    # COMPLETE
    ]


pruning_events = [
    # (alpha, beta),
    ]
