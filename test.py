from multiprocessing.context import SpawnProcess
import pygame
import sys
from particle import Particle
import random

pygame.init()

screenWidth = 800
screenHeight = 600

RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 255)
PINK = (255, 0, 128)

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
        part.orbit(interpolation)

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
        for part in particles:
            part.radius -= 1

    if pygame.key.get_pressed()[pygame.K_w]:
        for part in particles:
            part.radius += 1

    if pygame.key.get_pressed()[pygame.K_e]:
        for part in particles:
            part.speedX += 0.0025

    if pygame.key.get_pressed()[pygame.K_r]:
        for part in particles:
            part.speedX -= 0.0025

    if pygame.key.get_pressed()[pygame.K_t]:
        for part in particles:
            part.sizeX -= 0.25
            part.sizeY -= 0.25

    if pygame.key.get_pressed()[pygame.K_y]:
        for part in particles:
            part.sizeX += 0.25
            part.sizeY += 0.25

    if pygame.key.get_pressed()[pygame.K_u]:
        for part in particles:
            part.orbitCenterX += 0.25


while game_is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == NEW_SHAPE:
            particles.append(Particle(sizeX=5, speedX=0.025))
            particles.append(Particle(sizeX=5, colour=BLUE,
                             orbitCenterX=200, orbitCenterY=200, radius=75, speedX=0.025))
            particles.append(Particle(sizeX=4, colour=GREEN,
                             orbitCenterX=100, orbitCenterY=100, radius=95, speedX=-0.025))
            particles.append(Particle(sizeX=5, colour=PINK,
                             orbitCenterX=300, orbitCenterY=300, radius=65, speedX=0.025))
            particles.append(Particle(sizeX=4, colour=PURPLE,
                             orbitCenterX=400, orbitCenterY=400, radius=105, speedX=-0.025))

    loops = 0

    while pygame.time.get_ticks() > next_game_tick and loops < MAX_FRAMESKIP:
        updateGame(interpolation)
        getInput()
        next_game_tick += SKIP_TICKS
        loops += 1

    interpolation = float(pygame.time.get_ticks() +
                          SKIP_TICKS - next_game_tick) / float(SKIP_TICKS)
    draw()
