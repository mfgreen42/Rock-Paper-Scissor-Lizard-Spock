
from player import Player
import random

class Ai(Player):

    def __init__(self):
        super().__init__('Computer')
        self.number_of_wins = 0

        

    def throw_hands(self):
        self.ai_choice = random.choice(self.gesture_choices)
        print(f'The computer chose {self.ai_choice}')
        return self.ai_choice
        

