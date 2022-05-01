from classes.Vessels.ShipTypes import ShipTypes


class Ship:
    def __init__(self, ship: ShipTypes):
        self.ship = ship
        self.hit_counter = 0

    def get_size(self) -> int:
        return int(self.ship.value)

    def get_name(self) -> str:
        return self.ship.name

    def hit(self):
        self.hit_counter += 1

    def is_sunk(self) -> bool:
        return self.hit_counter == self.ship.value
