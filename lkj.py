import random
from string import Template    #17    'str'| 's', 'repl'| 'r' and 'ascii'| 'a'
from string.templatelib import Template, convert

#I propose you a solution with a basic class usage.
def render_to_string(tpl: Template) -> str:
    values: list[str] = []
    for part in tpl:
        if isinstance(part, str):
            values.append(part)
        else:
            val: str = convert(part.value, part.conversion)
            if part.format_spec:
                val = format(val, part.format_spec)
            values.append(val)
    return ''.join(values)

#First, let's make a Card class:
SYMBOL_={'clubs':'♣','diamonds':'♦','hearts':'♥','spades':'♠'}
class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
    def __str__(self):
        return f'{self.value}{SYMBOL_[self.color]}'
#Then, let's make a list of colors:

colors4 = ['hearts', 'diamonds', 'spades', 'clubs'] 
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
colors = ['hearts', 'diamonds', 'spades', 'clubs']
#Finally, let's build your deck with a list comprehension:
#cColor = {'red': ['hearts', 'diamonds'], 'black': ['spades', 'clubs']}
ccColor = {'hearts': 'red', 'diamonds': 'red', 'spades': 'black', 'clubs': 'black'}
ddColor = {'hearts': '[31m', 'diamonds': '[1;33m', 'spades': '[32m', 'clubs': '[34m'}
'''RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    DARK_GRAY = "\033[1;30m"
    YELLOW = "\033[1;33m"'''
deck = [Card(value, color) for color in colors for value in values]
"""The Card class is only a wrapper, just to manipulate cards instead of tuples, 
which feels more natural. In this current state, it's almost equivalent 
to renaming the tuple type... Basically, it only consists in a constructor, 
__init__, that sets the attributes of the instance.  So when I call 
Card(value, color) in the list comprehension, so for example Card(11, 'spades'), 
a new instance of the Card class is created, which has its value attribute 
set to 11, and its color attribute set to 'spades'.
I recommend you read some tutorial about OOP for an in-depth understanding 
of the concepts.   Now, you can try and improve this idea, for instance 
by using a more detailed values list instead of the range(1, 14):

Do you think you could elaborate a little more on the class part of it? 
I am afraid I do not understand how it works, but I think your answer is great!

@Mushy0364 I edited my post :) Also, I don't like to do advertising 
for my own posts, but here is a strongly related question about 
what I think OOP can bring: Python OO program structure planning.

Mushy0364    Over a year ago
Great thanks for clearing everything up, I will be sure to try this out. 
I have already made a dictionary with values being stored such as 
values = {1:"Ace",etc.) I will definitely take your recommendation 
of reading the OOP tutorial. Thank you for the assistance.
"""
SDeck=[]
for pop in deck:   #print(list(mydict.keys())[list(mydict.values()).index(cColor[pop.color])])
    print(f'Card:  \033{ddColor[pop.color]}{pop}\033[0m!  ==>{ccColor[pop.color]}')
    # if ccColor[pop.color] == 'red':               #     print(f'Card:  \033[31m{pop}\033[0m!  ==>{ccColor[pop.color]}')               # else:             #     print(f'Card:  \033[1;30m{pop}\033[0m!  ==>{ccColor[pop.color]}')
    SDeck.append(pop)
print(deck[1], ccColor[deck[1].color])

random.shuffle(SDeck)
print(SDeck[1], ccColor[SDeck[1].color])
name = "Alice"
print(f"Hello, \033[34m{name}\033[0m!")  # 34 is the code for blue
print('\n\n\n\n')
for stn,god in enumerate(SDeck):
    print(f'\033{ddColor[god.color]}{god}\033[0m',end='  ')
    # if ccColor[god.color] == 'red':               #     print(f'\033[31m{god}\033[0m',end='  ')           # else:             #     print(f'\033[1;30m{god}\033[0m',end='  ')
    if  (stn + 1) % 8 == 0:
        print()
namf = "Brice"
print(f"\n\nHello, \033[34m{namf}\033[0m!")  # 34 is the code for blue


product: str = 'T-shirt'
price: float = 10.0
order: Template = t'Product: {product}, Price: ${price:.2f}'

print(f'{order}')
print(render_to_string(order))
