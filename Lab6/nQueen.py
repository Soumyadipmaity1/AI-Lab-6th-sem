def queens_placement(n):
    board = [[0] * n for _ in range(n)]
    place_queens(0, board, n)

def place_queens(row, board, n):
    if row == n:
        for line in board:
            print(" ".join(map(str, line)))  # Fixed missing string before .join()
        print()
        return

    for col in range(n):
        if safe_check(board, row, col, n):
            board[row][col] = 1
            place_queens(row + 1, board, n)
            board[row][col] = 0  # Backtrack

def safe_check(board, x, y, n):
    for i in range(x):  # Check column
        if board[i][y] == 1:
            return False

    i, j = x - 1, y - 1  # Check upper left diagonal
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = x - 1, y + 1  # Check upper right diagonal
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True

if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))  # Fixed syntax
    queens_placement(n)
