import pygame, sys, random, os
from pygame.locals import *
from collections import namedtuple

horCardSlots=8
XPOS = [12, 236, 460, 684, 908, 1132, 1356, 1580]
YPOS = [70, 140, 210, 280, 350, 420, 490]
DPOS = 600
col0=[]
col1=[]
col2=[]
col3=[]
col4=[]
col5=[]
col6=[]
col7=[]
TableA=[]
# Declaring namedtuple()   
BeginPos = namedtuple('BeginPos',['beginx','beginy'])   
EndPos = namedtuple('EndPos',['endx','endy'])         
# Adding values   
Begpos = BeginPos('1500','19')   
Enditp = EndPos('1200','144')      
# Access using index   
print (f"The Begin (DragStart) Position beginy using index (Begpos[1]) is: {Begpos[1]}",end ="")   
print (Begpos[1])   
      
# Access using name    
print (f"The End (Drop) Position endx using keyname (Enditp.endx) is: {Enditp.endx}", end = "")   #print (Enditp.endx) 
n = 24 #rows
m = 8 #cols
TableB=[[0] * n for i in range(m)]
Discard=[0,0,0,0,0,0,0,0]
def GetFaceValue(realval):
    if realval < 14:
        return realval # realval less than 14
    elif realval < 27: # realval greater than or equal 14 and less than 27
        return (realval - 13)
    elif realval < 40: # realval greater than or equal 27 and  less than 40
        return (realval - 26)
    else             : # realval greater than or equal 39 and  less than 53
        return (realval - 26)
def IsValidMove(deck,beginAddr,endAddr):
    # TODO: Convert screen addr to a card or set of cards put up last-card then prev card until at beginAddr
    #if Discard[0]==0:
        #   Convert bosco, joseph to TableA?
    bosco,joseph=beginAddr   
    endax,enday =endAddr
    CardBegx=0
    CardBegy=0
    CardEndx=0
    CardEndy=0
    lastCardInCol = len(XPOS) - 1
    lastCardInRow = len(YPOS) - 1


    #739, 474
    for xsub in range(lastCardInCol):
        if bosco > XPOS[xsub] and bosco <=XPOS[xsub + 1]:
            CardBegx=xsub
            break
    else:
        CardBegx=lastCardInCol

    for ysub in range(lastCardInRow):
        if joseph > YPOS[ysub] and joseph <=YPOS[ysub + 1]:
            CardBegy=ysub
            break
    else:
        CardBegy=lastCardInRow
    for xsub in range(lastCardInCol):
        if endax > XPOS[xsub] and endax <=XPOS[xsub + 1]:
            CardEndx=xsub
            break
    else:
        CardEndx=lastCardInCol
    for ysub in range(lastCardInRow):
        if enday > YPOS[ysub] and enday <=YPOS[ysub + 1]:
            CardEndy=ysub
            break
    else: 
        CardEndy=lastCardInRow 
    if enday > DPOS:
        CardEndy=lastCardInRow+1
    if  CardEndy==lastCardInRow+1 or  CardBegy==lastCardInRow+1:
        # TODO: process Discard-Row
        suck=0
    #deck[CardBegx][CardBegy]
    if deck[CardEndx][CardEndy]==0:
        #Check if EmptySlots<= NumCardsInSelectedAJ69Cache:
        #True Move them Else Don't Move
        suck1=0


    return True, CardBegx, CardBegy, CardEndx, CardEndy
    
def IsSolvable(setOfNumbers):
    for o,p in enumerate(setOfNumbers):
        y_modifier= (o//(horCardSlots)) #+1    #if i==horCardSlots+1 or y_modifier==0:         y_modifier=y_modifier+1             #y_modifier=y_modifier+1    
        x_modifier=(o%(horCardSlots))       #shorty.append(y_modifier) #!    newx=(x*x_modifier) + x#initial_left_width    newx=newx+(card_width*(x_modifier))    #shorty.append(YPOS[y_modifier-1])
        #lit1=f"C:/Users/Brice/source/repos/LearningPy/LearningPy/cardimagesRB/{str(k)}.png"
        #PenguinImage = pygame.image.load(lit1).convert()
        if not p in TableB:
            TableB[x_modifier][y_modifier]=p
        if x_modifier==0 and not p in col0:
            col0.append(p)    
        if x_modifier==1 and not p in col1:
            col1.append(p)    
        if x_modifier==2 and not p in col2:
            col2.append(p)    
        if x_modifier==3 and not p in col3:
            col3.append(p)    
        if x_modifier==4 and not p in col4:
            col4.append(p)    
        if x_modifier==5 and not p in col5:
            col5.append(p)    
        if x_modifier==6 and not p in col6:
            col6.append(p)    
        if x_modifier==7 and not p in col7:
            col7.append(p)    
        #DISPLAYSURF.blit(PenguinImage, (XPOS[x_modifier],YPOS[y_modifier]))         #    courtx.append(newx)    courty.append(y*y_modifier)         #    i=i+1
    TableA.append(col0)
    TableA.append(col1)
    TableA.append(col2)
    TableA.append(col3)
    TableA.append(col4)
    TableA.append(col5)
    TableA.append(col6)
    TableA.append(col7)
    return True
def CheckDiscard(Discard,TableA):   #,col0,col1,col2,col3,col4,col5,col6,col7):    
    aces=[1,14,27,40]
    twos=[2,15,28,41]
    jack=[11,24,37,50]
    quen=[12,25,38,51]
    king=[13,26,39,52]
    #Discard=[0,0,0,0,0,0,0,0]
    #Quantify auto card move to ace(foundation)-area == Discard[4-7]
        #if three ace(foundation)-area cards are gt> the other pull_fc=threefc#8,4,9,10=8
    fvDiscard1=GetFaceValue(Discard[4])
    fvDiscard2=GetFaceValue(Discard[5])
    fvDiscard3=GetFaceValue(Discard[6])
    fvDiscard4=GetFaceValue(Discard[7])
    MinDiscard=min(fvDiscard1,fvDiscard2,fvDiscard3,fvDiscard4)
    #check each colx[lengthcolx]==Discard[4-7]+1 if Discard[4-7] >0     #TODO: blit from col0-7 and discard; Hint
    for sub in range(4,8):
        for gog in range(8):                                            #gog is 0 thru 7  is colx
            lastCardInColumn = len(TableA[gog]) - 1
            if Discard[sub] > 0:                                        
                if TableA[gog][lastCardInColumn] == Discard[sub] + 1:
                    Discard[sub] = TableA[gog].pop(lastCardInColumn)                           #del TableA[gog][lastCardInColumn]
                else: 
                    continue
            elif TableA[gog][lastCardInColumn] in aces:
                Discard[sub] = TableA[gog].pop(lastCardInColumn)                
    return Discard,TableA   #,col0,col1,col2,col3,col4,col5,col6,col7            
            #    if   col0[len(col0) - 1] == Discard[sub] + 1:           
            #        Discard[sub]= col0[len(col0) - 1]                   
            #        col0.pop(len(col0) - 1)                             
            #    elif col1[len(col1) - 1] == Discard[sub] + 1:           
            #        Discard[sub]= col1[len(col1) - 1]                   
            #        col1.pop(len(col1) - 1)                             
            #    elif col2[len(col2) - 1] == Discard[sub] + 1:
            #        Discard[sub]= col2[len(col2) - 1]
            #        col2.pop(len(col2) - 1)
            #    elif col3[len(col3) - 1] == Discard[sub] + 1:
            #        Discard[sub]= col3[len(col3) - 1]
            #        col3.pop(len(col3) - 1)
            #    elif col4[len(col4) - 1] == Discard[sub] + 1:
            #        Discard[sub]= col4[len(col4) - 1]
            #        col4.pop(len(col4) - 1)
            #    elif col5[len(col5) - 1] == Discard[sub] + 1:
            #        Discard[sub]= col5[len(col5) - 1]
            #        col5.pop(len(col5) - 1)
            #    elif col6[len(col6) - 1] == Discard[sub] + 1:
            #        Discard[sub]= col6[len(col6) - 1]
            #        col6.pop(len(col6) - 1)
            #    elif col7[len(col7) - 1] == Discard[sub] + 1:
            #        Discard[sub]= col7[len(col7) - 1]
            #        col7.pop(len(col7) - 1)
            #    else:
            #        continue
            #elif col0[len(col0) -1] in aces: #Discard[sub]==0
            #    Discard[sub]=col0[len(col0) - 1]
            #    col0.pop(len(col0) - 1)
            #elif col1[len(col1) -1] in aces: #Discard[sub]==0
            #    Discard[sub]=col1[len(col1) - 1]
            #    col1.pop(len(col1) - 1)
            #elif col2[len(col2) -1] in aces: #Discard[sub]==0
            #    Discard[sub]=col2[len(col2) - 1]
            #    col2.pop(len(col2) - 1)
            #elif col3[len(col3) -1] in aces: #Discard[sub]==0
            #    Discard[sub]=col3[len(col3) - 1]
            #    col3.pop(len(col3) - 1)
            #elif col4[len(col4) -1] in aces: #Discard[sub]==0
            #    Discard[sub]=col4[len(col4) - 1]
            #    col4.pop(len(col4) - 1)
            #elif col5[len(col5) -1] in aces: #Discard[sub]==0
            #    Discard[sub]=col5[len(col5) - 1]
            #    col5.pop(len(col5) - 1)
            #elif col6[len(col6) -1] in aces: #Discard[sub]==0
            #    Discard[sub]=col6[len(col6) - 1]
            #    col6.pop(len(col6) - 1)
            #elif col7[len(col7) -1] in aces: #Discard[sub]==0
            #    Discard[sub]=col7[len(col7) - 1]
            #    col7.pop(len(col7) - 1)
            #else:
            #    continue
            #lengthcol0=len(col0) - 1                   TableA=
            #if col0[lengthcol0] in aces:
            #    if   Discard[4]==0:
            #         Discard[4]=col0[lengthcol0] 
            #    elif Discard[5]==0:
            #         Discard[5]=col0[lengthcol0]
            #    elif Discard[6]==0:
            #         Discard[6]=col0[lengthcol0]
            #    else:
            #         Discard[7]=col0[lengthcol0]
            #    col0.pop(lengthcol0)
            #lengthcol1=len(col1) - 1
            #if col1[lengthcol1] in aces:        
            #    if Discard[4]==0:
            #        Discard[4]=col1[lengthcol1]
            #    elif Discard[5]==0:
            #        Discard[5]=col1[lengthcol1]
            #    elif Discard[6]==0:
            #        Discard[6]=col1[lengthcol1]
            #    else:
            #        Discard[7]=col1[lengthcol1]
            #    col1.pop(lengthcol1) #pop
    
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
#horCardSlots=8     #XPOS = [12, 236, 460, 684, 908, 1132, 1356, 1580]      #YPOS = [70, 140, 210, 280, 350, 420, 490]
#col0=[]            #col1=[]        #col2=[]        #col3=[]                #col4=[]        #col5=[]        #col6=[]        #col7=[]
#TableA=[]          #n = 24 #rows   #m = 8 #cols    #TableB=[[0] * m for i in range(n)]
DISPLAYSURF = pygame.display.set_mode((width,height))
DISPLAYSURF.fill(WHITE)
shorty = []
pygame.display.set_caption("Display some stuff")        #istring=os.path.join("images","1.png")     shorty=[] courtx=[]courty=[]
#       loop until issovable is true
setOfNumbers = list(range(1,53)) 
random.shuffle(setOfNumbers)
while not IsSolvable(setOfNumbers):
    print(setOfNumbers)  #setOfNumbers = list(range(1,53)) #random.shuffle(setOfNumbers)    #print(setOfNumbers)
    setOfNumbers = list(range(1,53)) 
    random.shuffle(setOfNumbers)
#while len(setOfNumbers) < 53:          #    setOfNumbers.add(random.randint(1, 52))        #!random.shuffle(setOfNumbers)      print(setOfNumbers)
x = 12; # x coordnate of image
y = 70; # y coordinate of image         card_widtht=card_width+x            i=0#1
#if IsSolvable(setOfNumbers):
for j,k in enumerate(setOfNumbers):     #while i<53:    
    y_modifier= (j//(horCardSlots)) #+1    #if i==horCardSlots+1 or y_modifier==0:         y_modifier=y_modifier+1             #y_modifier=y_modifier+1    
    x_modifier=(j%(horCardSlots))       #shorty.append(y_modifier) #!    newx=(x*x_modifier) + x#initial_left_width    newx=newx+(card_width*(x_modifier))    #shorty.append(YPOS[y_modifier-1])
    lit1=f"C:/Users/Brice/source/repos/LearningPy/LearningPy/cardimagesRB/{str(k)}.png"
    PenguinImage = pygame.image.load(lit1).convert()
    #if x_modifier==0:         col0.append(k)                   #if x_modifier==1:         col1.append(k)               #if x_modifier==2:         col2.append(k)    
    #if x_modifier==3:         col3.append(k)                   #if x_modifier==4:         col4.append(k)               #if x_modifier==5:         col5.append(k)    
    #if x_modifier==6:         col6.append(k)                   #if x_modifier==7:         col7.append(k)               #TableB[x_modifier][y_modifier]=k
    aces=[1,14,27,40]
    if not k in TableB:
        TableB[x_modifier][y_modifier]=k
    if x_modifier==0 and not k in col0:
        col0.append(k)    
    if x_modifier==1 and not k in col1:
        col1.append(k)    
    if x_modifier==2 and not k in col2:
        col2.append(k)    
    if x_modifier==3 and not k in col3:
        col3.append(k)    
    if x_modifier==4 and not k in col4:
        col4.append(k)    
    if x_modifier==5 and not k in col5:
        col5.append(k)    
    if x_modifier==6 and not k in col6:
        col6.append(k)    
    if x_modifier==7 and not k in col7:
        col7.append(k)    
    if j > 43 and k in aces:
        continue
    else:
        DISPLAYSURF.blit(PenguinImage, (XPOS[x_modifier],YPOS[y_modifier]))         #    courtx.append(newx)    courty.append(y*y_modifier)         #    i=i+1
#TableA.append(col0)                #TableA.append(col1)                #TableA.append(col2)                #TableA.append(col3)                
#TableA.append(col5)                #TableA.append(col6)                #TableA.append(col7)                #TableA.append(col4)
print(f'****////*\\\\****    TableA(0,0)={TableA[0][0]}     TableA={TableA}')
print(f'TableB={TableB}')
Discard,TableA = CheckDiscard(Discard,TableA)   #,col0,col1,col2,col3,col4,col5,col6,col7)
running = True 
IsThereADiscard = False
for g,h in enumerate(Discard):
    if h > 0:
        IsThereADiscard = True
        lit1=f"C:/Users/Brice/source/repos/LearningPy/LearningPy/cardimagesRB/{str(h)}.png"
    else:
        lit1=f"C:/Users/Brice/source/repos/LearningPy/LearningPy/cardimagesRB/{str(53)}.png"
    PenguinImage = pygame.image.load(lit1).convert()
    DISPLAYSURF.blit(PenguinImage, (XPOS[g],DPOS))     
pygame.display.flip() # paint screen one time
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
print("col 0-7:")
print(col0,col1,col2,col3,col4,col5,col6,col7)
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            popx,popy=event.pos     #            popy=event.y
            #BeginPos = namedtuple('BeginPos',['beginx','beginy'])   
            Begpos = BeginPos(popx,popy)   
            
            print(f'mous down @ {Begpos[0]},{Begpos[1]}')
        elif event.type == MOUSEBUTTONUP:
            #EndPos = namedtuple('EndPos',['endx','endy'])         
            popx,popy=event.pos    
            but1=event.button
            Enditp = EndPos(popx,popy)
            if but1==1:
                print(f'mous up   @ {Enditp.endx},{Enditp.endy}')
                returnTrue, CardBegx, CardBegy, CardEndx, CardEndy=IsValidMove(TableA,Begpos,Enditp)
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
#loop over, quit pygame             #print(shorty) 
# Creating Lines and Shapes         asurf = pygame.image.load(os.path.join('images', '1.png'))
#pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (130,170))          #pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (170,170))
#pygame.draw.line(DISPLAYSURF, GREEN, (130,170), (170,170))         #pygame.draw.circle(DISPLAYSURF, BLACK, (100,50), 30)
#pygame.draw.circle(DISPLAYSURF, BLACK, (200,50), 30)               #pygame.draw.rect(DISPLAYSURF, RED, (100, 200, 100, 50), 2)
#pygame.draw.rect(DISPLAYSURF, BLACK, (110, 260, 80, 5))
