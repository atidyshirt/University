from math import inf

def next_vertex(in_tree, distance):
    parent = 0
    for vertex in range(len(distance)):
        if distance[vertex] == 0:
            parent = vertex
    current_min = (float('inf'), None)
    for vertex in range(len(distance)):
        if distance[vertex] <= current_min[0] and in_tree[vertex] == False:
            current_min = distance[vertex], vertex
    return current_min[1]
