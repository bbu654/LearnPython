import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)    #The tree base colors are defined as:
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)         #By mixing two base colors we obtained more colors:
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)    #At the end of the event loop, we add the following:
spaceBetweenColY=70
global DeckTbl,RevHist,FwdHist
DeckTbl=[]
RevHist=[]
FwdHist=[]
class reverseforward:
    def __init__(self,DeckTbl) -> None:
        self.ReverseHistory=[]
        self.ForwardHistory=[]
        DeckTbl,RevHist,FwdHist=self.StowHistory(DeckTbl,self.ReverseHistory,self.ForwardHistory)
        if len(RevHist) > 0:
            for x in RevHist:    
                self.ReverseHistory.append(x)
        if len(FwdHist) > 0:
            for y in FwdHist:    
                self.ForwardHistory.append(y)
    def StowHistory(self,DeckTbl,RevHist,FwdHist):
        RevHist.append(DeckTbl)
        return DeckTbl,RevHist,FwdHist


revfwd=reverseforward(DeckTbl)
screen = pygame.display.set_mode((640, 240))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            screen.fill(YELLOW)
pygame.display.update()

pygame.quit()