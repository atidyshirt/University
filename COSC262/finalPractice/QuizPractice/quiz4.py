"""Minimum cost section"""

"""A broken implementation of a recursive search for the optimal path through
   a grid of weights.
   Richard Lobb, January 2019.
"""
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
def top_file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))

""" Next Question """

""" Bottom up approach, the one above is top down """



"""A program to read a grid of weights from a file and compute the 
   minimum cost of a path from the top row to the bottom row
   with the constraint that each step in the path must be directly
   or diagonally downwards. 
   This question has a large(ish) 200 x 200 grid and you are required
   to use a bottom-up DP approach to solve it.
"""
INFINITY = float('inf')  

def read_grid(filename):
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
def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given grid of
       integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    
    # **** Your code goes here. It must compute a value 'best', which is
    # the minimum cost from the top of the grid to the bottom.
    table =  [[-1 for _ in range(n_cols)] for x in range(n_rows)]
    table[0] = grid[0]

    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == -1:
                table[i][j] = grid[i][j] + min(table[i-1][j], table[i-1][j+1])
            elif j == (n_cols - 1):
                table[i][j] = grid[i][j] + min(table[i - 1][j], table[i - 1][j - 1])
            else:
                table[i][j] = grid[i][j] + min(table[i - 1][j], table[i - 1][j - 1], table[i - 1][j + 1])

    return min(table[-1]) + 1
def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))

""" NEXT QUESTION - Not impleemnted """
def coins_reqd(value, coinage):
    """A version that doesn't use a list comprehension"""
    numCoins = [0] * (value + 1)
    for amt in range(1, value + 1):
        minimum = None
        for c in coinage:
            if amt >= c:
                coin_count = numCoins[amt - c]  # Num coins required to solve for amt - c
                if minimum is None or coin_count < minimum:
                    minimum = coin_count
        numCoins[amt] = 1 + minimum
    return numCoins[value]
"""finding max value"""
import sys
sys.setrecursionlimit(2000)

class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"
def max_value(items, capacity):
    cache = {}
    def rec(n, capacity):
        if n <= 0 or capacity <= 0:
            return 0

        if (n, capacity) in cache:
            return cache[(n, capacity)]

        if items[n-1].weight <= capacity:
            total = max(items[n-1].value + rec(n-1, capacity - items[n-1].weight), rec(n-1, capacity))
            cache[(n, capacity)] = total

        else:
            total = rec(n-1, capacity)

        return total

    return rec(len(items), capacity)

