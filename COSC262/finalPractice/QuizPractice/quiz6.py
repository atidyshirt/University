""" Quiz 6 practice for final """

# Grabbing tools for adjacency matrix ect
from graphTools import *
#from traces import bfs, dfs

g = """\
U 4
0 1
0 2
0 3
1 2
1 3
"""

print(dfs(adjacency_list(g), 0))
