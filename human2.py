from player import Player

class Human2(Player):
    def __init__(self):
        super().__init__('Player Two')
        self.number_of_wins = 0