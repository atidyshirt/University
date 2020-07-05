""" CURRENT WORKING FUNCTION """
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
 

def adjacency_list_harrys(graph_str):
    graph_lst = graph_str.splitlines()
    data_line = graph_lst[0]
    return_lst = [[] for vertex in range(int(data_line.split(' ')[1]))]
    strings = []
    for ints in range(1, len(graph_lst)):
        strings.append(graph_lst[ints].split(" "))
    graph_ints = []
    for item in strings:
        test = []
        for abc in item:
            test.append(int(abc))
        graph_ints.append(test)
    weighted = False
    directed = True
    if data_line[-1] == "W":
        weighted = True
    if data_line[0] == "U":
        directed = False
    for vertex in range(len(graph_ints)):
        if directed == True:
            if weighted == False:
                return_lst[graph_ints[vertex][0]].append((graph_ints[vertex][1], None))
            else:
                return_lst[graph_ints[vertex][0]].append((graph_ints[vertex][1], (graph_ints[vertex][-1])))
        else:
            if weighted == False:
                return_lst[graph_ints[vertex][0]].append((graph_ints[vertex][1], None))
                return_lst[graph_ints[vertex][1]].append((graph_ints[vertex][0], None))
            else:
                return_lst[graph_ints[vertex][0]].append((graph_ints[vertex][1], (graph_ints[vertex][-1])))
                return_lst[graph_ints[vertex][1]].append((graph_ints[vertex][0], (graph_ints[vertex][-1])))
    return return_lst
""" TEST CASES """
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
print(adj_list)
