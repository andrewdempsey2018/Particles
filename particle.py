import math
import pygame

RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 255)
PINK = (255, 0, 128)


class Particle:
    def __init__(self, x, y, speedX, speedY, life, size, orbitCenterX, orbitCenterY, radius):
        self.xPos = x
        self.yPos = y
        self.size = size
        self.speedX = speedX
        self.speedY = speedY
        self.life = life
        self.angle = 0
        self.orbitCenterX = orbitCenterX
        self.orbitCenterY = orbitCenterY
        self.radius = radius

    def move(self, interpolation):
        self.xPos += self.speedX * interpolation
        self.yPos += self.speedY * interpolation

    def orbit(self, interpolation):
        self.angle += 0.025 * interpolation
        self.xPos = (self.orbitCenterX + math.cos(self.angle) * self.radius)
        self.yPos = (self.orbitCenterY + math.sin(self.angle) * self.radius)

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW,
                         (self.xPos, self.yPos, self.size, self.size))
