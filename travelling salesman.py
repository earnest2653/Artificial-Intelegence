from itertools import permutations

def calculate_total_distance(order, distances):
    total_distance = 0
    for i in range(len(order) - 1):
        total_distance += distances[order[i]][order[i + 1]]
    total_distance += distances[order[-1]][order[0]]  # Return to the starting city
    return total_distance

def traveling_salesman_problem(num_cities, distances):
    cities = list(range(num_cities))
    min_distance = float('inf')
    min_path = None

    for order in permutations(cities):
        distance = calculate_total_distance(order, distances)
        if distance < min_distance:
            min_distance = distance
            min_path = order

    return min_path, min_distance

# User input for the number of cities
num_cities = int(input("Enter the number of cities: "))

# User input for the distances between cities
distances = []
print("Enter the distances between cities (enter 0 for the distance from a city to itself):")
for i in range(num_cities):
    row = list(map(int, input().split()))
    distances.append(row)

# Calculate the optimal path and distance
optimal_path, optimal_distance = traveling_salesman_problem(num_cities, distances)

# Output the result
print("Optimal Path:", optimal_path)
print("Optimal Distance:", optimal_distance)
