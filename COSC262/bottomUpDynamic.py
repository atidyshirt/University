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
    table = [[-1 for i in range(n_cols)] for i in range(n_rows)]
    table[0] = grid[0]
    counter = 0
    for row in table:
        count = 0
        for item in row:
            if item == -1:
                if count == 0:
                    table[counter][count] = grid[counter][count] + min(table[counter - 1][count], table[counter - 1][count + 1])
                elif count == (n_cols - 1):
                    table[counter][count] = grid[counter][count] + min(table[counter - 1][count], table[counter - 1][count - 1])
                else:
                    table[counter][count] = grid[counter][count] + min(
                        table[counter - 1][count], table[counter - 1][count - 1], table[counter - 1][count + 1])
            count += 1
        counter += 1


    return min(table[-1])
    
    
def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))

print(file_cost('file.txt'))
