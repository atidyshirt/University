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

    return knapsack(capacity, weights, values, len(items))

def knapsack(capacity, weight, value, n):
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weight[i-1] <= w:
                K[i][w] = max(value[i-1] + K[i-1][w-weight[i-1]],  K[i-1][w]) 
            else:
                K[i][w] = K[i-1][w] 

    return K[n][capacity]  
# Main
# The example in the lecture notes
items = [Item(45, 3),
         Item(45, 3),
         Item(80, 4),
         Item(80, 5),
         Item(100, 8)]
print(max_value(items, 10)) 
