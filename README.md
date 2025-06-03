# Learn-Data-Structures-ALGOs

## Representing a Graph in Code

We'll primarily be using an adjacency list to work with graphs. For each vertex in the graph, it stores a set of all the vertices connected to that vertex.

| Vertex | Connects with      |
|--------|--------------------|
| 0      | 1, 4               |
| 1      | 0, 2, 3, 4         |
| 2      | 1, 3               |
| 3      | 1, 2, 4            |
| 4      | 0, 1, 3            |