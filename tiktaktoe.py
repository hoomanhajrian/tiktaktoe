from subpackages.changeplayer import change_player
from subpackages.checkgame import check_game
from subpackages.choosexoro import choose_x_or_o
from subpackages.showboard import showboard
from subpackages.updateboard import update_board


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


if __name__ == "__main__":
    tiktaktoe()
