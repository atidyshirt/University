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
    table = [[0]*(capacity+1) for i in range(len(items)+1)]
    for i in range(1, len(items)+1):
        active_item = items[i-1]
        for j in range(1, capacity + 1):
            if j >= active_item.weight:
                table[i][j] = max(table[i-1][j], table[i-1][j-active_item.weight] + active_item.value)
            else:
                table[i][j] = table[i-1][j]

    list_of_items = []
    i, j = len(items), capacity
    while i != 0 and j != 0:
        if table[i][j] != table[i-1][j]:
            list_of_items.append(items[i-1])
            j -= items[i-1].weight
        i -= 1

    return (table[-1][-1], list_of_items)
def lcs_numerical(s1, s2):
    cache = {}
    def aux(i, j):
        if (i, j) in cache:
            return cache[(i, j)]
        elif i == 0 or j == 0:
            return []
        elif s1[i - 1] == s2[j - 1]:
            m = aux(i - 1, j) + [s1[i-1]]
            cache [(i, j)] = m
            return m
        else:
            m = max([aux(i - 1, j), aux(i, j - 1)], key=len)
            cache [(i, j)] = m
            return m
    return aux(len(s1), len(s2))
def lcs_string(s1, s2):
    cache = {}
    def aux(i, j):
        if (i, j) in cache:
            return cache[(i, j)]
        elif i == 0 or j == 0:
            return []
        elif s1[i - 1] == s2[j - 1]:
            m = aux(i - 1, j) + [s1[i-1]]
            cache [(i, j)] = m
            return m
        else:
            m = max([aux(i - 1, j), aux(i, j - 1)], key=len)
            cache [(i, j)] = m
            return m
    return "".join(aux(len(s1), len(s2))) 


s1 = [1,5,6,4,3,2] 
s2 = [1,2,3]
lcs = lcs_numerical(s1, s2)
print(lcs)
