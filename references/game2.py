import sys, pygame
from player import Player
from level import Level
from camera import Camera

pygame.init()

screenWidth = 640
screenHeight = 480

size = width, height = screenWidth, screenHeight

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("assets/gfx/bg.bmp")

player = Player(200, 200)

TICKS_PER_SECOND = 60
SKIP_TICKS = 1000 / TICKS_PER_SECOND
MAX_FRAMESKIP = 5

next_game_tick = pygame.time.get_ticks()
loops = 0
interpolation = 0.0

game_is_running = True

brick = pygame.image.load("assets/gfx/brick.bmp")
brickXPos = 320
brickYPos = 240

cam = Camera()

def updateGame(interpolation):
    getInput()
    player.walk(interpolation)
    cam.offsetX = player.xPos - 320


def draw():
    screen.blit(bgImage, (0,0))
    screen.blit(player.sprite, (player.xPos - cam.offsetX, player.yPos))
    screen.blit(brick, (brickXPos - cam.offsetX, brickYPos))
    pygame.display.flip()

def getInput():
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        if player.walkSpeed > -5:
            player.walkSpeed -= 0.25

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        if player.walkSpeed < 5:
            player.walkSpeed += 0.25

    if not pygame.key.get_pressed()[pygame.K_LEFT] and not pygame.key.get_pressed()[pygame.K_RIGHT]:
        if player.walkSpeed < 0:
            player.walkSpeed += 0.25

        if player.walkSpeed > 0:
            player.walkSpeed -= 0.25
    

while game_is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    loops = 0

    while pygame.time.get_ticks() > next_game_tick and loops < MAX_FRAMESKIP:
        updateGame(interpolation)
        next_game_tick += SKIP_TICKS
        loops += 1

    interpolation = float(pygame.time.get_ticks() + SKIP_TICKS - next_game_tick ) / float( SKIP_TICKS )
    draw()