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

def bfs(adj, s):
    
    n = len(adj)
    state = ['U' for i in range(n)]
    parent = [None for i in range(n)]
    Q = deque()
    state[s] = 'D'
    Q.append(s)
    return bfs_loop(adj, Q, state, parent)
def bfs_loop(adj, Q, state, parent):
    visited_nodes = set()
    visited_nodes.add(Q[0])
    counter = 0
    while len(Q) != 0:
        u = Q.popleft()
        for v in adj[u]:
            if state[v[0]] == 'U':
                state[v[0]] = 'D'
                parent[v[0]] = u
                Q.append(v[0])
                visited_nodes.add(v[0])
        
        state[u] = 'P'
    return visited_nodes

def bubbles(physical_contact_info):
    listx = adjacency_list(physical_contact_info)
    visited = set()
    answer = []
    for i in range(0, len(listx)):
        if i not in visited:
            next_visit = bfs(listx, i)
            visited = visited.union(next_visit)
            answer.append(list(next_visit))
    return answer
    


physical_contact_info = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))