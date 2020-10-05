""" from quiz 1 """
def almost_all(numbers, n=-1):
    "Only sums numbers once"
    if n == -1:
        n = sum(numbers)
    return [n - x for x in numbers]

def sort_of(numbers):
    result = []
    for i in range(len(numbers)):
        sub = sorted(numbers[i:])
        result.append(sub[0])
    return result

def concat_list(list_of_strings, res = ""):
    if len(list_of_strings) == 0:
        return res
    else:
        res = res + list_of_strings[0]
        return concat_list(list_of_strings[1:], res)

def product(data, total=1):
    if len(data) == 0:
        return total
    else:
        total *= data[-1]
        return product(data[:-1], total)

def backwards(s):
    if len(s) <= 1:
        return s
    else:
        return backwards(s[1:]) + s[0]

def odds(nums):
    if len(nums) <= 0:
        return []
    elif nums[0] % 2 != 0:
        return [nums[0]] + odds(nums[1:])
    else:
        return odds(nums[1:])

def squares(nums):
    if len(nums) <= 0:
        return []
    else:
        return [(nums[0]**2)] + squares(nums[1:])

def find(data, value):
    if len(data) <= 0:
        return 1
    elif value == data[0]:
        return find(data[1:], value) + 1
    else:
        return find(data[1:], value)

""" from quiz 2 """
def cycle_length(start, count=0):
    if start == 1:
        return count + 1
    elif start % 2 == 0:
        return cycle_length((start / 2), count+1)
    else:
        return cycle_length((3 * start + 1), count+1)

def recursive_divide(x, y):
    if x - y == 0:
        return 1
    elif x - y < 0:
        return 0
    else:
        return 1 + recursive_divide(x-y, y)

def my_enumerate(items, counter=0):
    if len(items) < 1:
        return []
    else:
        tup = (counter, items[0])
        items.pop(0)
        return [tup] + my_enumerate(items, counter+1)

def num_rushes(height, height_gain, back_slide, counter=0):
    if height_gain >= height:
        return counter
    else:
        return num_rushes(height-height_gain+back_slide, height_gain*0.95, back_slide*0.95, counter+1)

def dumbo_func(data, i=0):
    """Takes a list of numbers and does weird stuff with it"""
    if i >= len(data):
        return 0
    else:
        c = dumbo_func(data, i + 1)
        if (data[i] // 100) % 3 != 0:
            c += 1
        return c
#need both the following functions to get all pairs

def all_pairs(list1, list2, i=0):
    if i >= len(list1):
        return []
    return all_pairs_inner(list1[i], list2) + all_pairs(list1, list2, i + 1)
def all_pairs_inner(number, list2, i=0):
    if i >= len(list2):
        return []
    return [(number, list2[i])] + all_pairs__inner(number, list2, i + 1)

""" from quiz 3 """
from collections import defaultdict # for greedy change
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

""" from quiz 4 """
# Top Down Solution
INFINITY = float('inf')
def top_read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers.
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()
    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid
def top_grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given
       grid of integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    cache = {}
    def top_cell_cost(row, col):
        """The cost of getting to a given cell in the current grid."""
        if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
            return INFINITY  # Off-grid cells are treated as infinities
        else:
            if (row, col) in cache:
                return cache[(row, col)]
            cost = grid[row][col]
            if row != 0:
                cost += min(cell_cost(row - 1, col + delta_col) for delta_col in range(-1, 2))
                cache[(row, col)] = cost
        return cost
    best = min(cell_cost(n_rows - 1, col) for col in range(n_cols))
    return best


def lcs_numerical(s1, s2): # input: {[1,3,4,3,2], [1,2,3,9,8]} >> output: {1,2,3}
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

def lcs_string(s1, s2): # input: 'world', 'wrong' >> output: ['w', 'r', 'o']
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

