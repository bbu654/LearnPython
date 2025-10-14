#17

#I propose you a solution with a basic class usage.

#First, let's make a Card class:

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
    def __str__(self):
        return f'Card:  {self.value} of {self.color}'
#Then, let's make a list of colors:
colors4 = ['hearts', 'diamonds', 'spades', 'clubs'] 
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
colors = ['hearts', 'diamonds', 'spades', 'clubs']
#Finally, let's build your deck with a list comprehension:
#cColor = {'red': ['hearts', 'diamonds'], 'black': ['spades', 'clubs']}
ccColor = {'hearts': 'red', 'diamonds': 'red', 'spades': 'black', 'clubs': 'black'}
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
for pop in deck:   #print(list(mydict.keys())[list(mydict.values()).index(cColor[pop.color])])
    print(f'{pop}  ==>{ccColor[pop.color]}')




#
'''

PS C:\Users\gulwe\Source\Python>  c:; cd 'c:\Users\gulwe\Source\Python'; & 'c:\Program Files\Python313\python.exe' 'c:\Users\gulwe\.vscode\extensions\ms-python.debugpy-2025.10.0-win32-x64\bundled\libs\debugpy\launcher' '58309' '--' 'c:\Users\gulwe\Source\Python\Cards.py' 
Card: aceheart
Card: acediamonds
Card: acespades
Card: aceclubs
Card: 2heart
Card: 2diamonds
Card: 2spades
Card: 2clubs
Card: 3heart
Card: 3diamonds
Card: 3spades
Card: 3clubs
Card: 4heart
Card: 4diamonds
Card: 4spades
Card: 4clubs
Card: 5heart
Card: 5diamonds
Card: 5spades
Card: 5clubs
Card: 6heart
Card: 6diamonds
Card: 6spades
Card: 6clubs
Card: 7heart
Card: 7diamonds
Card: 7spades
Card: 7clubs
Card: 8heart
Card: 8diamonds
Card: 8spades
Card: 8clubs
Card: 9heart
Card: 9diamonds
Card: 9spades
Card: 9clubs
Card: 10heart
Card: 10diamonds
Card: 10spades
Card: 10clubs
Card: jackheart
Card: jackdiamonds
Card: jackspades
Card: jackclubs
Card: queenheart
Card: queendiamonds
Card: queenspades
Card: queenclubs
Card: kingheart
Card: kingdiamonds
Card: kingspades
Card: kingclubs
PS C:\Users\gulwe\Source\Python>  c:; cd 'c:\Users\gulwe\Source\Python'; & 'c:\Program Files\Python313\python.exe' 'c:\Users\gulwe\.vscode\extensions\ms-python.debugpy-2025.10.0-win32-x64\bundled\libs\debugpy\launcher' '58337' '--' 'c:\Users\gulwe\Source\Python\Cards.py' 
Card:  ace of heart
Card:  ace of diamonds
Card:  ace of spades
Card:  ace of clubs
Card:  2 of heart
Card:  2 of diamonds
Card:  2 of spades
Card:  2 of clubs
Card:  3 of heart
Card:  3 of diamonds
Card:  3 of spades
Card:  3 of clubs
Card:  4 of heart
Card:  4 of diamonds
Card:  4 of spades
Card:  4 of clubs
Card:  5 of heart
Card:  5 of diamonds
Card:  5 of spades
Card:  5 of clubs
Card:  6 of heart
Card:  6 of diamonds
Card:  6 of spades
Card:  6 of clubs
Card:  7 of heart
Card:  7 of diamonds
Card:  7 of spades
Card:  7 of clubs
Card:  8 of heart
Card:  8 of diamonds
Card:  8 of spades
Card:  8 of clubs
Card:  9 of heart
Card:  9 of diamonds
Card:  9 of spades
Card:  9 of clubs
Card:  10 of heart
Card:  10 of diamonds
Card:  10 of spades
Card:  10 of clubs
Card:  jack of heart
Card:  jack of diamonds
Card:  jack of spades
Card:  jack of clubs
Card:  queen of heart
Card:  queen of diamonds
Card:  queen of spades
Card:  queen of clubs
Card:  king of heart
Card:  king of diamonds
Card:  king of spades
Card:  king of clubs
PS C:\Users\gulwe\Source\Python>  c:; cd 'c:\Users\gulwe\Source\Python'; & 'c:\Program Files\Python313\python.exe' 'c:\Users\gulwe\.vscode\extensions\ms-python.debugpy-2025.10.0-win32-x64\bundled\libs\debugpy\launcher' '58358' '--' 'c:\Users\gulwe\Source\Python\Cards.py' 
Card:  ace of heart
Card:  2 of heart
Card:  3 of heart
Card:  4 of heart
Card:  5 of heart
Card:  6 of heart
Card:  7 of heart
Card:  8 of heart
Card:  9 of heart
Card:  10 of heart
****************************************
Card:  J of clubs
Card:  Q of clubs
Card:  K of clubs
PS C:\Users\gulwe\Source\Python>  c:; cd 'c:\Users\gulwe\Source\Python'; & 'c:\Program Files\Python313\python.exe' 'c:\Users\gulwe\.vscode\extensions\ms-python.debugpy-2025.10.0-win32-x64\bundled\libs\debugpy\launcher' '58614' '--' 'c:\Users\gulwe\Source\Python\Cards.py' 
PS C:\Users\gulwe\Source\Python>  c:; cd 'c:\Users\gulwe\Source\Python'; & 'c:\Program Files\Python313\python.exe' 'c:\Users\gulwe\.vscode\extensions\ms-python.debugpy-2025.10.0-win32-x64\bundled\libs\debugpy\launcher' '58642' '--' 'c:\Users\gulwe\Source\Python\Cards.py' 
PS C:\Users\gulwe\Source\Python>  c:; cd 'c:\Users\gulwe\Source\Python'; & 'c:\Program Files\Python313\python.exe' 'c:\Users\gulwe\.vscode\extensions\ms-python.debugpy-2025.10.0-win32-x64\bundled\libs\debugpy\launcher' '58667' '--' 'c:\Users\gulwe\Source\Python\Cards.py' 
PS C:\Users\gulwe\Source\Python>  c:; cd 'c:\Users\gulwe\Source\Python'; & 'c:\Program Files\Python313\python.exe' 'c:\Users\gulwe\.vscode\extensions\ms-python.debugpy-2025.10.0-win32-x64\bundled\libs\debugpy\launcher' '58800' '--' 'c:\Users\gulwe\Source\Python\Cards.py' 
Card:  A of hearts red
Card:  2 of hearts red
Card:  3 of hearts red
Card:  4 of hearts red
Card:  5 of hearts red
Card:  6 of hearts red
Card:  7 of hearts red
Card:  8 of hearts red
Card:  9 of hearts red
Card:  T of hearts red
Card:  J of hearts red
Card:  Q of hearts red
Card:  K of hearts red
Card:  A of diamonds red
Card:  2 of diamonds red
Card:  3 of diamonds red
Card:  4 of diamonds red
Card:  5 of diamonds red
Card:  6 of diamonds red
Card:  7 of diamonds red
Card:  8 of diamonds red
Card:  9 of diamonds red
Card:  T of diamonds red
Card:  J of diamonds red
Card:  Q of diamonds red
Card:  K of diamonds red
Card:  A of spades black
Card:  2 of spades black
Card:  3 of spades black
Card:  4 of spades black
Card:  5 of spades black
Card:  6 of spades black
Card:  7 of spades black
Card:  8 of spades black
Card:  9 of spades black
Card:  T of spades black
Card:  J of spades black
Card:  Q of spades black
Card:  K of spades black
Card:  A of clubs black
Card:  2 of clubs black
Card:  3 of clubs black
Card:  4 of clubs black
Card:  5 of clubs black
Card:  6 of clubs black
Card:  7 of clubs black
Card:  8 of clubs black
Card:  9 of clubs black
Card:  T of clubs black
Card:  J of clubs black
Card:  Q of clubs black
Card:  K of clubs black
PS C:\Users\gulwe\Source\Python>  c:; cd 'c:\Users\gulwe\Source\Python'; & 'c:\Program Files\Python313\python.exe' 'c:\Users\gulwe\.vscode\extensions\ms-python.debugpy-2025.10.0-win32-x64\bundled\libs\debugpy\launcher' '58826' '--' 'c:\Users\gulwe\Source\Python\Cards.py' 
Card:  A of hearts  ==>red
Card:  2 of hearts  ==>red
Card:  3 of hearts  ==>red
Card:  4 of hearts  ==>red
Card:  5 of hearts  ==>red
Card:  6 of hearts  ==>red
Card:  7 of hearts  ==>red
Card:  8 of hearts  ==>red
Card:  9 of hearts  ==>red
Card:  T of hearts  ==>red
Card:  J of hearts  ==>red
Card:  Q of hearts  ==>red
Card:  K of hearts  ==>red
Card:  A of diamonds  ==>red
Card:  2 of diamonds  ==>red
Card:  3 of diamonds  ==>red
Card:  4 of diamonds  ==>red
Card:  5 of diamonds  ==>red
Card:  6 of diamonds  ==>red
Card:  7 of diamonds  ==>red
Card:  8 of diamonds  ==>red
Card:  9 of diamonds  ==>red
Card:  T of diamonds  ==>red
Card:  J of diamonds  ==>red
Card:  Q of diamonds  ==>red
Card:  K of diamonds  ==>red
Card:  A of spades  ==>black
Card:  2 of spades  ==>black
Card:  3 of spades  ==>black
Card:  4 of spades  ==>black
Card:  5 of spades  ==>black
Card:  6 of spades  ==>black
Card:  7 of spades  ==>black
Card:  8 of spades  ==>black
Card:  9 of spades  ==>black
Card:  T of spades  ==>black
Card:  J of spades  ==>black
Card:  Q of spades  ==>black
Card:  K of spades  ==>black
Card:  A of clubs  ==>black
Card:  2 of clubs  ==>black
Card:  3 of clubs  ==>black
Card:  4 of clubs  ==>black
Card:  5 of clubs  ==>black
Card:  6 of clubs  ==>black
Card:  7 of clubs  ==>black
Card:  8 of clubs  ==>black
Card:  9 of clubs  ==>black
Card:  T of clubs  ==>black
Card:  J of clubs  ==>black
Card:  Q of clubs  ==>black
Card:  K of clubs  ==>black
PS C:\Users\gulwe\Source\Python>  c:; cd 'c:\Users\gulwe\Source\Python'; & 'c:\Program Files\Python313\python.exe' 'c:\Users\gulwe\.vscode\extensions\ms-python.debugpy-2025.10.0-win32-x64\bundled\libs\debugpy\launcher' '58856' '--' 'c:\Users\gulwe\Source\Python\Cards.py' 
Card:  A of hearts  ==>red
Card:  2 of hearts  ==>red
Card:  3 of hearts  ==>red
Card:  4 of hearts  ==>red
Card:  5 of hearts  ==>red
Card:  6 of hearts  ==>red
Card:  7 of hearts  ==>red
Card:  8 of hearts  ==>red
Card:  9 of hearts  ==>red
Card:  T of hearts  ==>red
Card:  J of hearts  ==>red
Card:  Q of hearts  ==>red
Card:  K of hearts  ==>red
Card:  A of diamonds  ==>red
Card:  2 of diamonds  ==>red
Card:  3 of diamonds  ==>red
Card:  4 of diamonds  ==>red
Card:  5 of diamonds  ==>red
Card:  6 of diamonds  ==>red
Card:  7 of diamonds  ==>red
Card:  8 of diamonds  ==>red
Card:  9 of diamonds  ==>red
Card:  T of diamonds  ==>red
Card:  J of diamonds  ==>red
Card:  Q of diamonds  ==>red
Card:  K of diamonds  ==>red
Card:  A of spades  ==>black
Card:  2 of spades  ==>black
Card:  3 of spades  ==>black
Card:  4 of spades  ==>black
Card:  5 of spades  ==>black
Card:  6 of spades  ==>black
Card:  7 of spades  ==>black
Card:  8 of spades  ==>black
Card:  9 of spades  ==>black
Card:  T of spades  ==>black
Card:  J of spades  ==>black
Card:  Q of spades  ==>black
Card:  K of spades  ==>black
Card:  A of clubs  ==>black
Card:  2 of clubs  ==>black
Card:  3 of clubs  ==>black
Card:  4 of clubs  ==>black
Card:  5 of clubs  ==>black
Card:  6 of clubs  ==>black
Card:  7 of clubs  ==>black
Card:  8 of clubs  ==>black
Card:  9 of clubs  ==>black
Card:  T of clubs  ==>black
Card:  J of clubs  ==>black
Card:  Q of clubs  ==>black
Card:  K of clubs  ==>black



'''