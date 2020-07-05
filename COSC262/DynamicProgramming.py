"""A broken implementation of a recursive search for the optimal path through
   a grid of weights.
   Richard Lobb, January 2019.
"""

INFINITY = float('inf')

def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers. (across)
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid

def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given
       grid of integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    cache = {}

    def cell_cost(row, col):
        """The cost of getting to a given cell in the current grid."""
        if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
            return INFINITY  # Off-grid cells are treated as infinities
        else:
            if (row, col) in cache:
                #print("working")
                return cache[(row, col)]
            else:
                cost = grid[row][col]
                if row != 0:
                    cost += min(cell_cost(row - 1, col + delta_col) for delta_col in range(-1, 2))
                    cache[(row, col)] = cost
            return cost
    # the lowest cost cell out of the cell_cost() function
    best = min(cell_cost(n_rows - 1, col) for col in range(n_cols))
    return best

def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))

print(file_cost("file.txt"))
print(file_cost("checksmall"))
print(file_cost("checkmed"))
