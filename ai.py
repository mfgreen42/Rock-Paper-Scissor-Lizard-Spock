
from player import Player
import random

class Ai(Player):

    def __init__(self):
        super().__init__()
        self.ai_choice = ['Rock', 'Paper','Scissor', 'Lizard', 'Spock']
        self.name = 'Computer'
        self.ai_player = Player()
        

    def computer_choice(self):
        self.ai_choice = random.choice(self.ai_choice)
        print(f'The computer chose {self.ai_choice}')