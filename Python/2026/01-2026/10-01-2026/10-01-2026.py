def check_hor(board):
    if (board[0][1] == board[0][0] and board[0][1] == board[0][2]):
        return board[0][1] + " wins"
    elif (board[1][1] == board[1][0] and board[1][1] == board[1][2]):
        return board[1][1] + " wins"
    elif (board[2][1] == board[2][0] and board[2][1] == board[2][2]):
        return board[2][1] + " wins"


def check_ver(board):
    if (board[1][0] == board[0][0] and board[1][0] == board[2][0]):
        return board[1][0] + " wins"
    elif (board[1][1] == board[0][1] and board[1][1] == board[2][1]):
        return board[1][1] + " wins"
    elif (board[1][2] == board[0][2] and board[1][2] == board[2][2]):
        return board[1][2] + " wins"


def check_diag(board):
    if (board[1][1] == board[0][0] and board[1][1] == board[2][2]):
        return board[1][1] + " wins"
    elif (board[1][1] == board[0][2] and board[1][1] == board[2][0]):
        return board[1][1] + " wins"


def tic_tac_toe(board):
    if (check_hor(board) != None):
        return check_hor(board)
    elif (check_ver(board) != None):
        return check_ver(board)
    elif (check_diag(board) != None):
        return check_diag(board)
    else:
        return "Draw"


tic_tac_toe([["X", "X", "X"], ["O", "O", "X"], ["O", "X", "O"]])
tic_tac_toe([["X", "O", "X"], ["X", "O", "X"], ["O", "O", "X"]])
tic_tac_toe([["X", "O", "O"], ["O", "X", "O"], ["O", "X", "X"]])
tic_tac_toe([["O", "X", "X"], ["X", "O", "O"], ["X", "O", "X"]])
tic_tac_toe([["X", "O", "O"], ["O", "X", "O"], ["O", "X", "X"]])
