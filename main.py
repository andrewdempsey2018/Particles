from shutil import move
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
        part.arc(interpolation)
        part.life -= 1
        if part.life == 0:
            arcGroup.remove(part)
            

    getInput()

def draw():
    screen.blit(background, (0, 0))

    for part in moveGroup:
        pygame.draw.rect(screen, pygame.Color("cyan2"), (part.xPos, part.yPos, 2, 2))

    for part in arcGroup:
        pygame.draw.rect(screen, pygame.Color("red"), (part.xPos, part.yPos, 2, 2))

    pygame.display.flip()

def getInput():
    if pygame.key.get_pressed()[pygame.K_q]:
        moveGroup.append(Particle(random.randrange(0,800),random.randrange(0,10),random.randrange(-2,5),random.randrange(5,9),random.randrange(1,200)))

    if pygame.key.get_pressed()[pygame.K_w]:
        arcGroup.append(Particle(random.randrange(0,800),random.randrange(0,10),2,random.randrange(5,9),random.randrange(1,200)))


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