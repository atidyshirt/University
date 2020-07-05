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
    return len(candidate) == len(input_data)
        
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

print(sorted(permutations({1,2,3})))
print(sorted(permutations({'a'})))
perms = permutations(set())
print(len(perms) == 0 or list(perms) == [()])