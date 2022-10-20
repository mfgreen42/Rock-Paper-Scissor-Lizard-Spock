
import random

class Computer:

    def __init__(self):
        self.comp_choice = ['Rock', 'Paper','Scissor', 'Lizard', 'Spock']
        

    def computer_choice(self):
        self.comp_choice = random.choice(self.comp_choice)
        print(f'The computer chose {self.comp_choice}')