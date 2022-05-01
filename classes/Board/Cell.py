from classes.Vessels.Ship import Ship


class Cell:

    def __init__(self, x: int, y: str):
        self.is_cell_hit = False
        self.ship = None
        self.x = x
        self.y = y

    def hit(self):
        self.is_cell_hit = True
        if self.ship is not None:
            self.ship.hit()

    def is_hit(self) -> bool:
        return self.is_cell_hit

    def place(self, ship: Ship):
        self.ship = ship

    def get_ship(self) -> Ship:
        return self.ship

    def enemy_print(self):
        if self.is_hit() and self.ship is None:
            return "+"
        elif self.is_hit():
            return "x"
        else:
            return "-"

    def __str__(self):
        if self.is_hit():
            return "+"
        elif self.ship is None:
            return "-"
        else:
            return self.ship.get_name()[0]
