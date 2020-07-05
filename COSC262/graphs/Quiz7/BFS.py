from collections import deque

""" PREVIOUS REQUIRED FUNCTIONS """
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

""" CURRENT FUNCTION - WORKING """
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
    print(parent)
    return parent

""" TEST CASES """
graph_string = """\
U 4
0 1
0 2
0 3
1 2
1 3
"""
print(bfs_tree(adjacency_list(graph_string), 1))
