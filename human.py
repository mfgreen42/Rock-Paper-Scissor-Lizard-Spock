
from player import Player

class Human(Player):
    def __init__(self, gesture):
        super().__init__()
        self.player_choice = gesture
        self.human_wins = 0
        self.human_current_round = 0
        
        


    