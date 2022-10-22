
from time import sleep
from unicodedata import name

from human1 import Human1
from human2 import Human2
from ai import Ai

class RunGame:
    def __init__(self):
        self.ai = Ai()
        self.human1 = Human1()
        self.human2 = Human2()


    def game_play(self):
        self.display_welcome()
        self.number_of_players()

        
    def display_welcome(self):
        print("""
        Let's play Rock, Paper, Sissor, Lizard, Spock! """)
        sleep(.25)
        print("""
        Each match will be best out of three games
        Please use the number keys to make your selection
        """)
        wins_list = ['Rock crushes Scissors', 'Scissors cuts Paper','Paper covers Rock', 'Rock crushes Lizard', 'Lizard poisons Spock', 'Spock smashes Scissors', 'Scissors decapitates Lizard', 'Lizard eats Paper', 'Paper disproves Spock', 'Spock vaporizes Rock']
        for wins in wins_list:
            sleep(.25)
            print(wins)

    def number_of_players(self):
        players = input('How many players? 1 or 2 ')
        
        if players == '1':
            self.human_vs_ai_gameplay()
           
        elif players == '2':
            self.human_vs_human_gameplay()
            

        else:
            print('Please choose again: ')
            self.number_of_players()

    def how_to_win():
      pass

    def human_vs_ai_gameplay(self):
        while self.human1.number_of_wins <= 2 or self.ai.number_of_wins <= 2:
            battle_bool = True
            
            if self.human1.throw_hands == 'Scissors' and self.ai.throw_hands == 'Paper':
                print('Scissors cut Paper')
                print('Player One wins this round')
                self.human1.number_of_wins += 1
            
      
        pass

    def human_vs_human_gameplay(self):   
       pass