import sys, pygame
from particle import Particle

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

x = Particle(10,10,10,10)

particles = []

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

def updateGame(interpolation):
    x.move(interpolation)

    for part in particles:
        part.move(interpolation)

    getInput()

def draw():
    screen.blit(background, (0, 0))
    screen.blit(x.sprite, (x.xPos, x.yPos))

    for part in particles:
        screen.blit(part.sprite, (part.xPos, part.yPos))
    pygame.display.flip()

def getInput():
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        particles.append(Particle(10,10,10,10))

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        pass

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