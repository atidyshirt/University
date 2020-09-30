#   -----------------------------------------------------------------
#   Question Four
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

#  print_shows([
    #  ('a', 0, 6),
    #  ('b', 1, 3),
    #  ('c', 3, 2),
    #  ('d', 3, 5),
    #  ('e', 4, 3),
    #  ('f', 5, 4),
    #  ('g', 6, 4),
    #  ('h', 8, 3)])
#   END Q4
#   -----------------------------------------------------------------

def fractional_knapsack(capacity, items):
    """
        takes list of input, and max capacity for bag, creates new list with value ratio, value and weight
        returns the total value that we can get with the associated capacity
    """
    alist = []
    for item in items:
        value = item[1]
        weight = item[2]
        alist.append((value / weight, value, weight))

    alist.sort()
    total = 0
    for item in reversed(alist):
        if capacity == 0:
            break
        elif capacity >= item[2]:
            total += item[1]
            capacity -= item[2]
        else:
            total += item[1] * (capacity / item[2])
            capacity = 0
    return total

# The example from the lecture notes
items = [
    ("Chocolate cookies", 20, 5),
    ("Potato chips", 15, 3),
    ("Pizza", 14, 2),
    ("Popcorn", 12, 4)]
print(fractional_knapsack(9, items))
