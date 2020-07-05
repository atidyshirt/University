print()
print("-------------------------------------------------")
print("Question Two")
print()

#Question Two
from collections import defaultdict
def change_greedy(exact, coins, counter=0):
    coins_count = defaultdict(int)

    while exact != 0:
        counter = 0
        for i in reversed(sorted(coins)):
            counter += 1
            if exact >= i:
                exact = exact - i
                coins_count[i] += 1
                break
            if counter >= len(coins):
                return None
    return [(k, v) for v, k in coins_count.items()]

print(change_greedy(82, [1, 10, 25, 5]))
print(change_greedy(80, [1, 10, 25]))
print(change_greedy(82, [10, 25, 5]))

print()
print("-------------------------------------------------")
print("Question Six")
print()

#Question Six
def fractional_knapsack(max_weight, items):
    length = len(items)
    for i in range(0, length):
            for j in range(0, length-i-1):
                if (items[j][1] > items[j + 1][1]):
                    temp = items[j]
                    items[j] = items[j + 1]
                    items[j + 1] = temp
    return items

items = [
    ("Chocolate cookies", 20, 5),
    ("Potato chips", 15, 3),
    ("Pizza", 14, 2),
    ("Popcorn", 12, 4)]
print(fractional_knapsack(9, items))

print()
print("-------------------------------------------------")
print()

