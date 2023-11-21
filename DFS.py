def dfs(graph, start, visited):
    if start not in visited:
        print(start, end=" ")
        visited.add(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

# User inputs for the graph
graph = {}
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    edge = input("Enter edge (node1 node2): ").split()
    node1, node2 = edge
    graph.setdefault(node1, []).append(node2)
    graph.setdefault(node2, []).append(node1)

start_node = input("Enter the starting node: ")
visited_nodes = set()

# Call DFS with the user-provided graph and starting node
print("DFS traversal starting from node", start_node, ":")
dfs(graph, start_node, visited_nodes)
