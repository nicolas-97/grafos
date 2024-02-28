from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                
aristas = [(0, 1, 2), (0, 2, 4), (1, 2, 1), (1, 3, 7), (2, 3, 3)]
graph = {}
for u, v, _ in aristas:
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, _))
    graph[v].append((u, _))


bfs(graph, 0)

