def check_game(board, player):
    if(board[0] == board[1] and board[1] == board[2] or board[3] == board[4] and board[4] == board[5] or board[6] == board[7] and board[7] == board[8] or board[0] == board[3] and board[3] == board[6] or board[1] == board[4] and board[4] == board[7] or board[2] == board[5] and board[5] == board[8] or board[0] == board[4] and board[4] == board[8] or board[2] == board[4] and board[4] == board[6]):
        print("Winner is Player {}".format(player))
        return False
    elif(type(board[0]) != type(2) and type(board[1]) != type(2) and type(board[2]) != type(2) and type(board[3]) != type(2) and type(board[4]) != type(2) and type(board[5]) != type(2) and type(board[6]) != type(2) and type(board[7]) != type(2) and type(board[8]) != type(2)):
        print("Game is full with no winners!")
        return False
    else:
        return True


def change_player(player):
    if (player == "X"):
        return "O"
    else:
        return "X"


def showboard(board):
    print(board[6], "|", board[7], "|", board[8])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[0], "|", board[1], "|", board[2])


def choose_x_or_o():
    firstplayer = input("Player 1: Do you want to be X or O?")
    return firstplayer


def update_board(array, position, sign):
    if(type(array[position]) != type("X")):
        array[position] = sign
        return array
    else:
        return array


def tiktaktoe():
    startboard = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Welcome to Tic Tac Toe!")
    game = True
    player = choose_x_or_o()
    showboard(startboard)
    positions = []
    while(game):
        position = input(
            "player {}: Please choose the where you want to place {}:".format(player, player))
        if position in positions:
            print("There is already a value there!")
            continue
        else:
            newboard = update_board(startboard, int(position) - 1, player)
            showboard(newboard)
            game = check_game(newboard, player)
            player = change_player(player)
    again = input("Do you want to try again?(Y/N)")
    if(again == "Y"):
        tiktaktoe()
    else:
        pass


tiktaktoe()
