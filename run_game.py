
from time import sleep

from human1 import Human1
from human2 import Human2
from ai import Ai

# player_one = Human1.throw_hands
# player_two = Human2.throw_hands
# player_ai = Ai.throw_hands

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

      

    def human_vs_ai_gameplay(self):
        battle_bool = True
        while battle_bool:
            if self.human1.number_of_wins == 2:
                battle_bool = False
                print('Player One is the WINNER!!')
                break
            elif self.ai.number_of_wins == 2:
                battle_bool = False
                print('The Computer is the Winner!!!')
                break
            self.human1.throw_hands()
            self.ai.throw_hands()
            if self.human1.human1_choice == self.ai.ai_choice:
                print('That is a tie, play again!')
            elif self.human1.human1_choice == 'Scissors' and self.ai.ai_choice == 'Paper' or self.human1.human1_choice == 'Scissors' and self.ai.ai_choice == 'Lizard':
                print('Player One wins this round')
                self.human1.number_of_wins += 1
            elif self.human1.human1_choice == 'Paper' and self.ai.ai_choice == 'Rock' or self.human1.human1_choice == 'Paper' and self.ai.ai_choice == 'Spock':
                print('Player One wins this round')
                self.human1.number_of_wins += 1
            elif self.human1.human1_choice == 'Rock' and self.ai.ai_choice == 'Lizard' or self.human1.human1_choice == 'Rock' and self.ai.ai_choice == 'Scissors':
                print('Player One wins this round')
                self.human1.number_of_wins += 1
            elif self.human1.human1_choice == 'Lizard' and self.ai.ai_choice == 'Spock' or self.human1.human1_choice == 'Lizard' and self.ai.ai_choice =='Paper':
                print('Player Once wins this round')
                self.human1.number_of_wins += 1
            elif self.human1.human1_choice == 'Spock' and self.ai.ai_choice == 'Scissors' or self.human1.human1_choice == 'Spock' and self.ai.ai_choice == 'Rock':
                print('Player Once wins this round')
                self.human1.number_of_wins =+ 1
            elif self.ai.ai_choice == 'Scissors' and self.human1.human1_choice == 'Paper' or self.ai.ai_choice == 'Scissors' and self.human1.human1_choice == 'Lizard':
                print('The Computer wins this round')
                self.ai.number_of_wins += 1
            elif self.ai.ai_choice =='Paper' and self.human1.human1_choice == 'Rock' or self.ai.ai_choice == 'Paper' and self.human1.human1_choice == 'Spock':
                print('The Computer wins this round')
                self.ai.number_of_wins += 1
            elif self.ai.ai_choice =='Rock' and self.human1.human1_choice =='Lizard' or self.ai.ai_choice =='Rock' and self.human1.human1_choice == 'Scissors':
                print('The Computer wins this round')
                self.ai.number_of_wins += 1
            elif self.ai.ai_choice == 'Lizard' and self.human1.human1_choice =='Spock' or self.ai.ai_choice =='Lizard' and self.human1.human1_choice =='Paper':
                print('The Computer wins this round')
                self.ai.number_of_wins += 1
            elif self.ai.ai_choice =='Spock' and self.human1.human1_choice == 'Scissors' or self.ai.ai_choice =='Spock' and self.human1.human1_choice =='Rock':
                print('The Computer wins this round')
                self.ai.number_of_wins += 1
            else:
                continue
            

    def human_vs_human_gameplay(self):   
        battle_bool = True
        while battle_bool:
            if self.human1.number_of_wins == 2:
                battle_bool = False
                print('Player One is the WINNER!!')
                break
            elif self.human2.number_of_wins == 2:
                battle_bool = False
                print('Player Two is the Winner!!!')
                break
            self.human1.throw_hands()
            self.human2.throw_hands()
            if self.human1.human1_choice == self.human2.human2_choice:
                print('That is a tie, play again!')
            elif self.human1.human1_choice == 'Scissors' and self.human2.human2_choice == 'Paper' or self.human1.human1_choice == 'Scissors' and self.human2.human2_choice == 'Lizard':
                print('Player One wins this round')
                self.human1.number_of_wins += 1
            elif self.human1.human1_choice == 'Paper' and self.human2.human2_choice == 'Rock' or self.human1.human1_choice == 'Paper' and self.human2.human2_choice == 'Spock':
                print('Player One wins this round')
                self.human1.number_of_wins += 1
            elif self.human1.human1_choice == 'Rock' and self.human2.human2_choice == 'Lizard' or self.human1.human1_choice == 'Rock' and self.human2.human2_choice == 'Scissors':
                print('Player One wins this round')
                self.human1.number_of_wins += 1
            elif self.human1.human1_choice == 'Lizard' and self.human2.human2_choice == 'Spock' or self.human1.human1_choice == 'Lizard' and self.human2.human2_choice =='Paper':
                print('Player Once wins this round')
                self.human1.number_of_wins += 1
            elif self.human1.human1_choice == 'Spock' and self.human2.human2_choice == 'Scissors' or self.human1.human1_choice == 'Spock' and self.human2.human2_choice == 'Rock':
                print('Player Once wins this round')
                self.human1.number_of_wins =+ 1
            elif self.human2.human2_choice == 'Scissors' and self.human1.human1_choice == 'Paper' or self.human2.human2_choice == 'Scissors' and self.human1.human1_choice == 'Lizard':
                print('The Computer wins this round')
                self.human2.number_of_wins += 1
            elif self.human2.human2_choice =='Paper' and self.human1.human1_choice == 'Rock' or self.human2.human2_choice == 'Paper' and self.human1.human1_choice == 'Spock':
                print('The Computer wins this round')
                self.human2.number_of_wins += 1
            elif self.human2.human2_choice =='Rock' and self.human1.human1_choice =='Lizard' or self.human2.human2_choice =='Rock' and self.human1.human1_choice == 'Scissors':
                print('The Computer wins this round')
                self.human2.number_of_wins += 1
            elif self.human2.human2_choice == 'Lizard' and self.human1.human1_choice =='Spock' or self.human2.human2_choice =='Lizard' and self.human1.human1_choice =='Paper':
                print('The Computer wins this round')
                self.human2.number_of_wins += 1
            elif self.human2.human2_choice =='Spock' and self.human1.human1_choice == 'Scissors' or self.human2.human2_choice =='Spock' and self.human1.human1_choice =='Rock':
                print('The Computer wins this round')
                self.human2.number_of_wins += 1
            else:
                continue
    