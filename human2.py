from player import Player
from time import sleep


class Human2(Player):
    def __init__(self):
        super().__init__('Player Two')
        self.number_of_wins = 0
        self.human2_choice = ''

    def throw_hands(self):
        valid = True
        print('Player Two please choose from the following:')
        for gesture in self.gesture_choices:
            sleep(.25)
            print(gesture)
        while valid:
            human_input = input('Choose your gesture:  ')
            if human_input == 'Rock' or 'Paper' or 'Scissors' or 'Lizard' or 'Spock':
                print(f'Player Two chose {human_input}')
                self.human2_choice = human_input
                valid = False
                return self.human2_choice

          

            else:
                
                print('Invalid entry, please choose again.')
