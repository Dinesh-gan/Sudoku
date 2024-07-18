# HintGenerator.py

def generate_hint(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col, board[row][col])
    return None  # Return None if no empty cell is found (though this should not happen in a valid game)
