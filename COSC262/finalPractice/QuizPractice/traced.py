from traces import adjacency_list, dfs, dfs_loop
g = """\
U 8 W
1 3 2
0 6 7
2 5 5
2 7 1
4 6 2
5 7 3
"""
graph = adjacency_list(g)
print(dfs(graph, 5))


