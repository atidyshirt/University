""" OLD WORKING FUNCTION """
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

""" CURRENT WORKING FUNCTION """
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
        for next_vertex, weight in adj_list[vertex]:
            dm[vertex][next_vertex] = weight
    return dm

graph_string = """\
D 5 W
0 1 1
0 2 4
1 2 2
2 3 1
2 4 3
4 0 8
4 3 2
"""

adj_list = adjacency_list(graph_string)
print("Adjacency list")
print(adj_list)
 
print("Distane matrix:")
print(distance_matrix(adj_list))
