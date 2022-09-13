import pygame
import sys
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

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

black = (0, 0, 0)
peach = (255, 175, 128)
green = (0, 104, 55)
white = (255, 255, 255)

particles = []


NEW_SHAPE = pygame.USEREVENT
pygame.time.set_timer(NEW_SHAPE, 1000)

def updateGame(interpolation):

    for part in particles:
        part.orbit(interpolation, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    getInput()


def draw():
    screen.blit(background, (0, 0))

    for part in particles:
        pygame.draw.rect(screen, pygame.Color(10, 255, 10),
                         (part.xPos, part.yPos, part.size, part.size))

    pygame.display.flip()


def getInput():
    if pygame.mouse.get_pressed()[0]:
        particles.append(Particle(200, random.randrange(100, 200), 1, 1, 1, 8))


while game_is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == NEW_SHAPE:  
            particles.append(Particle(200, random.randrange(100, 200), 1, 1, 1, 8))

    loops = 0

    while pygame.time.get_ticks() > next_game_tick and loops < MAX_FRAMESKIP:
        updateGame(interpolation)
        getInput()
        next_game_tick += SKIP_TICKS
        loops += 1

    interpolation = float(pygame.time.get_ticks() +
                          SKIP_TICKS - next_game_tick) / float(SKIP_TICKS)
    draw()


