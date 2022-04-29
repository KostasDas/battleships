from classes.Board.Board import Board
from classes.Board.Cell import Cell
from classes.Players.Player import Player


class HumanPlayer(Player):
    def hit(self, b: Board) -> Cell:
        hit = input()
        while not b.hit(hit):
            hit = input()
        return b.get_current_hit()


