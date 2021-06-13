import pygame,sys
class GameObject:
    def __init__(self, image, width, height, speed=0):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(width, height)
    def move(self,apos):
        mx= apos.x;    my=apos.y
        mx-=10
        my+=10
        self.pos.x=mx;self.pos.y=my    #        self.pos = self.pos.move(self.pos, self.speed)
        if self.pos.right > 600:            
            self.pos.left = 0
        if self.pos.bottom > 440:
            self.pos.top = 0
screen = pygame.display.set_mode((640, 480))
player = pygame.image.load('C:/Users/Brice/source/Resources/Python/player.jpg').convert()
background = pygame.image.load('C:/Users/Brice/source/Resources/Python/background.jpg').convert()
screen.blit(background, (0, 0))
objects = []
#for x in range(5):                    #create 10 objects</i>
#    o = GameObject(player, x*40, x)
#    objects.append(o)
while 1:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseDX, mouseDY) = pygame.mouse.get_pos()              
            d= GameObject(player,mouseDX,mouseDY)
            objects.append(d)
        if event.type == pygame.MOUSEBUTTONUP:
            (mouseUX, mouseUY) = pygame.mouse.get_pos()              
            u= GameObject(player,mouseUX,mouseUY)
            objects.append(u)
        if event.type == pygame.MOUSEMOTION:
            (mouseMX, mouseMY) = pygame.mouse.get_pos()              
            m= GameObject(player,mouseMX,mouseMY)
            objects.append(m)

    for o in objects:
        screen.blit(background, o.pos, o.pos)
    for o in objects:
        o.move(o.pos)
        print(f"{o.pos=}, {o.pos.x=}, {o.pos.y=}")
        screen.blit(o.image, o.pos)
    pygame.display.update()
    pygame.time.delay(100)