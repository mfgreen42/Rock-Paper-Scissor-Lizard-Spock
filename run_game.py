
from time import sleep

from human import Human
from ai import Ai

class RunGame:
    def __init__(self):
        self.ai = Ai()
        self.human = Human()


    def game_play(self):
        self.display_welcome()
        self.number_of_players()


    def display_welcome(self):
        print("""
        Let's play Rock Paper Sissor, Lizard Spock! """)
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
            player1_name = input('What is Player 1 name? ')
            print(f'{player1_name} vs Computer')
        elif players == '2':
            player1_name = input('What is Player 1 name? ')
            player2_name = input('What is Player 2 name? ')
            print(f'{player1_name} vs {player2_name}')
        else:
            self.number_of_players()

    def human_vs_ai_gameplay(self):
        
        pass

    def human_vs_human_gameplay(self):   
       pass