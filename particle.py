import pygame
import math

class Particle:
    def __init__(self, x, y, speedX, speedY, life, size):
        self.xPos = x
        self.yPos = y
        self.moveSpeedX = speedX
        self.moveSpeedY = speedY
        self.life = life
        self.size = size

    def move(self, interpolation):
        self.xPos += self.moveSpeedX * interpolation
        self.yPos += self.moveSpeedY * interpolation