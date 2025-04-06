from collections import deque

grid = [
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 0]
]

def bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    # Ensure start and goal are valid
    if grid[start[0]][start[1]] == 0 or grid[goal[0]][goal[1]] == 0:
        return None
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([(start, [start])])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    visited[start[0]][start[1]] = True  # Mark start as visited

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True  # Mark visited when enqueuing
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None

# Ensure start and goal are in walkable areas
start = (2, 1)  # Valid start position
goal = (5, 3)   # Valid goal position

path = bfs(grid, start, goal)

if path:
    print("Shortest Path:", path)
else:
    print("No path found.")