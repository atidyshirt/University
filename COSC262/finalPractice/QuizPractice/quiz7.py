def transpose(adj):
    transpose = [[] for i in range(len(adj))]
    for i in range(len(adj)):
        for node, weight in adj[i]:
            transpose[node].append((i, weight))
    return transpose

# Question 2, dependant on transpose function (from Q1)
from collections import deque
def dfs(adj_list, start):
    numOfVertices = len(adj_list)
    state = ["U"] * numOfVertices
    parent = [None] * numOfVertices
    state[start] = "D" 
    dfs_loop(adj_list, start, state, parent)
    return (parent, state)
def dfs_loop(adj_list, u, state, parent, counter=0):
    for v in adj_list[u]:
        if state[v[0]] == "U":
            state[v[0]] = "D"
            parent[v[0]] = u
            dfs_loop(adj_list, v[0], state, parent, counter+1)
    state[u] = "P"
def is_strongly_connected(adj_list):
    dfs_on_g = dfs(adj_list, 0)
    state_g = dfs_on_g[1]
    for state in state_g:
        if state == "U":
            return False
    ttt = transpose(adj_list)
    dfs_on_gT = dfs(ttt, 0)
    state_gT = dfs_on_gT[1]
    for state in state_gT:
        if state == "U":
            return False
    return True


