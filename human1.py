from time import sleep
from player import Player
# from ai import Ai



class Human1(Player):
    def __init__(self):
        super().__init__('Player One')
        self.number_of_wins = 0
        self.human1_choice = ''

    def throw_hands(self):
        valid = True
        print('Player One please choose from the following:')
        for gesture in self.gesture_choices:
            sleep(.25)
            print(gesture)
        while valid:
            human_input = input('Choose your gesture:  ')
            if human_input == self.gesture_choices:
                print(f'Player one chose {human_input}')
                self.human1_choice = human_input
                valid = False
                return self.human1_choice
            
            else:
                print('Invalid entry, please choose again.')



            
                

        
        
        


    