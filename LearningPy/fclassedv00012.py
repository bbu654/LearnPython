import pygame, sys, random, statistics, os
from pygame.joystick import get_count
from pygame.locals import *
from collections import namedtuple
""" Hello, Welcome to FreeCell 2.0.
        You must pip install pygame 
        and make sure to update pathrb 
        to where the Cards were copied"""
GlobalsForMe=[]

n = 24; """#rows""";    m = 8; """#cols""";     XCardSlots = 8;    SpaceBetweenCardY=60
TableB=[[0] * n for i in range(m)]
global DeckTbl
DeckTbl = []
PopTbl  = [[0],[0],[0],[0],[0],[0],[0],[0]]
XPOS = [12, 236, 460, 684, 908, 1132, 1356, 1580]
YPOS = [0, 70, 130, 200, 270, 340, 410, 480, 550,620,690];  DPOS = 69; EPOS=1804
#      no zero, ace   2h
Magic1 = (0,0,29,30,31,32,33,34,35,36,37,38,39,0,0,29,30,31,32,33,34,35,36,37,38,39,0,0, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,0,0, 3, 4, 5, 6, 7, 8, 9,10,11,12,13)
Magic2 = (0,0,42,43,44,45,46,47,48,49,50,51,52,0,0,42,43,44,45,46,47,48,49,50,51,52,0,0,16,17,18,19,20,21,22,23,24,25,26,0,0,16,17,18,19,20,21,22,23,24,25,26)
Magic3 = ("Zero","Ah","2h","3h","4h","5h","6h","7h","8h","9h","Th","Jh","Qh","Kh","Ad","2d","3d","4d","5d","6d","7d","8d","9d","Td","Jd","Qd","Kd","As","2s","3s","4s","5s","6s","7s","8s","9s","Ts","Js","Qs","Ks","Ac","2c","3c","4c","5c","6c","7c","8c","9c","Tc","Jc","Qc","Kc")
#Magic = ((0,0),(0,0),(29,42),(30,43),(31,44),(32,45),(33,46),(34,47),(35,48),(36,49),(37,50),(38,51),(39,52),(0,0),(29,42),(30,43),(31,44),(32,45),(33,46),(34,47),(35,48),(36,49),(37,50),(38,51),(39,52),(0,0),(3,16)(4,17),(5,18),(6,19),(7,20),(8,21),(9,22),(10,23),(11,24),(12,25),(13,26),(0,0),(3,16)(4,17),(5,18),(6,19),(7,20),(8,21),(9,22),(10,23),(11,24),(12,25),(13,26))
print(f"Magic1={Magic1} And len(Magic1={len(Magic1)}")
print(f"Magic2={Magic2} And len(Magic2={len(Magic2)}")

aces = [1,14,27,40]
king = [13,26,39,52]
PrintMoves = []
col0=[0];        col1=[0];        col2=[0];        col3=[0];   #SO FAR so good 
col4=[0];        col5=[0];        col6=[0];        col7=[0]    #TODO:ADD 8 ZEROS to below
DeckTable=[[7, 34, 41, 40, 42, 33, 8], [38, 20, 28, 24, 17, 49, 37], [44, 47, 6, 31, 2, 21, 26], [29, 27, 14, 1, 50, 15, 4], [12, 13, 32, 22, 30, 11], [52, 10, 23, 25, 46, 9], [48, 5, 51, 35, 36, 3], [18, 43, 19, 45, 39, 16]]
class deck:
    
    def __init__(self, cards):
        self.cards = cards
        self.col=[[0],[0],[0],[0],[0],[0],[0],[0]]
        # TODO:      EveryWhere there is a Discard we need a workaround!!!!!
        col0=[0];    col1=[0];    col2=[0];    col3=[0];    col4=[0];    col5=[0];    col6=[0];    col7=[0]
        self.DeckTbl=[]
        if len(self.cards) > 0:
            for ick in range(XCardSlots): #0-7
                for pop,card in enumerate(self.cards[ick]):
                    self.fillColx(ick,cards[ick][pop])
                    #self.DeckTbl[ick].append(card)
            self.fillDeckTbl(DeckTbl)
            print(f"self.DeckTbl={self.DeckTbl}")
        else:
            cards = list(range(1,53)) 
            random.shuffle(cards)
            while not self.IsSolvable(cards):
                print(cards)  #cards = list(range(1,53)) #random.shuffle(cards)    #print(cards)
                cards = list(range(1,53)) 
                random.shuffle(cards)        #        self.tricks = []    # creates a new empty list for each dog
            for card in cards:
                self.DeckTbl.append(card)
        self.Tbl=self.DeckTbl
        
    def IsSolvable(self,cards):
        self.cards = cards
        for o,p in enumerate(self.cards):
            y_modifier= (o//(XCardSlots)) #+1    #if i==horCardSlots+1 or y_modifier==0:         y_modifier=y_modifier+1             #y_modifier=y_modifier+1    
            x_modifier=(o%(XCardSlots))       #shorty.append(y_modifier) #!    newx=(x*x_modifier) + x#initial_left_width    newx=newx+(card_width*(x_modifier))    #shorty.append(YPOS[y_modifier-1])
            #lit1=f"C:/Users/Brice/source/repos/LearningPy/LearningPy/cardimagesRB/{str(k)}.pn g"
            #PenguinImage = pygame.image.load(lit1).convert()
            if not p in TableB:                TableB[x_modifier][y_modifier]=p
            self.fillColx(x_modifier,p)
            #SCREEN.blit(PenguinImage, (XPOS[x_modifier],YPOS[y_modifier]))         #    courtx.append(newx)    courty.append(y*y_modifier)         #    i=i+1
        self.fillDeckTbl(DeckTbl)

        return True

    def fillDeckTbl(self,DeckTbl):
        self.DeckTbl.append(col0);          self.DeckTbl.append(col1)
        self.DeckTbl.append(col2);          self.DeckTbl.append(col3)
        self.DeckTbl.append(col4);          self.DeckTbl.append(col5)
        self.DeckTbl.append(col6);          self.DeckTbl.append(col7)
        DeckTbl.append(col0);               DeckTbl.append(col1)
        DeckTbl.append(col2);               DeckTbl.append(col3)
        DeckTbl.append(col4);               DeckTbl.append(col5)
        DeckTbl.append(col6);               DeckTbl.append(col7)
    #def add_trick(self, trick):
    #    self.tricks.append(trick)
    def fillColx(self,xMod,xVal):
        self.col[xMod].append(xVal);PopTbl[xMod].append(xVal)
        if xMod==0 and not xVal in col0:    col0.append(xVal)
        if xMod==1 and not xVal in col1:    col1.append(xVal)
        if xMod==2 and not xVal in col2:    col2.append(xVal)
        if xMod==3 and not xVal in col3:    col3.append(xVal)
        if xMod==4 and not xVal in col4:    col4.append(xVal)
        if xMod==5 and not xVal in col5:    col5.append(xVal)
        if xMod==6 and not xVal in col6:    col6.append(xVal)
        if xMod==7 and not xVal in col7:    col7.append(xVal)
    def HaveYouWon(self,DeckTbl,SCREEN):
        won=True
        Discard,DeckTbl=self.CreatDiscard(DeckTbl)        #for pin in range(XCardSlots):        #    Discard.append(DeckTbl[pin][0])
        for icl in range(8):
            if len(DeckTbl[icl]) > 1:
                for mcl in range(1,len(DeckTbl[icl])):#check prev and start with one TODO:TODO!
                    if DeckTbl[icl][mcl-1] <= 0 or DeckTbl[icl][mcl]==  52:
                        pass#                 Magic1[52]doesnt exist only 51
                    #if (DeckTbl[icl][mcl]==0 or Magic1[(DeckTbl[CardBegx][CardBegy])] == DeckTbl[CardEndx][CardEndy] or Magic2[(DeckTbl[CardBegx][CardBegy])] == DeckTbl[CardEndx][CardEndy]):
                    elif DeckTbl[icl][mcl-1]==Magic1[DeckTbl[icl][mcl]] or DeckTbl[icl][mcl-1]==Magic2[DeckTbl[icl][mcl]]:
                        pass
                    else:
                        won=False
                        break
        if won or (Discard[4] in king and Discard[5] in king and Discard[6] in king and Discard[7] in king):
            for pcl in range(4): DeckTbl[pcl]=[0,0]    #            for qcl in range(4): Discard[qcl]=0     #        Discard[1]=0        Discard[2]=0
            for rcl in range(4,8): DeckTbl[rcl]=[king[rcl-4],0]
        else:
            DeckTbl=self.DestryDiscard(Discard,DeckTbl)
            #return True,DeckTbl        else:
        return won,DeckTbl,SCREEN
    def CreatDiscard(self,DeckTbl):
        Discard=[]
        for pin in range(XCardSlots):
            Discard.append(DeckTbl[pin].pop(0))
        return Discard,DeckTbl
    def DestryDiscard(self,Discard,DeckTbl):
        for jin in range(XCardSlots):
            DeckTbl[jin].insert(0, Discard[jin])    #            tmp=DeckTbl[jin]            DeckTbl[jin]=Discard[jin]            DeckTbl[jin].append(tmp)
        return DeckTbl
    def CheckDiscard(self,DeckTbl):   #,col0,col1,col2,col3,col4,col5,col6,col7):    
        aces=[1,14,27,40]
        twos=[2,15,28,41]
        jack=[11,24,37,50]
        quen=[12,25,38,51]
        D1scardChgd=False
        Discard,DeckTbl=self.CreatDiscard(DeckTbl)          #        for pin in range(XCardSlots):            Discard.append(DeckTbl[pin][0])
        fvDiscard=[]
        numofzerosinDiscard=0
        #Quantify auto card move to ace(foundation)-area == Discard[4-7]
            #if three ace(foundation)-area cards are gt> the other pull_fc=threefc#8,4,9,10=8
        for ick in range(4,8):
            fvDiscard.append(self.GetFaceValue(Discard[ick]))
            if Discard[ick] == 0:    numofzerosinDiscard += 1
        else:
            if numofzerosinDiscard == 4:
                numofzerosinDiscard -= 1
        MinDiscard = sum(fvDiscard)/(len(fvDiscard) - numofzerosinDiscard)
        if MinDiscard < 3:
            MinDiscard=2                #    MinDiscard=statistics.mean(fvDiscard)
        #check each colx[lengthcolx]==Discard[4-7]+1 if Discard[4-7] >0     #TODO: checkk if Discard[sub] > 0
        for sub in range(4,8):
            for gog in range(XCardSlots):                                            #gog is 0 thru 7  is colx
                if len(DeckTbl[gog])==0: DeckTbl[gog].append(0)#Fix Empty row
                lastCardInColumn = len(DeckTbl[gog]) - 1
                if Discard[sub] > 0 and self.GetFaceValue(Discard[sub]) <= MinDiscard:                                        
                    if DeckTbl[gog][lastCardInColumn] == Discard[sub] + 1:
                        PrintMoves.append(f"move: DeckTbl[{gog}][{lastCardInColumn}]({DeckTbl[gog][lastCardInColumn]},{Magic3[DeckTbl[gog][lastCardInColumn]]} to Discard[{sub}])")
                        Discard[sub] = DeckTbl[gog].pop(lastCardInColumn); D1scardChgd=True         #del DeckTbl[gog][lastCardInColumn]
                    else: 
                        continue
                elif DeckTbl[gog][lastCardInColumn] in aces and Discard[sub] == 0:
                    PrintMoves.append(f"move: DeckTbl[{gog}][{lastCardInColumn}]({DeckTbl[gog][lastCardInColumn]},{Magic3[DeckTbl[gog][lastCardInColumn]]} to Discard[{sub}])")
                    Discard[sub] = DeckTbl[gog].pop(lastCardInColumn); D1scardChgd=True
        #if D1scardChgd:
        #    for jin in range(XCardSlots):
        #        DeckTbl[jin][0]=Discard[jin]
        DeckTbl=self.DestryDiscard(Discard,DeckTbl)
        return DeckTbl   #,col0,col1,col2,col3,col4,col5,col6,col7            
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
    def GetFaceValue(self,realval):
        self.realval = realval
        if realval < 14:
            return realval # realval less than 14
        elif realval < 27: # realval greater than or equal 14 and less than 27
            return (realval - 13)
        elif realval < 40: # realval greater than or equal 27 and  less than 40
            return (realval - 26)
        else             : # realval greater than or equal 39 and  less than 53
            return (realval - 39)
    def IsValidMove(self, DeckTbl, popx,popy, endAddr,scrn):
        # TODO: Convert screen addr to a card or set of cards put up last-card then prev card until at beginAddr
        #if Discard[0]==0:
           #   Convert bosco, joseph to DeckTbl?
        bosco=popx
        joseph=popy
        #bosco,joseph=beginAddr   
        endax,enday =endAddr
        CardBegx=0
        CardBegy=0
        CardEndx=0
        CardEndy=0
        lastCardInCol = len(XPOS) - 1
        lastCardInRow = len(YPOS) - 1
        Status_Text=""
        D1scardChgd=False
        MultipleCards=False
        #739, 474  This still doesnt work!!!!!!!!!!!!!!!!!!         TEST outside card area

        Discard=[] 
        Discard,DeckTbl=self.CreatDiscard(DeckTbl)          #       for pin in range(XCardSlots):            Discard.append(DeckTbl[pin][0])

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
        #for esub in range(lastCardInRow):
        #    if enday > YPOS[esub] and enday <= YPOS[esub + 1]:
        #        CardEndy=min(esub-1, len(DeckTbl[CardEndx] - 1))
        #        break
        #else:
        #    CardEndy=min(lastCardInRow, len(DeckTbl[CardEndx]) - 1)
        if CardBegy > 0 and CardBegy < len(DeckTbl[CardBegx]) - 1 :
            MultipleCards=True
        if joseph <= DPOS:
            CardBegy=lastCardInRow+1
        if enday  <= DPOS:
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
        if Status_Text == "":           #        pass        # TODO Dont del the last entry in a col                 # See above: if CardBegx > (len(Discard)-1) or CardEndx > (len(Discard)-1):                   sukc2=0
            if  CardEndy==lastCardInRow+1 or  CardBegy==lastCardInRow+1:
            # TODO: process Discard-Row
                if CardBegx > 3 and CardBegy==lastCardInRow+1:
                    Status_Text = f"Can't move Foundation Cards"
                    suck=0
                elif CardBegy!=lastCardInRow+1 and CardEndy==lastCardInRow+1 and Discard[CardEndx]==0 and CardEndx < 4 and CardBegy > 0:
                        Discard[CardEndx]=DeckTbl[CardBegx].pop(CardBegy); D1scardChgd=True
                elif CardBegy!=lastCardInRow+1 and CardEndy==lastCardInRow+1 and Discard[CardEndx]==0 and CardEndx < 4 and CardBegy == 0:
                        Templike=DeckTbl[CardBegx][CardBegy]
                        DeckTbl[CardBegx][CardBegy]=0
                        Discard[CardEndx]=Templike; D1scardChgd=True
                elif CardBegy!=lastCardInRow+1 and CardEndy==lastCardInRow+1 and (DeckTbl[CardBegx][CardBegy] - Discard[CardEndx])==1 and CardEndx > 3 and CardBegy > 0:
                        Discard[CardEndx]=DeckTbl[CardBegx].pop(CardBegy); D1scardChgd=True
                elif CardBegy!=lastCardInRow+1 and CardEndy==lastCardInRow+1 and (DeckTbl[CardBegx][CardBegy] - Discard[CardEndx])==1 and CardEndx > 3 and CardBegy ==0:
                        PrintMoves.append(f"move: DeckTbl[{CardBegx}][{CardBegy}]({DeckTbl[CardBegx][CardBegy]},{Magic3[DeckTbl[CardBegx][CardBegy]]} to Discard[{CardEndx}])")
                        Templike=DeckTbl[CardBegx][CardBegy]
                        DeckTbl[CardBegx][CardBegy]=0       #TODO: Does this really work
                        Discard[CardEndx]=Templike; D1scardChgd=True
                elif CardBegx < 4:
                    if   CardBegy == lastCardInRow+1 and CardEndy != lastCardInRow+1 and Discard[CardBegx]==0:
                        Status_Text = f"No card to move"
                    elif CardBegy == lastCardInRow+1 and CardEndy != lastCardInRow+1 and DeckTbl[CardEndx][CardEndy] == 0:
                        DeckTbl[CardEndx][CardEndy]=Discard[CardBegx]
                        Discard[CardBegx]=0; D1scardChgd=True
                    elif CardBegy == lastCardInRow+1 and CardEndy != lastCardInRow+1 and (Magic1[Discard[CardBegx]]==DeckTbl[CardEndx][CardEndy] or Magic2[Discard[CardBegx]]==DeckTbl[CardEndx][CardEndy]):
                        DeckTbl[CardEndx].append(Discard[CardBegx])
                        Discard[CardBegx]=0; D1scardChgd=True
                    elif CardBegy == lastCardInRow+1 and CardEndy == lastCardInRow+1 and Discard[CardBegx] == Discard[CardEndx]+1:
                        Discard[CardEndx]=Discard[CardBegx]
                        Discard[CardBegx]=0; D1scardChgd=True
                    #TODO: Need to be able to move from Discard 0-3 to Discard 4-7 if appropriate
       #deck[CardBegx][CardBegy]
            elif DeckTbl[CardBegx][CardBegy]==0:
                Status_Text = f"No card to move"
            elif DeckTbl[CardBegx][CardBegy] > 26 and DeckTbl[CardEndx][CardEndy] > 26:
                Status_Text = "Same Black Suit"
            elif DeckTbl[CardBegx][CardBegy] < 27 and DeckTbl[CardEndx][CardEndy] < 27 and DeckTbl[CardEndx][CardEndy] != 0:
                Status_Text = "Same Red   Suit"
            else:
                print(f"{Magic1[(DeckTbl[CardBegx][CardBegy])]=},    {Magic2[(DeckTbl[CardBegx][CardBegy])]=}",end="    ")
                print(f"{DeckTbl[CardEndx][CardEndy]=}")
                if Status_Text == "" and (DeckTbl[CardEndx][CardEndy]==0 or Magic1[(DeckTbl[CardBegx][CardBegy])] == DeckTbl[CardEndx][CardEndy] or Magic2[(DeckTbl[CardBegx][CardBegy])] == DeckTbl[CardEndx][CardEndy]):
                    #pass            #TODO: Need to check all cards under selected cardBegxy MOVE DeckTbl from cardbegxy cardendxy    
                    if MultipleCards:
                        Discard,DeckTbl,CardBegx, CardBegy, CardEndx, CardEndy, Status_Text=self.MoveMultipleCards(Discard,DeckTbl,CardBegx, CardBegy, CardEndx, CardEndy, Status_Text)
                    else:
                        TempBegy=CardBegy
                        NumofFreeDiscardZeros=Discard[0:4].count(0)
                        NumofFreeDeckTblZeros=0
                        if len(DeckTbl[CardEndx])==1 and DeckTbl[CardEndx][CardEndy] == 0:    DeckTbl[CardEndx].pop(0)
                        for pogo in range(8):
                            if len(DeckTbl[pogo])==1 and DeckTbl[pogo][0]==0: 
                                NumofFreeDeckTblZeros +=1
                        numofwhileLoops=1
                        lenOfBegCol =len(DeckTbl[CardBegx]) - 1
                        if TempBegy < lenOfBegCol: 
                            numofwhileLoops=lenOfBegCol-TempBegy    #7-x=3   ?-x=3-7?x=-3+7?01234567or12345678 sub=5 len(DeckTbl[CardBegx])-sub=8-5
                            if numofwhileLoops > NumofFreeDiscardZeros + NumofFreeDeckTblZeros:
                                Status_Text = "Not Enough Free Spaces for move"
                            else:
                               if lenOfBegCol==0 or numofwhileLoops ==0:
                                   DeckTbl[CardEndx].append(DeckTbl[CardBegx][CardBegy])
                                   DeckTbl[CardBegx][CardBegy]=0
                               else:
                                   for logo in range(numofwhileLoops):
                                       DeckTbl[CardEndx].append(DeckTbl[CardBegx].pop(TempBegy+logo))
                        else:
                            if lenOfBegCol==0:
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
        DeckTbl=self.DestryDiscard(Discard,DeckTbl)      #if  D1scardChgd:            for jin in range(XCardSlots):               DeckTbl[jin][0]=Discard[jin]
        returnBool=Status_Text == ""            #    if Status_Text == "":           #
        return returnBool, DeckTbl, CardBegx, CardBegy, CardEndx, CardEndy, Status_Text, scrn    #Discard,deck,beginAddr,endAddr    else:        return False, Discard, DeckTbl, CardBegx, CardBegy, CardEndx, CardEndy, Status_Text    #Discard,deck,beginAddr,endAddr
    def MoveMultipleCards(Discard,DeckTbl,CardBegx, CardBegy, CardEndx, CardEndy, Status_Text):
        TempBegy=CardBegy
        NumofFreeDiscardZeros=Discard[0:4].count(0)
        NumofFreeDeckTblZeros=0
        if len(DeckTbl[CardEndx])==1 and DeckTbl[CardEndx][CardEndy] == 0:    DeckTbl[CardEndx].pop(0)
        for pogo in range(XCardSlots):
            if len(DeckTbl[pogo])==1 and DeckTbl[pogo][0]==0: 
                NumofFreeDeckTblZeros +=1
        numofwhileLoops=1
        lenOfBegCol =len(DeckTbl[CardBegx]) - 1
        if TempBegy < lenOfBegCol: 
            numofwhileLoops=lenOfBegCol-TempBegy    #7-x=3   ?-x=3-7?x=-3+7?01234567or12345678 sub=5 len(DeckTbl[CardBegx])-sub=8-5
            if numofwhileLoops > NumofFreeDiscardZeros + NumofFreeDeckTblZeros:
                Status_Text = "Not Enough Free Spaces for move"
            else:
                if lenOfBegCol==0 or numofwhileLoops ==0:
                    DeckTbl[CardEndx].append(DeckTbl[CardBegx][CardBegy])
                    DeckTbl[CardBegx][CardBegy]=0
                else:
                    for logo in range(numofwhileLoops):
                        DeckTbl[CardEndx].append(DeckTbl[CardBegx].pop(TempBegy+logo))
        else:
            if lenOfBegCol==0:
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
           #   elif DeckTbl[CardEndx][CardEndy]==0:
           #Check if EmptySlots<= NumCardsInSelectedAJ69Cache:
           #True Move them Else Don't Move

        return Discard,DeckTbl,CardBegx, CardBegy, CardEndx, CardEndy, Status_Text
# Setting up color objects
class screan(pygame.sprite.Sprite):
    def __init__(self,DeckTbl):
        pygame.init()
        # Declaring namedtuple()   
        self.Begpos = namedtuple('BeginPos',['beginx','beginy'])   
        self.Enditp = namedtuple('EndPos',['endx','endy'])         
        self.BLUE  = (0, 0, 255)
        self.RED   = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.LIGHTGREY=(100,100,100)             
        self.font = pygame.font.Font(None, 32)
        self.input_box = pygame.Rect(40, 900, 140, 32)   
        #    Rect(left, top, width, height) -> Rect   
        #    clock = pg.time.Clock()        self.deck = d
        self.Status_Text=""
        self.FPS = 30
        self.FramePerSec = pygame.time.Clock();              
        self.x = 12      # x coordnate of image
        self.y = 70      # y coordinate of image         card_widtht=card_width+x            i=0#1
        self.color_active = pygame.Color('dodgerblue2')
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color = self.color_inactive
        self.active = False
        self.text = ''
        self.done = False
        self.card_width =212
        self.card_height=292
        self.width = 1860
        self.height =1000    
        self.pathrb=f'C:/Users/Brice/source/repos/LearningPy/LearningPy/cardimagesRB/'
        self.SCREEN = pygame.display.set_mode((self.width,self.height))        
        #TODO: ADD SCREEN Logic fill screen,event handling ect blit flip ect
        self.SCREEN.fill(self.WHITE)        #        Status_Text=""
        #self.Deck = deck(DeckTable,self.SCREEN)
        self.DEckTble=DeckTbl
        
        DeckTbl,self.Status_Text,self.SCREEN = self.fillScreen(DeckTbl,self.Status_Text,self.SCREEN)
    def fillScreen(self,DeckTbl,Status_Text,SCREEN):
        Status_Text="";     countofAcesSkipped=0;       CurrentBick=0
        #returnTrue, Discard, DeckTbl, CardBegx, CardBegy, CardEndx, CardEndy, self.Status_Text=Deck.IsVal idMove(Discard, DeckTbl, self.Begpos, self.Enditp)
        #didyouwin,self.SCREEN= self.Have YouWon(Discard,DeckTbl,self.SCREEN)
        if self.Status_Text=="" or self.Status_Text=="Congratulations! You Win!":         #screen.fill((30, 30, 30))                      # Render the current text.
            #pass            #TODO: Actually move the card(s)
            self.SCREEN.fill(self.WHITE)
            pygame.display.set_caption("Brice's Free Cell")
            pygame.draw.line(self.SCREEN, self.RED, (XPOS[0],DPOS), (EPOS,DPOS))
            xxx,yyy,SCREEN = self.getScreenSize(SCREEN)
            print(f"{xxx=}, {yyy=}, {SCREEN=}")    #xxx=1860, yyy=1000, SCREEN=<Surface(1860x1000x32 SW)>
            #if didyouwin:    #Moved to a function            #    self.Status_Text = "Congratulations! You Win!"
            #    self.txt_surface = self.font.render(self.Status_Text, True, self.BLACK)                 # Resize the box if the text is too long.
            #    self.tsWidth = max(200, self.txt_surface.get_width()+10)            #    self.input_box.w = self.tsWidth                                                 # Blit the text.
            #    self.SCREEN.blit(self.txt_surface, (self.input_box.x+5, self.input_box.y+5))       # Blit the input_box rect.
            #    pygame.draw.rect(self.SCREEN, self.color, self.input_box, 2)            #    lit1=f"{pathrb}{str(53)}.png"            #    PenguinImage = pygame.image.load(lit1).convert()                 
            #    for lous in range(8):            #        self.SCREEN.blit(PenguinImage, (XPOS[lous],YPOS[0]))
            #else:
            #    Discard,DeckTbl = self.CheckDiscard(Discard,DeckTbl)   #,col0,col1,col2,col3,col4,col5,col6,col7)
            #for g,h in enumerate(Discard):
            #    lit1=f"{pathrb}{str(h)}.png";    IsThereADiscard = True;    #    PenguinImage = pygame.image.load(lit1).convert()    #    self.SCREEN.blit(PenguinImage, (XPOS[g],1))  
            
            for lick in range(8):
                for bick in range(len(DeckTbl[lick])):
                    #if DeckTbl[lick][bick] == 0:                    #    lit1=f"{pathrb}{str(53)}.png"                    #else:
                    lit1=f"C:/Users/Brice/source/repos/LearningPy/LearningPy/cardimagesRB/{str(DeckTbl[lick][bick])}.png"
                    PenguinImage = pygame.image.load(lit1).convert()                 
                    if bick ==len(DeckTbl[lick]) - 1 and DeckTbl[lick][bick]  in aces:
                        countofAcesSkipped +=1
                    else:
                        #CurrentBick=bick       
                        LastYPOS=len(YPOS)-1
                        if bick > LastYPOS:
                            CurrentBick+=YPOS[LastYPOS]+(SpaceBetweenCardY*(bick - LastYPOS))#+SpaceBetweenCardY)
                            self.SCREEN.blit(PenguinImage, (XPOS[lick],CurrentBick))         #    courtx.append(newx)    courty.append(y*y_modifier)         #    i=i+1
                        else:
                            self.SCREEN.blit(PenguinImage, (XPOS[lick],YPOS[bick]))
            print(f"countofAcesSkipped={countofAcesSkipped}")
            #Discard,DeckTbl = CheckDiscard(Discard,DeckTbl)   #,col0,col1,col2,col3,col4,col5,col6,col7)
            
            running = True 
            IsThereADiscard = False
            pygame.display.flip() # paint screen one time
        else:
            #if 'click' in num1_button.handle Event(event):
            #    if dice == 1:
            #        text = font.render("You Win!", 1, (0, 0, 0))
            #        screen.blit(text, (155, 255))
            self.txt_surface = self.font.render("                                     ", True, self.BLACK)
            self.txt_surface = self.font.render(self.Status_Text, True, self.BLACK)                 # Resize the box if the text is too long.
            tsWidth = max(200, self.txt_surface.get_width()+10)
            self.input_box.w = tsWidth                                                 # Blit the text.
            self.SCREEN.blit(self.txt_surface, (self.input_box.x+5, self.input_box.y+5))       # Blit the input_box rect.
            pygame.draw.rect(self.SCREEN, self.color, self.input_box, 2)
        
        return DeckTbl,Status_Text,SCREEN 
    def getScreenSize(self,SCREEN):
        self.scrn = SCREEN
        xxx, yyy = self.scrn.get_size()
        return xxx,yyy,SCREEN
    def handleEvent(self,DeckTbl,running,InitGame):
        if not InitGame:
            InitGame=True       #SCREEN = pygame.display.set_mode(width,height)
            screen.SCREEN.fill(screen.WHITE)
            DeckTbl,screen.Status_Text,screen.SCREEN = screen.fillScreen(DeckTbl,screen.Status_Text,screen.SCREEN)
    
        pygame.display.update()
        for event in pygame.event.get():
            self.Status_Text=""
            if event.type == QUIT:
                print(PrintMoves);          self.running = False;           sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                popx,popy=event.pos
                self.BeginPos = (popx,popy)
                self.shit=popx
                self.ship=popy
                self.Status_Text="";        print(f"mous down @ {popx},{popy}")
                #TODO: check if there is a place to move card(s) and enough
                #isv alidmove(Move=False)
            elif event.type == MOUSEBUTTONUP:
                self.handleMouseUp(DeckTbl,self.shit,self.ship,event,Decl)                #        InitGame=True;     
            elif event.type == MOUSEMOTION:
                qopx,qopy=event.pos     #            popy=event.y                #print(f'mouseMove @ {popx},{popy}')
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):                    print('left;')
                if event.key == pygame.K_RIGHT or event.key == ord('d'):                    print('right;')
                if event.key == pygame.K_UP or event.key == ord('w'):                    print('jump;')

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):                    print('left stop;')
                if event.key == pygame.K_RIGHT or event.key == ord('d'):                    print('right stop;')
                if event.key == pygame.K_UP or event.key == ord('w'):                    print('jump stop;')

                if event.key == ord('q'):
                    print(PrintMoves)
                    running = False  
                    #pygame.quit()
                    #sys.exit()

        self.FramePerSec.tick(self.FPS)
        return DeckTbl,running,InitGame
           # pygame.quit()
    def handleMouseUp(self,DeckTbl,popx,popy,event,Decl):
        opox,opoy = event.pos
        but1=event.button
        #shit=Begpos[0]
        #ship=Begpos[1]
        #self.oop=(shit,ship)
        self.Enditp=(opox,opoy)
        countofAcesSkipped=0
        CurrentBick=0
        if but1==1:
            print(f'mous up   @ {self.Enditp[0]},{self.Enditp[1]}')
            Status_Text=""
            returnTrue, DeckTbl, CardBegx, CardBegy, CardEndx, CardEndy, self.Status_Text,self=Decl.IsValidMove(DeckTbl, popx,popy, self.Enditp,self)
            didyouwin,DeckTbl,self.SCREEN= Decl.HaveYouWon(DeckTbl,self.SCREEN)
            if self.Status_Text=="" or self.Status_Text=="Congratulations! You Win!":         #screen.fill((30, 30, 30))                      # Render the current text.
                #pass            #TODO: Actually move the card(s)
                self.SCREEN.fill(self.WHITE)
                pygame.display.set_caption("Brice's Free Cell")
                if didyouwin:
                    DeckTbl,self.Status_Text,self.SCREEN = self.fillScreen(DeckTbl,self.Status_Text,self.SCREEN)
                    self.Status_Text = "Congratulations! You Win!"
                    self.txt_surface = self.font.render(self.Status_Text, True, self.RED)                 # Resize the box if the text is too long.
                    tsWidth = max(200, self.txt_surface.get_width()+10)
                    self.input_box.w = tsWidth                                                 # Blit the text.
                    self.input_box.y += 890
                    self.SCREEN.blit(self.txt_surface, (XPOS[0] + 32, 908 ))       #self.input_box.y+5 Blit the input_box rect.
                    pygame.draw.rect(self.SCREEN, self.color, self.input_box, 2)
                    lit1=f"C:/Users/Brice/source/repos/LearningPy/LearningPy/cardimagesRB/{str(0)}.png"
                    PenguinImage = pygame.image.load(lit1).convert()                 
                    for lous in range(8):
                        self.SCREEN.blit(PenguinImage, (XPOS[lous],YPOS[1]))
                else:
                    DeckTbl = Decl.CheckDiscard(DeckTbl)   #,col0,col1,col2,col3,col4,col5,col6,col7)
                    DeckTbl,self.Status_Text,self.SCREEN = self.fillScreen(DeckTbl,self.Status_Text,self.SCREEN)
            
#Deck=deck(DeckTable,Discard,SCREEN)
DeclTbl=[]
Decl=deck(DeckTable)

screen=screan(Decl.DeckTbl)

print(f"{type(screen)=}, {DeckTable=}, {Decl.DeckTbl=}, {col0=}")
DeclTbl.append(col0);       DeclTbl.append(col1)
DeclTbl.append(col2);       DeclTbl.append(col3)
DeclTbl.append(col4);       DeclTbl.append(col5)
DeclTbl.append(col6);       DeclTbl.append(col7);       print(f"{DeclTbl=}")
print(f"col0=>7{col0}{col1}{col2}{col3}{col4}{col5}{col6}{col7}")
print(f"DeclTbl==Decl.DeckTbl={DeclTbl==Decl.DeckTbl}")
#gameLoop
running=True;   pygame.init(); j=-1; InitGame=False
while running:
    if not InitGame:
        InitGame=True       #SCREEN = pygame.display.set_mode(width,height)
        screen.SCREEN.fill(screen.WHITE)
        DeckTbl,screen.Status_Text,screen.SCREEN = screen.fillScreen(Decl.DeckTbl,screen.Status_Text,screen.SCREEN)
        DeckTbl=Decl.DeckTbl
    pygame.display.update()
    DeckTbl,running,InitGame=screen.handleEvent(DeckTbl,running,InitGame)
    screen.FramePerSec.tick(screen.FPS)
                #TODO: put Discard at top of page b) merge Discard into DeckTbl
pygame.quit()
        # for jck in range(XCardSlots):
        #     for kck in range(len(DeckTbl[jck])):
        #         j+=1
        #         lit1=f"{pathrb}{str(DeckTbl[jck][kck])}.p ng"
        #         if j > 43 and DeckTbl[jck][kck] in aces:
        #             pass
        #         else:
        #             pimage= pygame.image.load(lit1).convert()
        #             SCREEN.blit(lit1, (XPOS[jck],YPOS[kck]))
#d = Dog('Fido')
#e = Dog('Buddy')
#d.add_trick('roll over')
#e.add_trick('play dead')
#print(d.tricks)                        #['roll over']
#print(e.tricks)                        #['play dead']

