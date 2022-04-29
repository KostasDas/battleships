from classes.Players.Player import Player


class Game:

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def start(self):
        self.place_ships(self.player1)
        self.place_ships(self.player2)

        self.play()


    def place_ships(self, p: Player):
        board = p.board
        print(f"{p.get_name()} please place your ships using the grid below.")
        self.print_instructions()

        board.print()
        for ship in p.get_ships():
            print(f"Please place {ship.get_name()} of size {ship.get_size()}")
            print("Enter start: ")
            start = input()
            while not board.place_ship(start, ship):
                self.print_instructions()
                start = input()
            board.print()

    def play(self):
        current_player = self.player1
        other_player = self.player2

        while not self.game_is_finished():
            print(f"It is now {current_player.get_name()}'s turn")
            temp = current_player
            print(f"{current_player.get_name() } please enter coordinates to attack")
            print("----------------------------------------------------------------")
            print("Enemy board:")
            other_player.board.enemy_print()
            result = current_player.hit(other_player.board)
            print("----------------------------------------------------------------")
            hit_ship = result.get_ship()
            if hit_ship is not None:
                print(f"You've hit a ship at {result.y}{result.x}!")
                if hit_ship.is_sunk():
                    print(f"Congratulations! you've sunk {other_player.get_name()}'s {hit_ship.get_name()}")
            else:
                print(f"{result.y}{result.x} contains no enemy ship")

            # swap players
            current_player = other_player
            other_player = temp
        winner = current_player if current_player.has_lost() else other_player
        print(f"Congratulations {winner.get_name()}!! YOUR VAST SUPERIORITY OVER NAVAL WARFARE WILL NOT BE DENIED")



    def game_is_finished(self):
        return self.player1.has_lost() or self.player2.has_lost()

    @staticmethod
    def print_instructions():
        print("Use the format AXz where A is a character from A to J, X is a number from 0 to 9 and z is the direction")
        print("Choose a direction from the options: t (top) | b (bottom) | l (left) | r (right)")
        print("E.g. A1r ")
