
def adjacency_list(string):
    """ Nice implementation to generate an adj_list """
    lines = string.split('\n')
    header = lines[:1]
    lines = lines[1:]
    header = str(header[0]).split(' ')
    nodes = int(header[1])
    output = [[] for _ in range(nodes)]

    directed, weighted = check_graph(header, lines)

    for vertex in range(0, len(lines) - 1):
        edge = lines[vertex].split(" ")
        if not directed and not weighted:
            output[int(edge[0])].append((int(edge[1]), None))
            output[int(edge[1])].append((int(edge[0]), None))
        elif not directed and weighted:
            output[int(edge[0])].append((int(edge[1]), int(edge[2])))
            output[int(edge[1])].append((int(edge[0]), int(edge[2])))
        elif directed and not weighted:
            output[int(edge[0])].append((int(edge[1]), None))
        else:
            output[int(edge[0])].append((int(edge[1]), int(edge[2])))
    return output
def check_graph(header, lines):
    """ Helper function for adj_list
        this function checks a graph to see
        if it is directed and weighted
    """
    if header[0] == 'D':
        directed = True
    else:
        directed = False

    if len(header) > 2:
        weighted = True
    else: 
        weighted = False
    return directed, weighted

def distance_matrix(adj_list):
    n = len(adj_list)
    matrix = [
        [float('inf') if i != j else 0 for j in range(n)] for i in range(n)
    ]

    for vertex in range(n):
        for next_vertex, weight in adj_list[vertex]:
            matrix[vertex][next_vertex] = weight
    return matrix




""" ------------------------- BACKTRACKING PERMS -------------------------------- """
def permutations(s):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions


def dfs_backtrack(candidate, input_data, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data)

    
def add_to_output(candidate, output_data):
    output_data.append(candidate)

    
def should_prune(candidate):
    return False

def is_solution(candidate, input_data):
    if len(candidate) == len(input_data):
        boo = True
    else:
        boo = False
    return boo

def children(candidate, input_data):
    if len(input_data) == 0: 
        return [] 
    if len(input_data) == 1: 
        return [tuple(input_data)] 
    candidates = []
    input_data = list(input_data)
    for i in range(len(input_data)): 
       cand = input_data[i] 
       listx = input_data[:i] + input_data[i+1:] 
       for perm in children(candidate, listx): 
           candidates.append(tuple([cand]) + tuple(perm)) 
    return candidates

""" ------------------- BACKTRACKING ALL PATHS ----------------------------- """
def all_paths(adj_list, source, destination):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions


def dfs_backtrack(candidate, input_data, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data)

    
def add_to_output(candidate, output_data):
    output_data.append(candidate)

    
def should_prune(candidate):
    return False

def is_solution(candidate, destination):
    if destination in candidate:
        return True
    return False 

def children(candidate, input_data):
    if len(input_data) == 0: 
        return [] 
    if len(input_data) == 1: 
        return [tuple(input_data)] 
    candidates = []
    input_data = list(input_data)
    for i in range(len(input_data)): 
       cand = input_data[i] 
       listx = input_data[:i] + input_data[i+1:] 
       for perm in children(candidate, listx): 
           candidates.append(tuple([cand]) + tuple(perm)) 
    return candidates


