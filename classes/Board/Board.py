import string
from typing import Union

from classes.Board.Cell import Cell
from classes.Vessels.Ship import Ship


class Board:
    X_AXIS = 10
    Y_AXIS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    def __init__(self):
        self.allowed_directions = ['T', 'B', 'R', 'L']
        self.board = list()
        self.initialize_board()
        self.hit_cell = None

    def get_current_hit(self) -> Cell:
        return self.hit_cell

    def initialize_board(self):
        for x in range(self.X_AXIS):
            for y in self.Y_AXIS:
                self.board.append(Cell(x, y))

    def place_ship(self, placement: str, ship: Ship) -> bool:
        placement = placement.upper()
        if not self.verify_placement(placement):
            return False
        start = Cell(int(placement[1]), placement[0])
        end = self.calculate_end(start, ship.get_size(), placement[2])
        if not end or self.board_occupied(start, end):
            return False
        self.allocate_ship(start, end, ship)
        return True

    def calculate_end(self, start: Cell, size: int, direction: str) -> Union[bool, Cell]:
        end_x = start.x
        end_y = start.y
        y_index = self.Y_AXIS.index(end_y)
        try:
            if direction.lower() == 't':
                end_y = self.Y_AXIS[(y_index - size) + 1]
            elif direction.lower() == 'b':
                end_y = self.Y_AXIS[(y_index + size) - 1]
            elif direction.lower() == 'r':
                end_x = (end_x + size) - 1
            elif direction.lower() == 'l':
                end_x = (end_x - size) + 1
        except IndexError:
            print("Could not populate cells. Cell overflow error - wrong direction")
            return False
        if end_x > self.X_AXIS:
            print("Could not populate cells. Cell overflow error - wrong direction")
            return False

        return Cell(end_x, end_y)

    def verify_placement(self, placement: str) -> bool:
        if len(placement) != 3:
            print("Incorrect placement information")
            return False
        if not placement[0].isalpha() or not placement[1].isdigit():
            print("Invalid grid selection")
            return False
        if not placement[2] in self.allowed_directions:
            print("Invalid direction")
            return False
        if placement[0] not in string.ascii_uppercase[:10]:
            print("Invalid Y axis character")
            return False
        return True

    def board_occupied(self, start, end):
        cells = self.get_cells_between_vertically(start.x, start.y, end.y) if start.x == end.x \
            else self.get_cells_between_horizontally(start.y, start.x, end.x)
        for cell in cells:
            if cell.ship is not None:
                print(f"Placement {cell.x} - {cell.y} already occupied")
                return True
        return False

    def print(self, enemy=False):
        print("", end=3 * " ")
        for x in range(self.X_AXIS):
            print(x, end=3 * " ")
        print()
        for i in range(self.X_AXIS):
            print(self.Y_AXIS[i], end=2 * " ")
            y = self.Y_AXIS[i]
            for x in range(self.X_AXIS):
                if not enemy:
                    print(self.find_cell(x, y), end=3 * " ")
                else:
                    print(self.find_cell(x, y).enemy_print(), end=3 * " ")
            print()

    def enemy_print(self):
        self.print(True)

    def allocate_ship(self, start, end, ship):
        """
        Allocate the ship object to all the cells between start and end.
        :param start:
        :param end:
        :param ship:
        :return:
        """
        start.ship = ship
        end.ship = ship
        # ship placement is vertical
        if start.x == end.x:
            self.place_ship_vertically(start, end, ship)
        # ship placement is horizontal
        if start.y == end.y:
            self.place_ship_horizontally(start, end, ship)

    def find_cell(self, x: int, y: str) -> Cell:
        for b in self.board:
            if b.x == x and b.y == y:
                return b
        # this should never happen, we messed something up
        raise IndexError(f"Could not find a cell at {x} and {y}")

    def hit(self, hit: str) -> bool:
        hit = hit.upper()
        if len(hit) != 2:
            print("Incorrect coordinates length. Should be two characters")
            return False
        if not hit[1].isdigit() or hit[0] not in string.ascii_uppercase[:10]:
            print("Invalid coordinates. Please choose between A-J and 0-9, e.g. A0")
            return False
        self.hit_cell = self.find_cell(int(hit[1]), hit[0])
        if self.hit_cell.is_hit():
            print("The chosen coordinates have already been hit")
            self.hit_cell = None
            return False
        self.hit_cell.hit()
        return True

    def place_ship_vertically(self, start, end, ship):
        for cell in self.get_cells_between_vertically(start.x, start.y, end.y):
            cell.ship = ship

    def place_ship_horizontally(self, start, end, ship):
        for cell in self.get_cells_between_horizontally(start.y, start.x, end.x):
            cell.ship = ship

    def get_cells_between_horizontally(self, start_y, start_x, end_x) -> [Cell]:
        start = start_x if start_x < end_x else end_x
        end = start_x if start_x > end_x else end_x

        for i in range(start, end + 1):
            yield self.find_cell(i, start_y)

    def get_cells_between_vertically(self, start_x, start_y, end_y) -> [Cell]:
        start = start_y if start_y < end_y else end_y
        end = start_y if start_y > end_y else end_y

        for i in range(self.Y_AXIS.index(start), self.Y_AXIS.index(end) + 1):
            yield self.find_cell(start_x, self.Y_AXIS[i])
