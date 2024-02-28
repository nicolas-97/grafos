import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    print("Dijkstra:")
    for node, distance in distances.items():
        print(node, distance)


aristas = [(0, 1, 2), (0, 2, 4), (1, 2, 1), (1, 3, 7), (2, 3, 3)]
graph = {}
for u, v, _ in aristas:
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, _))
    graph[v].append((u, _))
dijkstra(graph, 0)
