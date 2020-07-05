"""
   _____                 _       _______          _     
  / ____|               | |     |__   __|        | |    
 | |  __ _ __ __ _ _ __ | |__      | | ___   ___ | |___ 
 | | |_ | '__/ _` | '_ \| '_ \     | |/ _ \ / _ \| / __|
 | |__| | | | (_| | |_) | | | |    | | (_) | (_) | \__ \
  \_____|_|  \__,_| .__/|_| |_|    |_|\___/ \___/|_|___/
                  | |                                   
                  |_|                                
"""

""" GENERATING AN ADJACENCY LIST """
def adjacency_list_without_check(string):
    """ Nice implementation to generate an adj_list """
    lines = string.split('\n')
    header = lines[:1]
    lines = lines[1:]
    header = str(header[0]).split(' ')
    nodes = int(header[1])
    output = [[] for _ in range(nodes)]

    directed, weighted = check_graph(header, lines)

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
def check_graph(header, lines):
    """ Helper function for adj_list
        this function checks a graph to see
        if it is directed and weighted
    """
    if header[0] == 'D':
        directed = True
    else:
        directed = False
        
    if len(header) > 2:
        weighted = True
    else: 
        weighted = False
    return directed, weighted

    """ just a test case for this function
        becuase then I can put all my stuff
        in a single file
    """
    graph_string = """\
    D 3
    0 1
    1 0
    0 2
    """
    print(adjacency_list(graph_string))

""" RETURNING PARENT ARRAY WITH BFS """ 
from collections import deque
def adjacency_list(string):
    """ generates an adj_list when given a string in correct
        format
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
def bfs(adj, s):
    """ Initilised arrays and queue, starts bfs loop on starting node, returns the parent array
    """
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
    while len(Q) != 0:
        u = Q.popleft()
        for v in adj[u]:
            if state[v[0]] == 'U':
                state[v[0]] = 'D'
                parent[v[0]] = u
                Q.append(v[0])
        state[u] = 'P'
    return parent

""" RETURNING PARENT ARRAY WITH DFS """
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
def dfs(adj, s):
    n = len(adj)
    state = ['U' for i in range(n)]
    parent = [None for i in range(n)]
    state[s] = 'D'
    dfs_loop(adj, s, state, parent)
    return parent
def dfs_loop(adj, u, state, parent):
    for v in adj[u]:
        if state[v[0]] == 'U':
            state[v[0]] = 'D'
            parent[v[0]] = u
            dfs_loop(adj, v[0], state, parent)
    state[u] = 'P'

""" TRANSPOSING A GRAPH """
def adjacency_list(string):
    """ generates an adj_list when given a string in correct
        format
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
def transpose(adj):
    transpose_graph = [[] for i in range(0, len(adj))]
    count = -1
    for vertex in adj:
        count += 1
        for node in vertex:
            transpose_graph[count].append((node[0], node[1]))
    return transpose_graph

""" FINDING SHORTEST PATH FROM POINT S - X """
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
def bfs(adj, s):
    """ Initilised arrays and queue, starts bfs loop on starting node, returns the parent array
    """
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
    while len(Q) != 0:
        print(Q, parent, state)
        u = Q.popleft()
        for v in adj[u]:
            print(Q)
            print(state)
            print(parent)
            if state[v[0]] == 'U':
                state[v[0]] = 'D'
                parent[v[0]] = u
                Q.append(v[0])
        state[u] = 'P'
    return parent
def shortest_path(graph, source, destination):
    """ Takes in a graph string and returns shortest path """
    def tree_path(parent, s, t):
        """ returns path from s, t """ 
        result.append(t)
        if s == t:
            return result
        else:
            return tree_path(parent, s, parent[t])
    result = []
    tree_path(bfs(graph, source), source, destination)
 
    return tuple(result)

""" FINDING A VALID TOPOLOGICAL ORDERING OF GRAPH """
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
def dfs_loop_topological(listx, u, state, stack):
        state[u] = "P"
        for v in listx[u]:
            if state[v[0]] == "U":
                dfs_loop(listx, v[0], state, stack)
        stack.append(u)
def topological_ordering(info):
    """ Returns a valid topological ordering, note that a topological
        ordering is the reverse of the final stack, if asked to return
        the stack, give opposite of topological ordering 
    """
    n = len(info)
    state = ["U" for _ in range(n)]
    parent = [None for _ in range(n)]
    stack = []
    for i in range(0, n):
        if state[i] == "U":
            dfs_loop_topological(info, i, state, stack)
    return stack[::-1]


""" Generating a Distance Matrix from Adjacency list """
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

""" Floyds Algorithm - good solution if negitive edges """
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
        # For index in row
        for i in range(0, n):
            # For index in column
            for j in range(0, n):
                print(distance[i][j], "(", i, j, k, ")")
                # Check that is never ever satisfied
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                print(distance[i][j], "(", i, j, k, ")")
    return distance

""" FINDING NEXT VERTEX """
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

""" DIJKSTRAS ALGORITHM RETURNING DISTACNE, PARENT """
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
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if in_tree[v] != True and (distance[u] + weight) < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
    return (parent, distance)

""" Strong Connectivity """
from collections import deque
def transpose(adj_list):
    transpose = [[] for i in range(len(adj_list))]
    for i in range(len(adj_list)):
        for node, weight in adj_list[i]:
            transpose[node].append((i, weight))
    return transpose
def dfs_tree(adj_list, start):
    numOfVertices = len(adj_list)
    state = ["U"] * numOfVertices
    parent = [None] * numOfVertices
    state[start] = "D"
    dfs_loop(adj_list, start, state, parent)
    return (parent, state)
def dfs_loop(adj_list, u, state, parent):
    for v in adj_list[u]:
        if state[v[0]] == "U":
            state[v[0]] = "D"
            parent[v[0]] = u
            dfs_loop(adj_list, v[0], state, parent)
    state[u] = "P"
def strongly_connected(adj_list):
    dfs_on_g = dfs_tree(adj_list, 0)
    state_g = dfs_on_g[1]
    for state in state_g:
        if state == "U":
            return False
    ttt = transpose(adj_list)
    dfs_on_gT = dfs_tree(ttt, 0)
    state_gT = dfs_on_gT[1]
    for state in state_gT:
        if state == "U":
            return False
    return True

