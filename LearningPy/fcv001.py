import pygame, sys, random, os
from pygame.locals import *

 
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
card_width =200
card_height=292
# Setup a 300x300 pixel display with caption
width = 1800
height =800
horCardSlots=8
DISPLAYSURF = pygame.display.set_mode((width,height))
DISPLAYSURF.fill(WHITE)

pygame.display.set_caption("Display some stuff")
#istring=os.path.join("images","1.png")
shorty=[] 
courtx=[]
courty=[]
setOfNumbers = list(range(1,53))
#while len(setOfNumbers) < 53:
#    setOfNumbers.add(random.randint(1, 52))
#!random.shuffle(setOfNumbers)
print(setOfNumbers)
x = 12; # x coordnate of image
y = 70; # y coordinate of image
i=1
for j in setOfNumbers:
#while i<53:
    y_modifier= i//(horCardSlots+1)
    if i==horCardSlots+1:
        y_modifier=y_modifier+1    
    y_modifier=y_modifier+1
    shorty.append(y_modifier)
    x_modifier=i%(horCardSlots+1)
    newx=(x*x_modifier)
    newx=newx+(card_width*(x_modifier-1))
    lit1=f"C:/Users/Brice/source/repos/LearningPy/LearningPy/images/{str(j)}.png"
    PenguinImage = pygame.image.load(lit1).convert()
    DISPLAYSURF.blit(PenguinImage, (newx,y*y_modifier))
    i=i+1
#DISPLAYSURF.blit(PenguinImage, ( x,y)  ) # paint to screen

pygame.display.flip() # paint screen one time
#print(shorty) 
# Creating Lines and Shapes         asurf = pygame.image.load(os.path.join('images', '1.png'))
#pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (130,170))
#pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (170,170))
#pygame.draw.line(DISPLAYSURF, GREEN, (130,170), (170,170))
#pygame.draw.circle(DISPLAYSURF, BLACK, (100,50), 30)
#pygame.draw.circle(DISPLAYSURF, BLACK, (200,50), 30)
#pygame.draw.rect(DISPLAYSURF, RED, (100, 200, 100, 50), 2)
#pygame.draw.rect(DISPLAYSURF, BLACK, (110, 260, 80, 5))
running = True 
# Beginning Game Loop
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            sys.exit()
   
    FramePerSec.tick(FPS)

#loop over, quite pygame
pygame.quit()
