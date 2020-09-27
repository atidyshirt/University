from collections import deque


def adjacency_list(Str):
    lines = Str.split("\n")
    header = lines[:1]
    header = str(header[0]).split(" ")
    nodes = int(header[1])
    list_of_lists = [[] for _ in range(0, nodes)]
    lines = lines[1:]
    # Conditions of items
    if header[0] == "U":
        if len(header) > 2:
            if header[2] == "W":
                for i in range(0, len(lines) - 1):
                    element = lines[i].split(" ")
                    list_of_lists[int(element[0])].append(
                        (int(element[1]), int(element[2]))
                    )
                    list_of_lists[int(element[1])].append(
                        (int(element[0]), int(element[2]))
                    )
        else:
            for i in range(0, len(lines) - 1):
                element = lines[i].split(" ")
                list_of_lists[int(element[0])].append((int(element[1]), None))
                list_of_lists[int(element[1])].append((int(element[0]), None))

    elif header[0] == "D":
        if len(header) > 2:
            if header[2] == "W":
                for i in range(0, len(lines) - 1):
                    element = lines[i].split(" ")
                    list_of_lists[int(element[0])].append(
                        (int(element[1]), int(element[2]))
                    )
        else:
            for i in range(0, len(lines) - 1):
                element = lines[i].split(" ")
                list_of_lists[int(element[0])].append((int(element[1]), None))
    return list_of_lists


def bfs_tree(adj, s):
    n = len(adj)
    state = ["U" for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = deque()
    state[s] = "D"
    Q.append(s)
    return bfs_loop(adj, Q, state, parent)


def bfs_loop(adj, Q, state, parent):
    while len(Q) != 0:
        u = Q.popleft()
        for v in adj[u]:
            if state[v[0]] == "U":
                state[v[0]] = "D"
                parent[v[0]] = u
                Q.append(v[0])
        state[u] = "P"
    return parent


def tree_path(parent, s, t):
    if s == t:
        return s
    else:
        return (tree_path(parent, s, parent[t]), t)


def next_vertex(in_tree, distance):
    parent = 0
    for vertex in range(len(distance)):
        if distance[vertex] == 0:
            parent = vertex
    current_min = (float("inf"), 0)
    for vertex in range(len(distance)):
        if distance[vertex] <= current_min[0] and in_tree[vertex] == False:
            current_min = distance[vertex], vertex
    return current_min[1]


def which_walkways(campus_map):
    info = adjacency_list(campus_map)
    n = len(info)
    in_path = [False for _ in range(n)]
    distance = [float("inf") for _ in range(n)]
    parent = [None for _ in range(n)]
    ans = []
    distance[0] = 0
    while not all(in_path) == True:
        u = next_vertex(in_path, distance)
        in_path[u] = True
        for v, weight in info[u]:
            if in_path[v] == False and weight < distance[v]:
                distance[v] = weight
                parent[v] = u
    for i in range(1, len(parent)):
        ans.append((min(parent[i], i), max(parent[i], i)))
    return ans


campus_map = """\
U 3 W
0 1 1
2 1 2
2 0 4
"""

print(sorted(which_walkways(campus_map)))
