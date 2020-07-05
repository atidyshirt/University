def adjacency_list(string):
    """ generates an adj_list when given a string in correct format
    """
    lines = string.split('\n')
    header = lines[:1]
    lines = lines[1:]
    header = str(header[0]).split(' ')
    nodes = int(header[1])
    output = [[] for _ in range(nodes)]
    # Check if graph is directed and weighted
    if header[0] == 'D':
        directed = True
    else:
        directed = False
        
    if len(header) > 2:
        weighted = True
    else: 
        weighted = False
    # Generates output based on info above
    for vertex in range(0, len(lines) - 1):
        edge = lines[vertex].split(" ")
        if not directed and not weighted:
            output[int(edge[0])].append((int(edge[1]), None))
            output[int(edge[1])].append((int(edge[0]), None))
        elif not directed and weighted:
            output[int(edge[0])].append((int(edge[1]), int(edge[2])))
            output[int(edge[1])].append((int(edge[0]), int(edge[2])))
        elif directed and not weighted:
            output[int(edge[0])].append((int(edge[1]), None))
        else:
            output[int(edge[0])].append((int(edge[1]), int(edge[2])))
    return output
from collections import deque

""" Returns a trace of dfs """
def dfs(adj_list, start):
    """ Prints steps of dfs """
    numOfVertices = len(adj_list)
    state = ["U"] * numOfVertices
    parent = [None] * numOfVertices
    state[start] = "D" 
    dfs_loop(adj_list, start, state, parent)
    return (parent, state)
def dfs_loop(adj_list, u, state, parent, counter=0):
    print("Recursion", counter, ":", state, parent)
    for v in adj_list[u]:
        if state[v[0]] == "U":
            state[v[0]] = "D"
            parent[v[0]] = u
            dfs_loop(adj_list, v[0], state, parent, counter+1)
    state[u] = "P"

""" Returns a full trace of bfs """
def bfs(adj, s):
    """ Prints steps of BFS """
    n = len(adj)
    state = ['U' for i in range(n)]
    parent = [None for i in range(n)]
    Q = deque()
    state[s] = 'D'
    Q.append(s)
    return bfs_loop(adj, Q, state, parent)
def bfs_loop(adj, Q, state, parent):
    """ Runs bfs on remaining nodes until 'Q' is empty
    """
    counter = 0
    while len(Q) != 0:
        counter += 1
        print("Loop ", counter, ':', Q, parent, state)
        u = Q.popleft()
        for v in adj[u]:
            if state[v[0]] == 'U':
                state[v[0]] = 'D'
                parent[v[0]] = u
                Q.append(v[0])
        state[u] = 'P'
    return parent

""" Returns a full trace of dijkstra's """
def next_vertex(in_tree, distance):
    """ Function to find the next lowest value """
    parent = 0
    mini = (float('inf'), None)
    for vertex in range(len(distance)):
        if distance[vertex] == 0:
            parent = vertex    
    for vertex in range(len(distance)):
        if distance[vertex] <= mini[0] and in_tree[vertex] == False:
            mini = distance[vertex], vertex
    return mini[1]

def dijkstra(adj_list, start):
    """ Function that implements dijkstras algorithm to find
        shortest path to visit all vertexes
    """
    INF = float('inf')
    n = len(adj_list)
    in_tree = [False for i in range(n)]
    distance = [INF for i in range(n)]
    parent = [None for i in range(n)]
    distance[start] = 0
    while all(in_tree) != True:
        u = next_vertex(in_tree, distance)
        print("Distance: ", distance, "Parent: ", parent, "In Tree: ", in_tree, '\t', "Next Vertex: ", u)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if in_tree[v] != True and (distance[u] + weight) < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
    return (parent, distance)

""" Trace of floyds algorithm """
def distance_matrix(adj):
    n = len(adj)
    dm = [
            [float('inf')
            if i != j
            else 0 
            for j in range(n)] 
            for i in range(n)
        ]

    for vertex in range(n):
        for next_vertex, weight in adj[vertex]:
            dm[vertex][next_vertex] = weight
    return dm
def floyd(distance):
    n = len(distance)
    # For node in range(a - x)
    for k in range(0, n):
        print("K = ", k, "Distance: ", distance)
        # For index in row
        for i in range(0, n):
            # For index in column
            for j in range(0, n):
                # printing the sequence
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance

""" Trace of Prims algorithm """
def prims(adj_list, start):
    """ Function that implements dijkstras algorithm to find
        shortest path to visit all vertexes
    """
    INF = float('inf')
    n = len(adj_list)
    in_tree = [False for i in range(n)]
    distance = [INF for i in range(n)]
    parent = [None for i in range(n)]
    distance[start] = 0
    while all(in_tree) != True:
        u = next_vertex(in_tree, distance)
        print("Distance: ", distance, "Parent: ", parent, "In Tree: ", in_tree, '\t', "Next Vertex: ", u)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if in_tree[v] != True and (distance[u] + weight) < distance[v]:
                distance[v] = weight
                parent[v] = u
    return (parent, distance)

