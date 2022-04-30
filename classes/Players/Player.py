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

    def get_board(self) -> Board:
        return self.board

    @abstractmethod
    def hit(self, b: Board) -> Cell:
        """
        Overwrite this method in your implementation of the Player abstract class in order to customize the
        hit mechanics. It is a requirement if you wish to create your own player
        :param b:
        :return:
        """
        pass

    @abstractmethod
    def place_ship(self, p: Ship) -> None:
        """
        Overwrite this method in your implementation of the Player abstract class in order to customize the ship
        placement. It is a requirement if you wish to create your own player
        :param p:
        :return:
        """
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
