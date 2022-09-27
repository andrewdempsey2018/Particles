from multiprocessing.context import SpawnProcess
import pygame
import sys
from particle import Particle
import random

from wheel import Wheel

pygame.init()

screenWidth = 800
screenHeight = 600

size = width, height = screenWidth, screenHeight

# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
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

particles = []


NEW_SHAPE = pygame.USEREVENT

pygame.time.set_timer(NEW_SHAPE, 1000)


def updateGame(interpolation):

    for part in particles:
        #part.move(interpolation)
        part.orbit(interpolation)
        #part.radius += 0.005

    getInput()


def draw():
    screen.blit(background, (0, 0))

    for part in particles:
        part.draw(screen)

    pygame.display.flip()


def getInput():
    if pygame.mouse.get_pressed()[0]:
        pass

    if pygame.key.get_pressed()[pygame.K_q]:
        pass


while game_is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == NEW_SHAPE:
            #particles.append(Particle(sizeX=3, sizeY=3, speedX=0.025, orbitCenterX=400, orbitCenterY=300, angle=20, radius=45, colour=GREEN))
            Wheel(particles)

    loops = 0

    while pygame.time.get_ticks() > next_game_tick and loops < MAX_FRAMESKIP:
        updateGame(interpolation)
        getInput()
        next_game_tick += SKIP_TICKS
        loops += 1

    interpolation = float(pygame.time.get_ticks() +
                          SKIP_TICKS - next_game_tick) / float(SKIP_TICKS)

    draw()
