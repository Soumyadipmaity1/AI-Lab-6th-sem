function queensPlacement(n) {
    let board = Array.from({ length: n }, () => Array(n).fill(0));
    placeQueens(0, board, n);
}

function placeQueens(row, board, n) {
    if (row === n) {
        board.forEach(line => console.log(line.join(" ")));
        console.log();
        return;
    }

    for (let col = 0; col < n; col++) {
        if (safeCheck(board, row, col, n)) {
            board[row][col] = 1;
            placeQueens(row + 1, board, n);
            board[row][col] = 0; // Backtrack
        }
    }
}

function safeCheck(board, x, y, n) {
    for (let i = 0; i < x; i++) {
        if (board[i][y] === 1) return false;
    }

    for (let i = x - 1, j = y - 1; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] === 1) return false;
    }

    for (let i = x - 1, j = y + 1; i >= 0 && j < n; i--, j++) {
        if (board[i][j] === 1) return false;
    }

    return true;
}

const n = parseInt(prompt("Enter the number of queens: "), 10);
queensPlacement(n);
