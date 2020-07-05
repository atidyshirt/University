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
def print_shows(show_list):
    ends = []
    for show in show_list:
        speaker, start_time, duration = show
        ends.append((start_time + duration, start_time, speaker))
    ends.sort()
    duration = 0
    
    for item in ends:
        if duration <= item[1]:
            print("{}, {}, {}".format(item[2], item[1], item[0]))
            duration = item[0]
def fractional_knapsack(capacity, items):
    #Items = (name, weight, value) just return total value
    result = 0
    for item in sorted(items, key=lambda item: (item[1]/item[2]), reverse=True):
        if capacity == 0:
            break
        elif capacity >= item[2]:
            result += item[1]
            capacity -= item[2]
        else:
            result += item[1] * (capacity / item[2])
            capacity = 0
    return result


""" HUFFMAN TREE QUESTIONS FOR QUIZ 3"""
