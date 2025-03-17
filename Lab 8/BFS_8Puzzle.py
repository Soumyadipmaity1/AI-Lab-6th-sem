from collections import deque
import copy

def bfs(start_state, goal_state):
    queue = deque()
    queue.append((start_state, []))  # Store state and path
    visited = set()
    visited.add(tuple(map(tuple, start_state)))
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal_state:
            return path  # Return the path to solution
        
        for move, new_state in get_neighbors(current_state):
            state_tuple = tuple(map(tuple, new_state))
            if state_tuple not in visited:
                visited.add(state_tuple)
                queue.append((new_state, path + [move]))
    
    return None  # No solution found

def get_neighbors(state):
    neighbors = []
    row, col = find_blank(state)
    moves = {
        "Up": (-1, 0), "Down": (1, 0),
        "Left": (0, -1), "Right": (0, 1)
    }
    
    for move, (dr, dc) in moves.items():
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = copy.deepcopy(state)
            new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
            neighbors.append((move, new_state))
    
    return neighbors

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return None

# Example usage
start_state = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

solution = bfs(start_state, goal_state)
if solution:
    print("Solution found:", solution)
else:
    print("No solution found")