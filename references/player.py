import pygame

class Player:
    def __init__(self, x, y):
        self.xPos = x
        self.yPos = y
        self.sprite = pygame.image.load("assets/gfx/player.bmp")
        self.sprite.set_colorkey((255,0,255))
        self.walkSpeed = 0

    def walk(self, interpolation):
        self.xPos += self.walkSpeed * interpolation
