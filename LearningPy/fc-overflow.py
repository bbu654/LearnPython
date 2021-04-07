import pygame
from collections import namedtuple

XCardSlots=8
XPOS = [12, 236, 460, 684, 908, 1132, 1356, 1580]
YPOS = [70, 130, 200, 270, 340, 410, 480]
SpaceBetweenCardY=60
DPOS = 800
#      no zero, ace   2h
Magic1 = (0,0,29,30,31,32,33,34,35,36,37,38,39,0,0,29,30,31,32,33,34,35,36,37,38,39,0,0, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,0,0, 3, 4, 5, 6, 7, 8, 9,10,11,12,13)
Magic2 = (0,0,42,43,44,45,46,47,48,49,50,51,52,0,0,42,43,44,45,46,47,48,49,50,51,52,0,0,16,17,18,19,20,21,22,23,24,25,26,0,0,16,17,18,19,20,21,22,23,24,25,26)
#Magic = ((0,0),(0,0),(29,42),(30,43),(31,44),(32,45),(33,46),(34,47),(35,48),(36,49),(37,50),(38,51),(39,52),(0,0),(29,42),(30,43),(31,44),(32,45),(33,46),(34,47),(35,48),(36,49),(37,50),(38,51),(39,52),(0,0),(3,16)(4,17),(5,18),(6,19),(7,20),(8,21),(9,22),(10,23),(11,24),(12,25),(13,26),(0,0),(3,16)(4,17),(5,18),(6,19),(7,20),(8,21),(9,22),(10,23),(11,24),(12,25),(13,26))
print(f"Magic1={Magic1} And len(Magic1={len(Magic1)}")
print(f"Magic2={Magic2} And len(Magic2={len(Magic2)}")
Magic3 = ("Zero","Ah","2h","3h","4h","5h","6h","7h","8h","9h","Th","Jh","Qh","Kh","Ad","2d","3d","4d","5d","6d","7d","8d","9d","Td","Jd","Qd","Kd","As","2s","3s","4s","5s","6s","7s","8s","9s","Ts","Js","Qs","Ks","Ac","2c","3c","4c","5c","6c","7c","8c","9c","Tc","Jc","Qc","Kc")
king=[13,26,39,52]
PrintMoves = []
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

class deck():
    def fillScreen(self,DeckTbl,Discard,Status_Text,SCREEN):
        LastYPOSi= len(YPOS) - 1
        didyouwin,DeckTbl,Discard,SCREEN= self.HaveYouWon(DeckTbl,Discard,SCREEN)
        if Status_Text=="" or Status_Text=="Congratulations! You Win!":         #screen.fill((30, 30, 30))                      # Render the current text.
            #pass            #TODO: Actually move the card(s)
            SCREEN.fill(self.WHITE)
            pygame.display.set_caption("Brice's Free Cell")
            if didyouwin:
                self.Status_Text = "Congratulations! You Win!"
                self.txt_surface = self.font.render(Status_Text, True, self.BLACK)                 # Resize the box if the text is too long.
                tsWidth = max(200, self.txt_surface.get_width()+10)
                self.input_box.w = tsWidth                                                 # Blit the text.
                self.SCREEN.blit(self.txt_surface, (self.input_box.x+5, self.input_box.y+5))       # Blit the input_box rect.
                pygame.draw.rect(self.SCREEN, self.color, self.input_box, 2)
                lit1=f"{self.pathrb}str(53).png"
                PenguinImage = pygame.image.load(lit1).convert()                 
                for lous in range(8):
                    self.SCREEN.blit(PenguinImage, (XPOS[lous],YPOS[0]))
            else:
                DeckTbl,Discard,SCREEN = self.CheckDiscard(DeckTbl,Discard,SCREEN)   #,col0,col1,col2,col3,col4,col5,col6,col7)

        for pcl in range(XCardSlots):
            for qcl in range(len(DeckTbl[pcl])):
                if DeckTbl[pcl][qcl] > 0:
                    lit10=f"{self.pathrb}{str(DeckTbl[pcl][qcl])}.png"
                else:
                    lit10=f"{self.pathrb}53.png"
                CardImage = pygame.image.load(lit10).convert()
                if qcl > LastYPOSi: CurrentYPOS=YPOS[LastYPOSi]+(SpaceBetweenCardY*(qcl - LastYPOSi))
                else: CurrentYPOS=YPOS[qcl]
                SCREEN.blit(CardImage,(XPOS[pcl],CurrentYPOS))
        for g,h in enumerate(Discard):
            if h > 0:
                lit1=f"{self.pathrb}{str(h)}.png"
            else:
                lit1=f"C:/Users/Brice/source/repos/LearningPy/LearningPy/cardimagesRB/{str(53)}.png"
            PenguinImage = pygame.image.load(lit1).convert()
            SCREEN.blit(PenguinImage, (XPOS[g],DPOS))  
        pygame.display.flip()
        return DeckTbl,Discard,Status_Text,SCREEN
