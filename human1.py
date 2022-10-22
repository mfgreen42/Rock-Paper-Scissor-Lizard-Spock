
from player import Player
from ai import Ai

class Human1(Player):
    def __init__(self):
        super().__init__('Player One')
        self.number_of_wins = 0

    def throw_hands(self):
        print("""
Choose: Rock, Paper, Scissors, Lizard, or Spock
""")
        human_input = input('Choose your gesture:  ')
        if human_input != 'Rock' or 'Paper' or 'Scissors' or 'Lizard' or 'Spock':
            print('Invalid entry, please choose again.')
            human_input = input('Choose your gesture:  ')
        else:
            print(f'Player one choose {human_input}')
        
        


    