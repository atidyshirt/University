def dijkstras(graph, source, destination):
    n = len(graph)
    parent = [None] * n
    distance = [float('inf')] * n
    in_tree = [False] * n
    distance[source] = 0 

    while not all(in_tree):
        cur = min([node for node in graph if not in_tree[node]], key=lambda node: distance[node])
        for adj, weight in graph[cur]:
            if distance[cur] + weight < distance[adj]:
                parent[adj] = cur
                distance[adj] = distance[cur] + weight
        return distance[destination]

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
    return distance
def path_length(distance, source, destination):
    distance_array = dijkstra(distance,source)
    return distance_array[destination]

print(dijkstra([None, 0], 0, 1))