# Smart Campus Navigation (Dijkstras Algorithm)
DIJKSTRA(G, s):
  for each vertex v in V:
      dist[v] ← ∞
      prev[v] ← NIL
  dist[s] ← 0
  Q ← V

  while Q ≠ ∅:
      u ← vertex in Q with min dist[u]
      remove u from Q
      for each neighbor v of u:
          if dist[u] + w(u,v) < dist[v]:
              dist[v] ← dist[u] + w(u,v)
              prev[v] ← u

## 📌 About
This project finds the shortest path between two locations using Dijkstra’s Algorithm.
It can be applied to student campuses, hostels, or city navigation.

## 🛠 How to Run
1. Clone this repo:
   ```bash
    https://github.com/pawarsakshi777/dijkstra-campus-navigation.git
# Dijkstras-campus-navigation
