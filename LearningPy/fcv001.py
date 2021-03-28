import pygame, sys, random, os
from pygame.joystick import get_count
from pygame.locals import *
from collections import namedtuple

horCardSlots=8
XPOS = [12, 236, 460, 684, 908, 1132, 1356, 1580]
YPOS = [70, 140, 210, 280, 350, 420, 490]
DPOS = 600
#      no zero, ace   2h
Magic1 = (0,0,29,30,31,32,33,34,35,36,37,38,39,0,0,29,30,31,32,33,34,35,36,37,38,39,0,0, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,0,0, 3, 4, 5, 6, 7, 8, 9,10,11,12,13)
Magic2 = (0,0,42,43,44,45,46,47,48,49,50,51,52,0,0,42,43,44,45,46,47,48,49,50,51,52,0,0,16,17,18,19,20,21,22,23,24,25,26,0,0,16,17,18,19,20,21,22,23,24,25,26)
#Magic = ((0,0),(0,0),(29,42),(30,43),(31,44),(32,45),(33,46),(34,47),(35,48),(36,49),(37,50),(38,51),(39,52),(0,0),(29,42),(30,43),(31,44),(32,45),(33,46),(34,47),(35,48),(36,49),(37,50),(38,51),(39,52),(0,0),(3,16)(4,17),(5,18),(6,19),(7,20),(8,21),(9,22),(10,23),(11,24),(12,25),(13,26),(0,0),(3,16)(4,17),(5,18),(6,19),(7,20),(8,21),(9,22),(10,23),(11,24),(12,25),(13,26))
print(f"Magic1={Magic1} And len(Magic1={len(Magic1)}")
print(f"Magic2={Magic2} And len(Magic2={len(Magic2)}")
col0=[]
col1=[]
col2=[]
col3=[]
col4=[]
col5=[]
col6=[]
col7=[]
DeckTbl=[[7, 34, 41, 40, 42, 33, 8], [38, 20, 28, 24, 17, 49, 37], [44, 47, 6, 31, 2, 21, 26], [29, 27, 14, 1, 50, 15, 4], [12, 13, 32, 22, 30, 11], [52, 10, 23, 25, 46, 9], [48, 5, 51, 35, 36, 3], [18, 43, 19, 45, 39, 16]]
Status_Text=""
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
def IsValidMove(Discard, DeckTbl, beginAddr, endAddr):
    # TODO: Convert screen addr to a card or set of cards put up last-card then prev card until at beginAddr
    #if Discard[0]==0:
        #   Convert bosco, joseph to DeckTbl?
    bosco,joseph=beginAddr   
    endax,enday =endAddr
    CardBegx=0
    CardBegy=0
    CardEndx=0
    CardEndy=0
    lastCardInCol = len(XPOS) - 1
    lastCardInRow = len(YPOS) - 1
    Status_Text=""

    #739, 474  This still doesnt work!!!!!!!!!!!!!!!!!!         TEST outside card area

    for xsub in range(lastCardInCol):
        if bosco > XPOS[xsub] and bosco <=XPOS[xsub + 1]:
            CardBegx=xsub
            break
    else:
        CardBegx=lastCardInCol
            #Dont forget to translate cardBeg, CardEndf=? into DeskTbl address
    for ysub in range(lastCardInRow):   
        if joseph > YPOS[ysub] and joseph <=YPOS[ysub + 1]:
            CardBegy=min(ysub, len(DeckTbl[CardBegx])-1)
            break
    else:
        CardBegy=min(lastCardInRow, len(DeckTbl[CardBegx])-1)
    for xsub in range(lastCardInCol):
        if endax > XPOS[xsub] and endax <=XPOS[xsub + 1]:
            CardEndx=xsub
            break
    else:
        CardEndx=lastCardInCol

    CardEndy=len(DeckTbl[CardEndx]) - 1 
    #for ysub in range(lastCardInRow):           #    Don't need the y since it can only go on the end
    #    if enday > YPOS[ysub] and enday <=YPOS[ysub + 1]:
    #        CardEndy=ysub
    #        break
    #else: 
    if joseph > DPOS:
        CardBegy=lastCardInRow+1
    if enday > DPOS:
        CardEndy=lastCardInRow+1
    EmptyColumn = [0]#=BackOfCard
    #How do you check to see if thecard exists
    if bosco < XPOS[0] or bosco > XPOS[lastCardInCol] + 204 or joseph < YPOS[0] or endax < XPOS[0] or endax > XPOS[lastCardInCol] + 204 or enday < YPOS[0]:
        Status_Text = "No Card Selected"
    if CardBegx > -1 and CardBegx < 8 and Status_Text == "":
        pass
    else:
        Status_Text = Status_Text + f"Initial Position: InternalError: Deck Indices (X) are out of range"
    if CardEndx > -1 and CardEndx < 8 and Status_Text == "":
        pass
    else:
        Status_Text = Status_Text + f"Final  Position: InternalError: Deck Indices (X) are out of range"
    if Status_Text == "":           #        pass        # TODO Dont del the last entry in a col                 # See above: if CardBegx > (len(DeckTbl[0])-1) or CardEndx > (len(DeckTbl[0])-1):                   sukc2=0
        if  CardEndy==lastCardInRow+1 or  CardBegy==lastCardInRow+1:
        # TODO: process Discard-Row
            if CardBegx > 3 and CardBegy==lastCardInRow+1:
                Status_Text = f"Can't move Foundation Cards"
                suck=0
            elif CardBegy!=lastCardInRow+1 and CardEndy==lastCardInRow+1 and Discard[CardEndx]==0 and CardEndx < 4 and CardBegy > 0:
                    Discard[CardEndx]=DeckTbl[CardBegx].pop(CardBegy)
            elif CardBegy!=lastCardInRow+1 and CardEndy==lastCardInRow+1 and Discard[CardEndx]==0 and CardEndx < 4 and CardBegy == 0:
                    Templike=DeckTbl[CardBegx][CardBegy]
                    DeckTbl[CardBegx][CardBegy]=0
                    Discard[CardEndx]=Templike
            elif CardBegy!=lastCardInRow+1 and CardEndy==lastCardInRow+1 and (DeckTbl[CardBegx][CardBegy] - Discard[CardEndx])==1 and CardEndx > 3 and CardBegy > 0:
                    Discard[CardEndx]=DeckTbl[CardBegx].pop(CardBegy)
            elif CardBegy!=lastCardInRow+1 and CardEndy==lastCardInRow+1 and (DeckTbl[CardBegx][CardBegy] - Discard[CardEndx])==1 and CardEndx > 3 and CardBegy ==0:
                    Templike=DeckTbl[CardBegx][CardBegy]
                    DeckTbl[CardBegx][CardBegy]=0
                    Discard[CardEndx]=Templike
            elif CardBegx < 4:
                if CardBegy == lastCardInRow+1 and CardEndy!=lastCardInRow+1 and Discard[CardBegx]==0:
                    Status_Text = f"No card to move"
                elif CardBegy == lastCardInRow+1 and CardEndy!=lastCardInRow+1 and DeckTbl[CardEndx][CardEndy] == 0:
                    DeckTbl[CardEndx][CardEndy]=Discard[CardBegx]
                    Discard[CardBegx]=0
                elif CardBegy == lastCardInRow+1 and CardEndy!=lastCardInRow+1 and (Magic1[Discard[CardBegx]]==DeckTbl[CardEndx][CardEndy] or Magic2[Discard[CardBegx]]==DeckTbl[CardEndx][CardEndy]):
                    DeckTbl[CardEndx].append(Discard[CardBegx])
                    Discard[CardBegx]=0

    #deck[CardBegx][CardBegy]
        elif DeckTbl[CardBegx][CardBegy]==0:
            Status_Text = f"No card to move"
        elif DeckTbl[CardBegx][CardBegy] > 26 and DeckTbl[CardEndx][CardEndy] > 26:
            Status_Text = "Same Black Suit"
        elif DeckTbl[CardBegx][CardBegy] < 27 and DeckTbl[CardEndx][CardEndy] < 27:
            Status_Text = "Same Red   Suit"
        else:
            print(f"Magic1[(DeckTbl[CardBegx][CardBegy])]={Magic1[(DeckTbl[CardBegx][CardBegy])]}",end="    ")
            print(f"Magic2[(DeckTbl[CardBegx][CardBegy])]={Magic2[(DeckTbl[CardBegx][CardBegy])]}",end="    ")
            print(f"DeckTbl[CardEndx][CardEndy]={DeckTbl[CardEndx][CardEndy]}")
            if Status_Text == "" and (Magic1[(DeckTbl[CardBegx][CardBegy])] == DeckTbl[CardEndx][CardEndy] or Magic2[(DeckTbl[CardBegx][CardBegy])] == DeckTbl[CardEndx][CardEndy]):
                #pass            #TODO: Need to check all cards under selected cardBegxy MOVE DeckTbl from cardbegxy cardendxy    
                TempBegy=CardBegy
                NumofFreeDiscardZeros=Discard[0:4].count(0)
                NumofFreeDeckTblZeros=0
                for pogo in range(8):
                    if len(DeckTbl[pogo])==1 and DeckTbl[pogo][0]==0: 
                        NumofFreeDeckTblZeros +=1
                numofwhileLoops=1
                lenOfBegCol =len(DeckTbl[CardBegx]) - 1
                if TempBegy < lenOfBegCol: 
                    numofwhileLoops=lenOfBegCol-TempBegy
                    if numofwhileLoops > NumofFreeDiscardZeros + NumofFreeDeckTblZeros:
                        Status_Text = "Not Enough Free Spaces for move"
                    else:
                        if lenOfBegCol==1:
                            DeckTbl[CardEndx].append(DeckTbl[CardBegx][CardBegy])
                            DeckTbl[CardBegx][CardBegy]=0
                        else:
                            for logo in range(numofwhileLoops):
                                DeckTbl[CardEndx].append(DeckTbl[CardBegx].pop(TempBegy+logo))
                else:
                    if lenOfBegCol==1:
                        DeckTbl[CardEndx].append(DeckTbl[CardBegx][CardBegy])
                        DeckTbl[CardBegx][CardBegy]=0
                    else:
                        for logo in range(numofwhileLoops):
                            Templogo=DeckTbl[CardBegx].pop(TempBegy+logo)
                            DeckTbl[CardEndx].append(Templogo)

                #while TempBegy < lenOfBegCol:
                #    if 
                #    TempBegy +=1
                #        #check each one to see if we have enough space to move it
                #else:
                #    pass
            else:
                Status_Text = "Card out of Order"
        #   elif DeckTbl[CardEndx][CardEndy]==0:
        #Check if EmptySlots<= NumCardsInSelectedAJ69Cache:
        #True Move them Else Don't Move
                suck1=0
    returnBool=Status_Text == ""            #    if Status_Text == "":           #
    return returnBool,  Discard, DeckTbl, CardBegx, CardBegy, CardEndx, CardEndy, Status_Text    #Discard,deck,beginAddr,endAddr    else:        return False, Discard, DeckTbl, CardBegx, CardBegy, CardEndx, CardEndy, Status_Text    #Discard,deck,beginAddr,endAddr
    
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
    DeckTbl.append(col0)
    DeckTbl.append(col1)
    DeckTbl.append(col2)
    DeckTbl.append(col3)
    DeckTbl.append(col4)
    DeckTbl.append(col5)
    DeckTbl.append(col6)
    DeckTbl.append(col7)
    return True
def CheckDiscard(Discard,DeckTbl):   #,col0,col1,col2,col3,col4,col5,col6,col7):    
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
            if len(DeckTbl[gog])==0: DeckTbl[gog].append(0)#Fix Empty row
            lastCardInColumn = len(DeckTbl[gog]) - 1
            if Discard[sub] > 0:                                        
                if DeckTbl[gog][lastCardInColumn] == Discard[sub] + 1:
                    Discard[sub] = DeckTbl[gog].pop(lastCardInColumn)                           #del DeckTbl[gog][lastCardInColumn]
                else: 
                    continue
            elif DeckTbl[gog][lastCardInColumn] in aces:
                Discard[sub] = DeckTbl[gog].pop(lastCardInColumn)                
    return Discard, DeckTbl   #,col0,col1,col2,col3,col4,col5,col6,col7            
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
            #lengthcol0=len(col0) - 1                   DeckTbl=
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
LIGHTGREY=(100,100,100)             #    screen = pg.display.set_mode((640, 480))
font = pygame.font.Font(None, 32)       #    clock = pg.time.Clock()
input_box = pygame.Rect(40, 10, 140, 32)   #    Rect(left, top, width, height) -> Rect
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
done = False
card_width =212
card_height=292
pathrb=f'C:/Users/Brice/source/repos/LearningPy/LearningPy/cardimagesRB'
# Setup a 300x300 pixel display with caption
width = 1860
height =800
#horCardSlots=8     #XPOS = [12, 236, 460, 684, 908, 1132, 1356, 1580]      #YPOS = [70, 140, 210, 280, 350, 420, 490]
#col0=[]            #col1=[]        #col2=[]        #col3=[]                #col4=[]        #col5=[]        #col6=[]        #col7=[]
#DeckTbl=[]          #n = 24 #rows   #m = 8 #cols    #TableB=[[0] * m for i in range(n)]
DISPLAYSURF = pygame.display.set_mode((width,height))
DISPLAYSURF.fill(WHITE)
shorty = []
pygame.display.set_caption("Brice's Free Cell")        #istring=os.path.join("images","1.png")     shorty=[] courtx=[]courty=[]
#       loop until issovable is true
shoop=0
if len(DeckTbl) > 0:
    print(DeckTbl)
else:
    setOfNumbers = list(range(1,53)) 
    random.shuffle(setOfNumbers)
    while not IsSolvable(setOfNumbers):
        print(setOfNumbers)  #setOfNumbers = list(range(1,53)) #random.shuffle(setOfNumbers)    #print(setOfNumbers)
        setOfNumbers = list(range(1,53)) 
        random.shuffle(setOfNumbers)
#while len(setOfNumbers) < 53:          #    setOfNumbers.add(random.randint(1, 52))        #!random.shuffle(setOfNumbers)      print(setOfNumbers)
x = 12; # x coordnate of image
y = 70; # y coordinate of image         card_widtht=card_width+x            i=0#1
aces=[1,14,27,40]                       #if IsSolvable(setOfNumbers):
if len(DeckTbl) > 0:
    for xxxx in range(8):
        for yyyy in range(len(DeckTbl[xxxx])):
            lit10=f"C:/Users/Brice/source/repos/LearningPy/LearningPy/cardimagesRB/{str(DeckTbl[xxxx][yyyy])}.png"
            CardImage = pygame.image.load(lit10).convert()
            if not DeckTbl[xxxx][yyyy] in TableB:      TableB[xxxx][yyyy]=DeckTbl[xxxx][yyyy]
            if xxxx == 0 and not DeckTbl[xxxx][yyyy] in col0: col0.append(DeckTbl[xxxx][yyyy])
            if xxxx == 1 and not DeckTbl[xxxx][yyyy] in col1: col1.append(DeckTbl[xxxx][yyyy])
            if xxxx == 2 and not DeckTbl[xxxx][yyyy] in col2: col2.append(DeckTbl[xxxx][yyyy])
            if xxxx == 3 and not DeckTbl[xxxx][yyyy] in col3: col3.append(DeckTbl[xxxx][yyyy])
            if xxxx == 4 and not DeckTbl[xxxx][yyyy] in col4: col4.append(DeckTbl[xxxx][yyyy])
            if xxxx == 5 and not DeckTbl[xxxx][yyyy] in col5: col5.append(DeckTbl[xxxx][yyyy])
            if xxxx == 6 and not DeckTbl[xxxx][yyyy] in col6: col6.append(DeckTbl[xxxx][yyyy])
            if xxxx == 7 and not DeckTbl[xxxx][yyyy] in col7: col7.append(DeckTbl[xxxx][yyyy])
            if shoop > 43 and DeckTbl[xxxx][yyyy] in aces:
                pass
            else:
                DISPLAYSURF.blit(CardImage, (XPOS[xxxx],YPOS[yyyy]))         #    courtx.append(newx)    courty.append(y*y_modifier)         #    i=i+1

else:
    for j,k in enumerate(setOfNumbers):     #while i<53:    
        y_modifier= (j//(horCardSlots)) #+1    #if i==horCardSlots+1 or y_modifier==0:         y_modifier=y_modifier+1             #y_modifier=y_modifier+1    
        x_modifier=(j%(horCardSlots))       #shorty.append(y_modifier) #!    newx=(x*x_modifier) + x#initial_left_width    newx=newx+(card_width*(x_modifier))    #shorty.append(YPOS[y_modifier-1])
        lit1=f"C:/Users/Brice/source/repos/LearningPy/LearningPy/cardimagesRB/{str(k)}.png"
        PenguinImage = pygame.image.load(lit1).convert()
        #if x_modifier==0:         col0.append(k)                   #if x_modifier==1:         col1.append(k)               #if x_modifier==2:         col2.append(k)    
        #if x_modifier==3:         col3.append(k)                   #if x_modifier==4:         col4.append(k)               #if x_modifier==5:         col5.append(k)    
        #if x_modifier==6:         col6.append(k)                   #if x_modifier==7:         col7.append(k)               #TableB[x_modifier][y_modifier]=k
        
        if not k in TableB:
            TableB[x_modifier][y_modifier]=k
        if x_modifier==0 and not k in col0:            col0.append(k)    
        if x_modifier==1 and not k in col1:            col1.append(k)    
        if x_modifier==2 and not k in col2:            col2.append(k)    
        if x_modifier==3 and not k in col3:            col3.append(k)    
        if x_modifier==4 and not k in col4:            col4.append(k)    
        if x_modifier==5 and not k in col5:            col5.append(k)    
        if x_modifier==6 and not k in col6:            col6.append(k)    
        if x_modifier==7 and not k in col7:            col7.append(k)    
        if j > 43 and k in aces:
            continue
        else:
            DISPLAYSURF.blit(PenguinImage, (XPOS[x_modifier],YPOS[y_modifier]))         #    courtx.append(newx)    courty.append(y*y_modifier)         #    i=i+1
#DeckTbl.append(col0)                #DeckTbl.append(col1)                #DeckTbl.append(col2)                #DeckTbl.append(col3)                
#DeckTbl.append(col5)                #DeckTbl.append(col6)                #DeckTbl.append(col7)                #DeckTbl.append(col4)
print(f'****////*\\\\****    DeckTbl(0,0)={DeckTbl[0][0]}     DeckTbl={DeckTbl}')
print(f'TableB={TableB}')
Discard,DeckTbl = CheckDiscard(Discard,DeckTbl)   #,col0,col1,col2,col3,col4,col5,col6,col7)
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
        Status_Text=""
        if event.type == QUIT:
            running = False
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            popx,popy=event.pos     #            popy=event.y
            #BeginPos = namedtuple('BeginPos',['beginx','beginy'])   
            Begpos = BeginPos(popx,popy)   
            Status_Text=""
            print(f'mous down @ {Begpos[0]},{Begpos[1]}')
        elif event.type == MOUSEBUTTONUP:
            #EndPos = namedtuple('EndPos',['endx','endy'])         
            popx,popy=event.pos    
            but1=event.button
            countofAcesSkipped=0
            CurrentBick=0
            Enditp = EndPos(popx,popy)
            if but1==1:
                print(f'mous up   @ {Enditp.endx},{Enditp.endy}')
                Status_Text=""
                returnTrue, Discard, DeckTbl, CardBegx, CardBegy, CardEndx, CardEndy, Status_Text=IsValidMove(Discard, DeckTbl, Begpos, Enditp)
                if Status_Text=="":         #screen.fill((30, 30, 30))                      # Render the current text.
                    #pass            #TODO: Actually move the card(s)
                    DISPLAYSURF.fill(WHITE)
                    pygame.display.set_caption("Brice's Free Cell")
                    for lick in range(8):
                        for bick in range(len(DeckTbl[lick])):
                            if DeckTbl[lick][bick] == 0:
                                lit1=f"C:/Users/Brice/source/repos/LearningPy/LearningPy/cardimagesRB/{str(53)}.png"
                            else:
                                lit1=f"C:/Users/Brice/source/repos/LearningPy/LearningPy/cardimagesRB/{str(DeckTbl[lick][bick])}.png"
                            PenguinImage = pygame.image.load(lit1).convert()                 
                            if bick ==len(DeckTbl[lick]) - 1 and DeckTbl[lick][bick]  in aces:
                                countofAcesSkipped +=1
                            else:
                                #CurrentBick=bick       
                                LastYPOS=len(YPOS)-1
                                if bick > LastYPOS:
                                    CurrentBick+=YPOS[LastYPOS]+(15*(bick - LastYPOS))
                                    DISPLAYSURF.blit(PenguinImage, (XPOS[lick],CurrentBick))         #    courtx.append(newx)    courty.append(y*y_modifier)         #    i=i+1
                                else:
                                    DISPLAYSURF.blit(PenguinImage, (XPOS[lick],YPOS[bick]))
                    print(f"countofAcesSkipped={countofAcesSkipped}")
                    Discard,DeckTbl = CheckDiscard(Discard,DeckTbl)   #,col0,col1,col2,col3,col4,col5,col6,col7)
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

                else:
                    #if 'click' in num1_button.handleEvent(event):
                    #    if dice == 1:
                    #        text = font.render("You Win!", 1, (0, 0, 0))
                    #        screen.blit(text, (155, 255))
                    txt_surface = font.render("                                     ", True, BLACK)
                    txt_surface = font.render(Status_Text, True, BLACK)                 # Resize the box if the text is too long.
                    width = max(200, txt_surface.get_width()+10)
                    input_box.w = width                                                 # Blit the text.
                    DISPLAYSURF.blit(txt_surface, (input_box.x+5, input_box.y+5))       # Blit the input_box rect.
                    pygame.draw.rect(DISPLAYSURF, color, input_box, 2)

                #   returnTrue, Discard, DeckTbl, CardBegx, CardBegy, CardEndx, CardEndy    #Discard,deck,beginAddr,endAddr
        elif event.type == MOUSEMOTION:
            popx,popy=event.pos     #            popy=event.y
            #print(f'mouseMove @ {popx},{popy}')
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
