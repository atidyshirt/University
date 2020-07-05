def dfs_backtrack(candidate, input, output): 
    if is_solution(candidate, input):
        add_to_output(candidate, output) 
    else:
        for child_candidate in children(candidate): 
            dfs_backtrack(child_candidate, input, output)

def is_solution(candidate, desired_length): 
    return len(candidate) == desired_length

def children(candidate):
    return [candidate + "0", candidate + "1"]

def add_to_output(candidate, output): 
    output.append(candidate)

def binary_numbers(desired_length): 
    solutions = []
    dfs_backtrack("", desired_length, solutions) 
    return solutions

print(binary_numbers(3))