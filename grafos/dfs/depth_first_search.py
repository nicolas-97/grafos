def dfs(graph, node, visited):
    if node not in visited:
        visited.add(node)
        for neighbor, _ in graph[node]:
            dfs(graph, neighbor, visited)


aristas = [(0, 1, 2), (0, 2, 4), (1, 2, 1), (1, 3, 7), (2, 3, 3)]
graph = {}
for u, v, _ in aristas:
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, _))
    graph[v].append((u, _))

dfs_visited = set()
dfs(graph, 0, dfs_visited)
print()
