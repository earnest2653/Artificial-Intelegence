from queue import Queue

# State class to represent the state of the problem
class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def is_valid(self):
        if self.missionaries < 0 or self.missionaries > 3:
            return False
        if self.cannibals < 0 or self.cannibals > 3:
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def __eq__(self, other):
        return (
            self.missionaries == other.missionaries
            and self.cannibals == other.cannibals
            and self.boat == other.boat
        )

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

# Function to get possible next states from the current state
def get_next_states(current_state):
    possible_states = []
    actions = [
        (1, 0),  # Move 1 missionary
        (2, 0),  # Move 2 missionaries
        (0, 1),  # Move 1 cannibal
        (0, 2),  # Move 2 cannibals
        (1, 1),  # Move 1 missionary and 1 cannibal
    ]

    for action in actions:
        new_state = State(
            current_state.missionaries + action[0] * current_state.boat,
            current_state.cannibals + action[1] * current_state.boat,
            1 - current_state.boat,
        )

        if new_state.is_valid():
            possible_states.append(new_state)

    return possible_states

# Breadth-First Search to find the solution
def solve():
    initial_state = State(3, 3, 1)
    goal_state = State(0, 0, 0)

    visited = set()
    q = Queue()
    q.put(initial_state)
    visited.add(initial_state)

    while not q.empty():
        current_state = q.get()

        if current_state.is_goal():
            return current_state

        next_states = get_next_states(current_state)
        for next_state in next_states:
            if next_state not in visited:
                q.put(next_state)
                visited.add(next_state)

    return None

# Print the solution path
def print_solution(solution):
    path = []
    while solution:
        path.append(solution)
        solution = solution.parent if solution.parent else None

    for t in reversed(path):
        print(f"Missionaries: {t.missionaries}, Cannibals: {t.cannibals}, Boat: {t.boat}")

if __name__ == "__main__":
    solution = solve()
    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution found.")
