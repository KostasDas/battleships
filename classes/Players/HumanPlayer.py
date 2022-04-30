from classes.Board.Board import Board
from classes.Board.Cell import Cell
from classes.Players.Player import Player
from classes.Vessels.Ship import Ship


class HumanPlayer(Player):

    def place_ship(self, ship: Ship):
        start = input()
        while not self.board.place_ship(start, ship):
            start = input()

    def hit(self, b: Board) -> Cell:
        hit = input()
        while not b.hit(hit):
            hit = input()
        return b.get_current_hit()
