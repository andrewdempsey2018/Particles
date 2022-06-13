import pygame


class Particle:
    def __init__(self, x, y, speedX, speedY):
        self.xPos = x
        self.yPos = y
        self.sprite = pygame.image.load("assets/gfx/white.bmp")
        self.sprite.set_colorkey((255,0,255))
        self.moveSpeedX = speedX
        self.moveSpeedY = speedY

    def move(self, interpolation):
        self.xPos += self.moveSpeedX * interpolation
        self.yPos += self.moveSpeedY * interpolation