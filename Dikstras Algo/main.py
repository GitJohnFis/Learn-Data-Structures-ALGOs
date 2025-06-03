def get_min_dist_node(distances, unvisited):
    # Return the node in unvisited with the smallest distance
    min_node = None
    min_dist = float('inf')
    for node in unvisited:
        if distances.get(node, float('inf')) < min_dist:
            min_dist = distances[node]
            min_node = node
    return min_node