from enum import Enum


class ShipTypes(Enum):
    Carrier = 5
    Battleship = 4
    Cruiser = 3
    Submarine = 3.1  # small hack so that cruiser and submarine don't collide. will need int(ShipTypes.Value)
    Destroyer = 2
