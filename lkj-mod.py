import random          #17         #I propose you a solution with a basic class usage.          #First, let's make a Card class:
SYMBOL_={'clubs':'♣','diamonds':'♦','hearts':'♥','spades':'♠'}
class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
    def __str__(self):
        return f'{self.value}{SYMBOL_[self.color]}'
    
#Then, let's make a list of colors:
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
colors = ['hearts', 'diamonds', 'spades', 'clubs']
#Finally, let's build your deck with a list comprehension:
#cColor = {'red': ['hearts', 'diamonds'], 'black': ['spades', 'clubs']}
ccColor = {'hearts': 'red', 'diamonds': 'red', 'spades': 'black', 'clubs': 'black'}
ddColor = {'hearts': '[31m', 'diamonds': '[1;33m', 'spades': '[32m', 'clubs': '[34m'}
''' RED = "\033[0;31m"                  GREEN = "\033[0;32m"                BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"                 PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"                 DARK_GRAY = "\033[1;30m"            YELLOW = "\033[1;33m"'''
deck = [Card(value, color) for color in colors for value in values]
"""The Card class is only a wrapper, just to manipulate cards instead of tuples, which feels more natural. In this current state, it's almost equivalent to renaming the tuple type... Basically, it only consists in a constructor, 
__init__, that sets the attributes of the instance.  So when I call Card(value, color) in the list comprehension, so for example Card(11, 'spades'), a new instance of the Card class is created, which has its value attribute 
set to 11, and its color attribute set to 'spades'.  Mushy0364    Over a year ago    Great thanks for clearing everything up, I will be sure to try this out. I have already made a dictionary with values being stored such as 
values = {1:"Ace",etc.) I will definitely take your recommendation    of reading the OOP tutorial. Thank you for the assistance.
"""#    print(f'Card:  \033{ddColor[pop.color]}{pop}\033[0m!  ==>{ccColor[pop.color]}') # if ccColor[pop.color] == 'red':
    #     print(f'Card:  \033[31m{pop}\033[0m!  ==>{ccColor[pop.color]}')    # else:    #     print(f'Card:  \033[1;30m{pop}\033[0m!  ==>{ccColor[pop.color]}')
random.shuffle(deck)
print('\n\n\n\n')
for stn,god in enumerate(deck):
    print(f'\033{ddColor[god.color]}{god}\033[0m',end='  ')
    if  (stn + 1) % 8 == 0:
        print()


        
namf = "Brice"
print(f"\n\nHello, \033[34m{namf}\033[0m!")  # 34 is the code for blue
