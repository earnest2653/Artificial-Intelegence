from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# User inputs for the graph
graph = {}
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    edge = input("Enter edge (node1 node2): ").split()
    node1, node2 = edge
    graph.setdefault(node1, []).append(node2)
    graph.setdefault(node2, []).append(node1)

start_node = input("Enter the starting node: ")

# Call BFS with the user-provided graph and starting node
print("BFS traversal starting from node", start_node, ":")
bfs(graph, start_node)
