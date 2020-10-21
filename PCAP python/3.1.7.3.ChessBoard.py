EMPTY = "-"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK #Replace Row 0 Coloumn 0 with 'ROOK'
board[0][7] = ROOK
board[7][0] = ROOK #Replace Row 7 Column 0 with 'ROOK'
board[7][7] = ROOK

print(board)