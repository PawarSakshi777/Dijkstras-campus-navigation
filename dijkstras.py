import heapq

def dijkstra(graph, start, end):

    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    prev = {node: None for node in graph}  # to store path
    pq = [(0, start)]  # priority queue (distance, node)

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = prev[current]

    return dist[end], path

graph = {}
n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

print("Enter edges in format: u v w")
for _ in range(m):
    u, v, w = input().split()
    w = int(w)
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, w))
    graph[v].append((u, w))  

source = input("Enter source vertex: ")
dest = input("Enter destination vertex: ")

distance, path = dijkstra(graph, source, dest)

print("\nShortest Path:", " → ".join(path))
print("Total Distance:", distance)
