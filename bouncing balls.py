import sys, pygame,random

from pygame.locals import*

 

pygame.init()

white = 255,255,255
background = [(255,255,255),(0, 255, 0),(255, 255, 0),(0, 0, 128),(138,51,36),(220,20,60)]
 

width = 800

height =700

pygame.display.set_caption("Bouncing ball")

 

size1 = width, heigth = 1,7

speed1 = [2,2]

screen = pygame.display.set_mode(size1)

clock1 = pygame.time.Clock()

ball1 = pygame.image.load("ball1.png")

ballrect1 = ball1.get_rect()

 

size2 = width, heigth = 900,700

speed2 = [3,3]

screen = pygame.display.set_mode(size2)

clock2 = pygame.time.Clock()

ball2 = pygame.image.load("ball1.png")

ballrect2 = ball2.get_rect()

 

while 1:

    clock1.tick(50)

    clock2.tick(80)

    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()

 

    ballrect1 = ballrect1.move(speed1)

    if ballrect1.left < 0 or ballrect1.right > width:

        speed1[0] = -speed1[0]
        screen.fill(background[random.randint(1,5)])
        pygame.display.flip()

    if ballrect1.top < 0 or ballrect1.bottom > height:

        speed1[1] = -speed1[1]
        screen.fill(background[random.randint(1,5)])
        pygame.display.flip()

 

    ballrect2 = ballrect2.move(speed2)

    if ballrect2.left < 0 or ballrect2.right > width:

        speed2[0] = -speed2[0]
        screen.fill(background[random.randint(1,5)])
        pygame.display.flip()

    if ballrect2.top < 0 or ballrect2.bottom > height:

        speed2[1] = -speed2[1]
        screen.fill(background[random.randint(1,5)])
        pygame.display.flip()

 

    screen.fill(background[random.randint(1,5)])

    screen.blit(ball1, ballrect1)

    screen.blit(ball2, ballrect2)

    pygame.display.flip()