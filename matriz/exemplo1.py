board = []
for _ in range(3):
    #board.append([''] * 3)
    board.append(['', '', ''])

board[0][2] = 'X'
board[1][0] = 'O'
board[1][1] = 'X'
board[2][0] = 'O'

for row in board:
    print(row)
