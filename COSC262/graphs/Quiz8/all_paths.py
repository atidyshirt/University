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
def all_paths(input_data, source, destination):
    """ 
        Function takes in a source and a destination
        find all the simple paths (without cycles) to
        get from source vertex to destination
    """
    solutions = []
    dfs_backtrack(adj_list, source, solutions)
    return solutions


def dfs_backtrack(input_data, candidate, output_data):
    if should_prune(candidate):
        return 
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(input_data, child_candidate, output_data)
    
def add_to_output(candidate, output_data):
    output_data.append(candidate)
    
def should_prune(candidate):
    for i in range(len(candidate) - 1):
        if candidate[i] == candidate[-1]:
            return True
    return False

def is_solution(candidate, destination):
    if type(candidate) == int:
        if candidate == destination:
            boo = True
        else:
            boo = False
    elif candidate[-1] == destination:
        boo =  True
    else:
        boo = False
    return boo

def children(candidate, input_data):
    children_candidate = []
    for i in input_data[candidate[-1]]:
        children_candidate.append(candidate + (i[0],))
    return children_candidate

triangle_graph_str = """\
U 3
0 1
1 2
2 0
"""

adj_list = adjacency_list(triangle_graph_str)
print(sorted(all_paths(adj_list, 0, 2)))
print(all_paths(adj_list, 1, 1))