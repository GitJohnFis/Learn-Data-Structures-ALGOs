# Learn-Data-Structures-ALGOs


<img width="343" alt="VVZYCm4" src="https://github.com/user-attachments/assets/195484e1-71ca-4c6d-a6bf-217f49b97941" />

## Representing a Graph in Code

We'll primarily be using an adjacency list to work with graphs. For each vertex in the graph, it stores a set of all the vertices connected to that vertex.

| Vertex | Connects with      |
|--------|--------------------|
| 0      | 1, 4               |
| 1      | 0, 2, 3, 4         |
| 2      | 1, 3               |
| 3      | 1, 2, 4            |
| 4      | 0, 1, 3            |


# Dijkstra's Algorithm

Dijkstra's algorithm (or Dijkstra's Shortest Path First algorithm) is an algorithm for finding the shortest paths between vertices in a graph. For example, I may want to find the shortest path along a road network for my daughter's paper route.

![dijkstra](https://github.com/user-attachments/assets/ff13c1e3-5531-42a5-80f5-c89e75385a76)
