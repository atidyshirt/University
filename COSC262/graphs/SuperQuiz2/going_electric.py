from collections import deque

def adjacency_list(Str):
    lines = Str.split('\n')
    header = lines[:1]
    header = str(header[0]).split(' ')
    nodes = int(header[1])
    list_of_lists = [[] for i in range(0, nodes)]
    lines = lines[1:]
    # Conditions of items
    if header[0] == 'U':
        if len(header) > 2:
            if header[2] == 'W':
                for i in range(0, len(lines) - 1):
                    element = lines[i].split(' ')
                    list_of_lists[int(element[0])].append((int(element[1]), int(element[2])))
                    list_of_lists[int(element[1])].append((int(element[0]), int(element[2])))
        else:
            for i in range(0, len(lines) - 1):
                element = lines[i].split(' ')
                list_of_lists[int(element[0])].append((int(element[1]), None))
                list_of_lists[int(element[1])].append((int(element[0]), None))

    elif header[0] == "D":
        if len(header) > 2:
            if header[2] == 'W':
                for i in range(0, len(lines) - 1):
                    element = lines[i].split(' ')
                    list_of_lists[int(element[0])].append((int(element[1]), int(element[2])))
        else:
            for i in range(0, len(lines) - 1):
                element = lines[i].split(' ')
                list_of_lists[int(element[0])].append((int(element[1]), None))
    return list_of_lists
 
def bfs_tree(adj, s):
    n = len(adj)
    state = ['U' for i in range(n)]
    parent = [None for i in range(n)]
    Q = deque()
    state[s] = 'D'
    Q.append(s)
    return bfs_loop(adj, Q, state, parent)

def bfs_loop(adj, Q, state, parent):
    while len(Q) != 0:
        u = Q.popleft()
        for v in adj[u]:
            if state[v[0]] == 'U':
                state[v[0]] = 'D'
                parent[v[0]] = u
                Q.append(v[0])
        state[u] = 'P'
    return parent

def tree_path(parent, s, t):
    if s == t:
        return s
    else:
        if parent == None or s == None or t == None or parent[t] == None:
            return "No Path"
        else:
            return (tree_path(parent, s, parent[t]), t)

def maximum_energy(city_map, depot_position):
    """ Find the maximum cost from depot position to every node in 
        the city map, so the max cost it would take to take bus from
        depot to any position in practical matters
    """ 
    all_cities = []
    results = []
    city_map = adjacency_list(city_map)

    # Grab paths through bfs
    for city in range(len(city_map)):
        all_cities.append(tree_path(bfs_tree(city_map, depot_position), depot_position, city))

    last_vertex = depot_position

    for edge in city_map[last_vertex]:
        # Fill results with costs
        for city in all_cities:
            if type(city) is int:
                if city == edge[0]:
                    results.append(edge[1])
            elif type(city) is str:
                results.append(0)
            else: 
                path = city
                for vertex in path:
                    if vertex == edge[0]:
                        results.append(edge[1]) 
    added = sum(results)   
    if added > 0:
        added = added + 1

    return added

city_map = """\
U 7 W
0 1 6
1 2 6
0 2 10
0 3 3
3 4 3
4 5 1
"""

print(maximum_energy(city_map, 0))
print(maximum_energy(city_map, 1))
print(maximum_energy(city_map, 2))
print(maximum_energy(city_map, 3))
print(maximum_energy(city_map, 4))
print(maximum_energy(city_map, 5))
print(maximum_energy(city_map, 6))