from collections import deque
from graphTools import dijkstra, next_vertex, adjacency_list
def path(graph, target):
    graph = adjacency_list(graph)
    parent, distance = dijkstra(graph, target)
    answer = []
    for i in range(0, len(distance)):
        if parent[i] != None:
            answer.append(i)
    return answer
g = """\
D 3
0 1
1 0
0 2
"""

print(path(g, 0))
