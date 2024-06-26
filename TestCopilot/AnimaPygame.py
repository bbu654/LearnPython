import pygame
from random import randrange

MAX_STARS = 250
STAR_SPEED = 2

def initStars(screen):
    """Create the Starfield"""
    global stars
    stars = []
    for i in range(MAX_STARS):
        #A Star is represented as a list w this format: [X,Y]
        star = [randrange(0, screen.get_width() - 1),randrange(0, screen.get_height() - 1)]
        stars.append(star)

def moveNDrawStars(screen):
    """Move and Draw the Stars"""
    global stars
    for star in stars:
        star[1] += STAR_SPEED
        if star[1] >= screen.get_height():
            star[1] = 0
            star[0] = randrange(0,639)
        screen.set_at(star, (255,255,255))

def main():
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Starfield Simulation")
    clock = pygame.time.Clock()
    initStars(screen)
    while True:
        """Lock the framerate at 50 FPS"""
        clock.tick(50)
        """Handle events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        moveNDrawStars(screen)
        pygame.display.flip()
if __name__ == "__main__":
    main()