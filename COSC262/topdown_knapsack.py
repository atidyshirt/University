class Item:
    """An item to (maybe) put in a knapsack"""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f"Item({self.value}, {self.weight})"
 
def max_value(items, capacity):
    """The maximum value achievable with a given list of items and a given
       knapsack capacity."""

    # *** IMPLEMENT ME ***
    values = []
    weights = []
    for item in items:
        values.append(item.value)
        weights.append(item.weight)

    n = len(values) - 1

    m = [[-1]*(capacity + 1) for _ in range(n + 1)]
    values.insert(0, None) # so that the value of the ith item is at value[i]
    weights.insert(0, None) # so that the weight of the ith item is at weight[i]
    return knapsack(values, weights, m, n, capacity)

def knapsack(value, weight, m, i, w):
    if m[i][w] >= 0:
        return m[i][w]
 
    if i == 0:
        q = 0
    elif weight[i] <= w:
        q = max(knapsack(value, weight, m, i - 1 , w - weight[i]) + value[i], knapsack(value, weight, m, i - 1 , w))
    else:
        q = knapsack(value, weight, m, i - 1 , w)
    m[i][w] = q
    return q

# Main
# The example in the lecture notes
items = [Item(45, 3),
         Item(45, 3),
         Item(80, 4),
         Item(80, 5),
         Item(100, 8)]
print(max_value(items, 10)) 