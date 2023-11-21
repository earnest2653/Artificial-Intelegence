import heapq

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def astar(grid, start, goal):
    open_set = [(0, start)]
    heapq.heapify(open_set)
    came_from = {}
    cost_so_far = {start: 0}

    while open_set:
        current_cost, current_node = heapq.heappop(open_set)

        if current_node == goal:
            path = reconstruct_path(came_from, start, goal)
            return path

        for neighbor in neighbors(current_node, grid):
            new_cost = cost_so_far[current_node] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_set, (priority, neighbor))
                came_from[neighbor] = current_node

    return None

def neighbors(node, grid):
    x, y = node
    candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    return [n for n in candidates if 0 <= n[0] < len(grid) and 0 <= n[1] < len(grid[0]) and grid[n[0]][n[1]] != 1]

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    return path[::-1]

# User input for the grid
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

grid = []
print("Enter the grid (0 for empty, 1 for obstacle):")
for _ in range(rows):
    row = list(map(int, input().split()))
    grid.append(row)

# User input for start and goal points
start_point = tuple(map(int, input("Enter the start point (row column): ").split()))
goal_point = tuple(map(int, input("Enter the goal point (row column): ").split()))

# Run A* algorithm
result_path = astar(grid, start_point, goal_point)

# Output the result
if result_path:
    print("Optimal Path:", result_path)
else:
    print("No path found.")
