def max_value(tree):
    if type(tree) is int:
        return tree

    return max([min_value(tree[i]) for i in range(len(tree))])

def min_value(tree):
    if type(tree) is int:
        return tree
    return min([max_value(tree[i]) for i in range(len(tree))])


game_tree = [1, 2, 3]

print("Root utility for minimiser:", min_value(game_tree))
print("Root utility for maximiser:", max_value(game_tree))
