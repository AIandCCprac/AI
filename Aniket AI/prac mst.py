def prim_mst(graph):
    vertices = len(graph)
    # Initialize lists to keep track of visited vertices and their corresponding minimum edge weights
    visited = [False] * vertices
    min_weights = [float('inf')] * vertices
    # Choose the starting vertex as 0
    start_vertex = 0
    min_weights[start_vertex] = 0

    for _ in range(vertices):
        # Find the vertex with the minimum weight from the set of unvisited vertices
        min_weight = float('inf')
        min_vertex = -1
        for v in range(vertices):
            if not visited[v] and min_weights[v] < min_weight:
                min_weight = min_weights[v]
                min_vertex = v

        # Mark the vertex as visited
        visited[min_vertex] = True

        # Update the minimum weights and select the minimum weight edges for the adjacent vertices
        for v in range(vertices):
            if (
                graph[min_vertex][v] != 0  # Check if there is an edge between the vertices
                and not visited[v]  # Check if the vertex is unvisited
                and graph[min_vertex][v] < min_weights[v]  # Check if the weight is less than the current minimum weight
            ):
                min_weights[v] = graph[min_vertex][v]

    return min_weights


# Get user input for the number of vertices and the graph
def main():
    vertices = int(input("Enter the number of vertices: "))
    graph = []
    print("Enter the adjacency matrix for the graph:")
    for _ in range(vertices):
        row = list(map(int, input().split()))
        graph.append(row)

# Call the prim_mst function to find the minimum spanning tree
    mst = prim_mst(graph)

# Print the minimum weights for the MST
    print("Minimum weights for the MST:")
    for i, weight in enumerate(mst):
        print(f"Vertex {i}: {weight}")

main()