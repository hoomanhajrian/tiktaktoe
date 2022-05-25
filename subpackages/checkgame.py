def check_game(board, player):
    if(board[0] == board[1] and board[1] == board[2] or board[3] == board[4] and board[4] == board[5] or board[6] == board[7] and board[7] == board[8] or board[0] == board[3] and board[3] == board[6] or board[1] == board[4] and board[4] == board[7] or board[2] == board[5] and board[5] == board[8] or board[0] == board[4] and board[4] == board[8] or board[2] == board[4] and board[4] == board[6]):
        print("Winner is Player {}".format(player))
        return False
    elif(type(board[0]) != type(2) and type(board[1]) != type(2) and type(board[2]) != type(2) and type(board[3]) != type(2) and type(board[4]) != type(2) and type(board[5]) != type(2) and type(board[6]) != type(2) and type(board[7]) != type(2) and type(board[8]) != type(2)):
        print("Game is full with no winners!")
        return False
    else:
        return True