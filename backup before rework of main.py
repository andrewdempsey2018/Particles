import sys, pygame
from particle import Particle
import random

pygame.init()

screenWidth = 800
screenHeight = 600

size = width, height = screenWidth, screenHeight

screen = pygame.display.set_mode(size)

TICKS_PER_SECOND = 60
SKIP_TICKS = 1000 / TICKS_PER_SECOND
MAX_FRAMESKIP = 5

next_game_tick = pygame.time.get_ticks()
loops = 0
interpolation = 0.0

game_is_running = True

moveGroup = []
arcGroup = []
bounceGroup = []
explodeGroup = []
updownGroup = []

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))


def updateGame(interpolation):

    for part in moveGroup:
        part.move(interpolation)
        part.life -= 1
        if part.life == 0:
            moveGroup.remove(part)

    for part in arcGroup:
        part.move(interpolation)
        part.life -= 1
        if part.life == 0:
            arcGroup.remove(part)

    for part in bounceGroup:
        part.move(interpolation)
        if part.xPos >= screenWidth or part.xPos <= 0:
            part.moveSpeedX = part.moveSpeedX * -1
        if part.yPos >= screenHeight or part.yPos <= 0:
            part.moveSpeedY = part.moveSpeedY * -1

    for part in explodeGroup:
        part.move(interpolation)
        part.life -= 1
        if part.life == 0:
            explodeGroup.remove(part)

    for part in updownGroup:
        part.move(5)
        part.moveSpeedX += 0.025
        if part.moveSpeedX >= 00:
            part.moveSpeedX = -10
        part.moveSpeedY += 0.025
        if part.moveSpeedY >= 10:
            part.moveSpeedY = -10
        if part.xPos >= screenWidth or part.xPos <= 0:
            part.moveSpeedX = part.moveSpeedX * -1
        if part.yPos >= screenHeight or part.yPos <= 0:
            part.moveSpeedY = part.moveSpeedY * -1
            

    getInput()

def draw():
    screen.blit(background, (0, 0))

    for part in moveGroup:
        pygame.draw.rect(screen, pygame.Color(10, 255, 10), (part.xPos, part.yPos, part.size, part.size))

    for part in arcGroup:
        pygame.draw.rect(screen, pygame.Color(100, 25, 100), (part.xPos, part.yPos, part.size, part.size))
    
    for part in bounceGroup:
        pygame.draw.rect(screen, pygame.Color(200, 25, 10), (part.xPos, part.yPos, part.size, part.size))

    for part in explodeGroup:
        pygame.draw.rect(screen, pygame.Color(120, 125, 200), (part.xPos, part.yPos, part.size, part.size))

    for part in updownGroup:
        pygame.draw.rect(screen, pygame.Color(245, 245, 65), (part.xPos, part.yPos, part.size, part.size))

    pygame.display.flip()

def getInput():
    if pygame.key.get_pressed()[pygame.K_q]:
        moveGroup.append(Particle(random.randrange(0,800),random.randrange(0,10),random.randrange(-2,5),random.randrange(5,9),random.randrange(1,200), random.randrange(2,6)))

    if pygame.key.get_pressed()[pygame.K_w]:
        arcGroup.append(Particle(random.randrange(0,800),random.randrange(0,10),2,random.randrange(5,9),random.randrange(1,200), random.randrange(2,6)))

    if pygame.key.get_pressed()[pygame.K_e]:
        bounceGroup.append(Particle(random.randrange(0,800),random.randrange(0,10),2,random.randrange(5,9),random.randrange(1,200), random.randrange(5,9)))

    if pygame.key.get_pressed()[pygame.K_r]:
        bounceGroup.append(Particle(random.randrange(0,800),random.randrange(0,10),2,random.randrange(5,9),random.randrange(1,200), random.randrange(5,19)))

    if pygame.key.get_pressed()[pygame.K_a]:
        for part in bounceGroup:
            part.moveSpeedX = random.randrange(1,5)
            part.moveSpeedY = random.randrange(1,5)

    if pygame.mouse.get_pressed()[2]:
        for part in bounceGroup:
            if part.xPos > pygame.mouse.get_pos()[0]:
                part.xPos -= 1
            if part.xPos < pygame.mouse.get_pos()[0]:
                part.xPos += 1
            if part.yPos > pygame.mouse.get_pos()[1]:
                part.yPos -= 1
            if part.yPos < pygame.mouse.get_pos()[1]:
                part.yPos += 1

    if pygame.key.get_pressed()[pygame.K_s]:
        for part in bounceGroup:
            if part.xPos > pygame.mouse.get_pos()[0]:
                part.xPos = pygame.mouse.get_pos()[0]
            if part.xPos < pygame.mouse.get_pos()[0]:
                part.xPos = pygame.mouse.get_pos()[0]
            if part.yPos > pygame.mouse.get_pos()[1]:
                part.yPos = pygame.mouse.get_pos()[1]
            if part.yPos < pygame.mouse.get_pos()[1]:
                part.yPos = pygame.mouse.get_pos()[1]

    if pygame.key.get_pressed()[pygame.K_d]:
        for part in bounceGroup:
            part.xPos = random.randrange(0,screenWidth)
            part.yPos = random.randrange(0,screenHeight)

    if pygame.mouse.get_pressed()[0]:
        explodeGroup.append(Particle(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],2,random.randrange(5,9),random.randrange(1,200), random.randrange(3,5)))

    if pygame.key.get_pressed()[pygame.K_f]:
        explodeGroup.append(Particle(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],random.randrange(-10,10),random.randrange(-10,10),random.randrange(10,200), random.randrange(3,5)))

    if pygame.key.get_pressed()[pygame.K_g]:
        bounceGroup.append(Particle(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],random.randrange(-10,10),random.randrange(-10,10),random.randrange(10,200), random.randrange(3,10)))

    if pygame.key.get_pressed()[pygame.K_h]:
        updownGroup.append(Particle(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],random.randrange(-10,10),random.randrange(-10,10),random.randrange(10,200), random.randrange(3,10)))


while game_is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    loops = 0

    while pygame.time.get_ticks() > next_game_tick and loops < MAX_FRAMESKIP:
        updateGame(interpolation)
        getInput()
        next_game_tick += SKIP_TICKS
        loops += 1

    interpolation = float(pygame.time.get_ticks() + SKIP_TICKS - next_game_tick ) / float( SKIP_TICKS )
    draw()