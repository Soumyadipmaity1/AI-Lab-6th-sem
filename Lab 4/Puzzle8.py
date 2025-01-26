import copy

GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

def isGoal(state):
    return state == GOAL_STATE

def findBlank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
            
def getNeighbors(state):
    """Generate all possible moves by swapping the blank tile."""
    row, col = findBlank(state)
    moves = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    
    for dr, dc in directions:
        n_row, n_col = row + dr, col + dc
        if 0 <= n_row < 3 and 0 <= n_col < 3:
            new_state = copy.deepcopy(state)
            new_state[row][col], new_state[n_row][n_col] = new_state[n_row][n_col], new_state[row][col]
            moves.append(new_state)
    return moves

def solve(state, path, visited):
    """Recursive function to solve the 8-puzzle problem."""
    # Base case: Check if the goal is reached
    if isGoal(state):
        return path 
    
    # Mark the current state as visited
    visited.add(tuple(tuple(row) for row in state))
    
    # Explore all neighbors
    for neighbor in getNeighbors(state):
        if tuple(tuple(row) for row in neighbor) not in visited:
            result = solve(neighbor, path + [neighbor], visited)
            if result:
                return result
            
    return None  # No solution found

# Initialize visited states set
visited = set()

# Solve the puzzle
solution = solve(initial_state, [initial_state], visited)

# Print the solution
if solution:
    print("Solution found:")
    for state in solution:
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
