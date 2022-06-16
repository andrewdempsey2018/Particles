import pygame
import math

class Particle:
    def __init__(self, x, y, speedX, speedY, life, img):
        self.xPos = x
        self.yPos = y
        self.sprite = pygame.image.load("assets/gfx/" + img)
        self.sprite.set_colorkey((255,0,255))
        self.moveSpeedX = speedX
        self.moveSpeedY = speedY
        self.life = life

    def __init__(self, x, y, speedX, speedY, life):
        self.xPos = x
        self.yPos = y
        self.moveSpeedX = speedX
        self.moveSpeedY = speedY
        self.life = life

    def move(self, interpolation):
        self.xPos += self.moveSpeedX * interpolation
        self.yPos += self.moveSpeedY * interpolation

    def arc(self, interpolation):
        self.xPos += self.moveSpeedX * interpolation
        self.yPos += self.moveSpeedY * interpolation