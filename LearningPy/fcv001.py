import pygame, sys, random, os
from pygame.locals import *


horCardSlots=8
XPOS = [12, 236, 460, 684, 908, 1132, 1356, 1580]
YPOS = [70, 140, 210, 280, 350, 420, 490]
col0=[]
col1=[]
col2=[]
col3=[]
col4=[]
col5=[]
col6=[]
col7=[]
TableA=[]
n = 24 #rows
m = 8 #cols
TableB=[[0] * m for i in range(n)]

def IsSolvable(setOfNumbers):
    for i,j in enumerate(setOfNumbers):
        y_modifier= (j//(horCardSlots)) #+1    #if i==horCardSlots+1 or y_modifier==0:         y_modifier=y_modifier+1             #y_modifier=y_modifier+1    
        x_modifier=(j%(horCardSlots))       #shorty.append(y_modifier) #!    newx=(x*x_modifier) + x#initial_left_width    newx=newx+(card_width*(x_modifier))    #shorty.append(YPOS[y_modifier-1])
        #lit1=f"C:/Users/Brice/source/repos/LearningPy/LearningPy/cardimagesRB/{str(k)}.png"
        #PenguinImage = pygame.image.load(lit1).convert()
        TableB[x_modifier][y_modifier]=k
        if x_modifier==0:         col0.append(k)    
        if x_modifier==1:         col1.append(k)    
        if x_modifier==2:         col2.append(k)    
        if x_modifier==3:         col3.append(k)    
        if x_modifier==4:         col4.append(k)    
        if x_modifier==5:         col5.append(k)    
        if x_modifier==6:         col6.append(k)    
        if x_modifier==7:         col7.append(k)    
        #DISPLAYSURF.blit(PenguinImage, (XPOS[x_modifier],YPOS[y_modifier]))         #    courtx.append(newx)    courty.append(y*y_modifier)         #    i=i+1
    TableA.append(col0)
    TableA.append(col1)
    TableA.append(col2)
    TableA.append(col3)
    TableA.append(col4)
    TableA.append(col5)
    TableA.append(col6)
    TableA.append(col7)
    
    return False 
# Initialize program
pygame.init()
 
# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()
 
# Setting up color objects
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
card_width =212
card_height=292
pathrb=f'C:/Users/Brice/source/repos/LearningPy/LearningPy/cardimagesRB'
# Setup a 300x300 pixel display with caption
width = 1860
height =800
#horCardSlots=8
#XPOS = [12, 236, 460, 684, 908, 1132, 1356, 1580]
#YPOS = [70, 140, 210, 280, 350, 420, 490]
#col0=[]
#col1=[]
#col2=[]
#col3=[]
#col4=[]
#col5=[]
#col6=[]
#col7=[]
#TableA=[]
#n = 24 #rows
#m = 8 #cols
#TableB=[[0] * m for i in range(n)]
DISPLAYSURF = pygame.display.set_mode((width,height))
DISPLAYSURF.fill(WHITE)
shorty = []
pygame.display.set_caption("Display some stuff")        #istring=os.path.join("images","1.png")     shorty=[] courtx=[]courty=[]
#       loop until issovable is true
while not IsSolvable(setOfNumbers:=random.shuffle(list(range(1,53)))):
    print(setOfNumbers)  #setOfNumbers = list(range(1,53)) #random.shuffle(setOfNumbers)    #print(setOfNumbers)
#while len(setOfNumbers) < 53:          #    setOfNumbers.add(random.randint(1, 52))        #!random.shuffle(setOfNumbers)      print(setOfNumbers)
x = 12; # x coordnate of image
y = 70; # y coordinate of image         card_widtht=card_width+x            i=0#1
#if IsSolvable(setOfNumbers):
for j,k in enumerate(setOfNumbers):     #while i<53:    
    y_modifier= (j//(horCardSlots)) #+1    #if i==horCardSlots+1 or y_modifier==0:         y_modifier=y_modifier+1             #y_modifier=y_modifier+1    
    x_modifier=(j%(horCardSlots))       #shorty.append(y_modifier) #!    newx=(x*x_modifier) + x#initial_left_width    newx=newx+(card_width*(x_modifier))    #shorty.append(YPOS[y_modifier-1])
    lit1=f"C:/Users/Brice/source/repos/LearningPy/LearningPy/cardimagesRB/{str(k)}.png"
    PenguinImage = pygame.image.load(lit1).convert()
    TableB[x_modifier][y_modifier]=k
    if x_modifier==0:         col0.append(k)    
    if x_modifier==1:         col1.append(k)    
    if x_modifier==2:         col2.append(k)    
    if x_modifier==3:         col3.append(k)    
    if x_modifier==4:         col4.append(k)    
    if x_modifier==5:         col5.append(k)    
    if x_modifier==6:         col6.append(k)    
    if x_modifier==7:         col7.append(k)    
    DISPLAYSURF.blit(PenguinImage, (XPOS[x_modifier],YPOS[y_modifier]))         #    courtx.append(newx)    courty.append(y*y_modifier)         #    i=i+1
TableA.append(col0)
TableA.append(col1)
TableA.append(col2)
TableA.append(col3)
TableA.append(col4)
TableA.append(col5)
TableA.append(col6)
TableA.append(col7)
print(f'****////*\\\\****    TableA(0,0)={TableA[0][0]}     TableA={TableA}')
print(f'TableB={TableB}')
pygame.display.flip() # paint screen one time
running = True 
# Beginning Game Loop       TODO: NEED FREECELL RULES Valid and Invalid moves!
fcrules="""
FreeCell Solitaire Rules
FreeCell Solitaire
Thanks to Microsoft's inclusion of a version of the game in Windows 95, Freecell solitaire has become one of the world's most popular solitaires. 
Unlike Klondike (probably the best-known solitaire game), Freecell is quite winnable. In fact, the vast majority of Freecell hands can be solved.
Freecell is an "open" solitaire, so-called because all of the cards are visible at the start of a game. It is a descendant of earlier games 
such as "Eight Off" and "Baker's Game".
Initial Layout: Cards are dealt face-up into eight columns. The first four columns each contain seven cards, and the last four contain six cards each. 
Space is set aside for four foundation piles and four "free cells" -- holding stations where cards may be temporarily stored during play.
Object: The object of the game is to move the four aces, as they appear, to the foundations, and build each up in suit from ace to king (A-2-3-4-5-6-7-8-9-10-J-Q-K).
Play: Only the top (exposed) card of each tableau pile is available for play. It may be moved to a foundation pile, a free cell, or to another tableau pile. 
Within the tableau, cards are built down in sequence and alternating in color. Any card may be moved into an empty space. Blocks of cards may not be moved, 
unless the requisite number of free cells and/or tableau spaces are availabe to allow each individual card to be moved. 
If you fill all four foundation piles, you win.
"""
#print(fcrules)
print(col0,col1,col2,col3,col4,col5,col6,col7)
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            popx,popy=event.pos     #            popy=event.y
            print(f'mousedown @ {popx},{popy}')
        elif event.type == MOUSEBUTTONUP:
            popx,popy=event.pos     #            popy=event.y
            print(f'mouseup   @ {popx},{popy}')
        elif event.type == MOUSEMOTION:
            popx,popy=event.pos     #            popy=event.y
            print(f'mouseMove @ {popx},{popy}')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left;')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right;')
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump;')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left stop;')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right stop;')
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump stop;')

            if event.key == ord('q'):
                running = False  
                pygame.quit()
                sys.exit()
            
    FramePerSec.tick(FPS)

pygame.quit()
#DISPLAYSURF.blit(PenguinImage, ( x,y)  ) # paint to screen     print(courtx)               print(courty)
#loop over, quit pygame
#print(shorty) 
# Creating Lines and Shapes         asurf = pygame.image.load(os.path.join('images', '1.png'))
#pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (130,170))
#pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (170,170))
#pygame.draw.line(DISPLAYSURF, GREEN, (130,170), (170,170))
#pygame.draw.circle(DISPLAYSURF, BLACK, (100,50), 30)
#pygame.draw.circle(DISPLAYSURF, BLACK, (200,50), 30)
#pygame.draw.rect(DISPLAYSURF, RED, (100, 200, 100, 50), 2)
#pygame.draw.rect(DISPLAYSURF, BLACK, (110, 260, 80, 5))
