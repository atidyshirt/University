from collections import deque
def flatten(test_list):
    if isinstance(test_list, list):
        if len(test_list) == 0:
            return []
        first, rest = test_list[0], test_list[1:]
        return flatten(first) + flatten(rest)
    else:
        return test_list
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
    elif is_none(parent[t]) and is_none(parent[s]):
        return float('inf')
    else:
        return list((tree_path(parent, s, parent[t]), t))
def path_length(converters_info, source_format, destination_format):
    output = []
    candidate = shortest_path(converters_info, source_format, destination_format)
    if source_format == destination_format:
        state = [source_format]
    elif len(candidate) == 1:
        if int(candidate) == candidate[0]:
            if candidate == 0:
                state = float('inf')
            else:
                state = [candidate]
    else:
        state = candidate

    if type(state) is str:
        return state
    else:
        for item in state:
            if type(item) is list:
                if type(item) is str:
                    output.append(item)
                else:
                    for x in item:
                        output.append(x)
            else:
                output.append(item)
    return flatten(output)
def is_none(val):
    if val is None:
        return True
    else: return False
def shortest_path(graph_string, source, destination):
    return tree_path(bfs_tree(adjacency_list(graph_string), source), source, destination)

print(path_length([None, 0], 0, 1))
