
from player import Player
import random

class Ai(Player):

    def __init__(self):
        super().__init__('Computer')
        # self.ai_choice = ['Rock', 'Paper','Scissor', 'Lizard', 'Spock']
        

    def throw_hands(self):
        self.ai_choice = random.choice(self.gesture_choices.keys)
        print(f'The computer chose {self.ai_choice}')