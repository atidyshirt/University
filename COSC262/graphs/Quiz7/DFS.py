""" PREVIOUS FUNCTIONS REQUIRED """
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

""" DFS FUNCTIONS WORKING """
def dfs_tree(adj, s):
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

""" TEST CASES  """
# graph from the textbook example
graph_string = """\
U 5
0 1
1 2
1 3
3 4
4 0
"""
print(dfs_tree(adjacency_list(graph_string), 4))