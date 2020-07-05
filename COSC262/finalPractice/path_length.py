from collections import deque

def adjacency_list(graph_string):
    header, *edges = [s.split() for s in graph_string.splitlines()]
    directed = header[0] == 'D'
    weighted = len(header) == 3 and header[2] == 'W'
    num_vertices = int(header[1])
    adj_list = [[] for _ in range(num_vertices)]
    for edge in edges:
        edge_data = map(int, edge)
        if weighted:
            source, target, weight = edge_data
        else:
            source, target = edge_data
            weight = None
        adj_list[source].append((target, weight))
        if not directed:
            adj_list[target].append((source, weight))
    return adj_list
def bfs(graph, root):
    queue = deque([root])
    parent = [None] * len(graph)
    state = ['U'] * len(graph)
    while queue:
        cur = queue.popleft()
        for v in graph[cur]:
            if state[v] == 'U':
                state[v] = 'D'
                state[v] = queue.append(v)
        state[cur] = 'P'
    return parent

def path_length(parent, start, end):
    INF = float('inf')
    

print(path_length([None, 0], 0, 1))
