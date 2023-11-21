from constraint import Problem

def map_coloring(num_regions, regions, constraints):
    problem = Problem()

    # Define variables for each region with possible colors
    for region in regions:
        problem.addVariable(region, ['Red', 'Green', 'Blue'])

    # Add constraints for neighboring regions
    for constraint in constraints:
        region1, region2 = constraint
        problem.addConstraint(lambda color1, color2: color1 != color2, (region1, region2))

    # Solve the CSP problem
    solutions = problem.getSolutions()

    if solutions:
        print("Map Coloring Solutions:")
        for solution in solutions:
            print(solution)
    else:
        print("No solution found.")

# User input
num_regions = int(input("Enter the number of regions: "))
regions = [input(f"Enter name of region {i + 1}: ") for i in range(num_regions)]

# User input for constraints
num_constraints = int(input("Enter the number of constraints: "))
constraints = []
for _ in range(num_constraints):
    region1, region2 = input("Enter constraint (e.g., A B for A and B cannot have the same color): ").split()
    constraints.append((region1, region2))

# Run Map Coloring CSP
map_coloring(num_regions, regions, constraints)
