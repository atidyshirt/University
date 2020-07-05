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

def dfs_loop(listx, u, state, stack):
        state[u] = "P"
        for v in listx[u]:
            if state[v[0]] == "U":
                dfs_loop(listx, v[0], state, stack)
        stack.append(u)

def starting_order(dependencies):
    info = adjacency_list(dependencies)
    n = len(info)
    state = ["U" for _ in range(n)]
    parent = [None for _ in range(n)]
    stack = []
    for i in range(n):
        if state[i] == "U":
            dfs_loop(info, i, state, stack)
    return stack[::-1]

dependencies = """\
D 7
6 0
6 5
0 1
0 2
1 2
1 3
2 4
2 5
4 3
5 4
"""
print(starting_order(dependencies))