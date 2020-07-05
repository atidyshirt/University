from graphTools import *

def path_length(parent, s, t):
    if s == t:
        return s 
    elif is_none(parent[t]) and is_none(parent[s]):
        return float('inf')
    else: 
        return len(list(path_length(parent, s, parent[t]))), t

def is_none(val):
    if val is None:
        return True
    else: return False

#print(path_length([None, 0], 0, 1))
#print(path_length([None, None], 0, 0))
#print(path_length([None, None], 0, 1))
#print(path_length([None, 2, 3, None, 3, 4], 3, 5))
print(path_length([None, 0, 1, 2, 3], 0, 4))