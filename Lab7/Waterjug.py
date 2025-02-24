from collections import deque

def water_jug_problem(start, goal, capacity):
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path, len(path) - 1  # Number of moves is (length of path - 1)

        for next_state in get_next_states(state, capacity):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    return None, None

def get_next_states(state, capacity):
    x, y = state
    max_x, max_y = capacity
    next_states = []

    # Fill Jug 1
    if x < max_x:
        next_states.append((max_x, y))

    # Fill Jug 2
    if y < max_y:
        next_states.append((x, max_y))

    # Empty Jug 1
    if x > 0:
        next_states.append((0, y))

    # Empty Jug 2
    if y > 0:
        next_states.append((x, 0))

    # Pour water from Jug 1 to Jug 2
    if x > 0:
        transfer = min(x, max_y - y)
        next_states.append((x - transfer, y + transfer))

    # Pour water from Jug 2 to Jug 1
    if y > 0:
        transfer = min(y, max_x - x)
        next_states.append((x + transfer, y - transfer))

    return next_states

# Define capacity of jugs
start = (0, 0)
goal = (0, 1)  # Change the goal state accordingly
capacity = (3, 4)  # (Jug1, Jug2)

# Find the solution
path, moves = water_jug_problem(start, goal, capacity)

if path:
    print("Steps:", path)
    print("Total Moves:", moves)
else:
    print("No solution found.")