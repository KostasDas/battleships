from classes.Board.Board import Board
from classes.Board.Cell import Cell
from classes.Vessels.Ship import Ship
from classes.Vessels.ShipTypes import ShipTypes
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name: str):
        self.name = name
        self.carrier = Ship(ShipTypes.Carrier)
        self.battleship = Ship(ShipTypes.Battleship)
        self.cruiser = Ship(ShipTypes.Cruiser)
        self.submarine = Ship(ShipTypes.Submarine)
        self.destroyer = Ship(ShipTypes.Destroyer)
        self.board = Board()

    def get_ships(self) -> []:
        return [
            self.carrier,
            self.battleship,
            self.cruiser,
            self.submarine,
            self.destroyer
        ]

    def get_name(self) -> str:
        return self.name

    @abstractmethod
    def hit(self, b: Board) -> Cell:
        pass

    def has_lost(self) -> bool:
        """
        Returns if all ships are sunk or not
        :return:
        """
        for ship in self.get_ships():
            if not ship.is_sunk():
                return False
        return True
