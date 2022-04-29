from classes.Game import Game
from classes.Players.HumanPlayer import HumanPlayer

if __name__ == '__main__':
    game = Game(HumanPlayer("Vandl"), HumanPlayer("Daskalos"))
    game.start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
