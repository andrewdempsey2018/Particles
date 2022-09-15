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
    def __init__(self, xPos=400, yPos=300, speedX=1, speedY=1, sizeX=3, sizeY=3,
                 orbitCenterX=400, orbitCenterY=300, radius=150, angle=0, colour=RED):
        self.xPos = xPos
        self.yPos = yPos
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.speedX = speedX
        self.speedY = speedY
        self.angle = angle
        self.orbitCenterX = orbitCenterX
        self.orbitCenterY = orbitCenterY
        self.radius = radius
        self.colour = colour

    def move(self, interpolation):
        self.xPos += self.speedX * interpolation
        self.yPos += self.speedY * interpolation

    def orbit(self, interpolation):
        self.angle += self.speedX * interpolation
        self.xPos = (self.orbitCenterX + math.cos(self.angle) * self.radius)
        self.yPos = (self.orbitCenterY + math.sin(self.angle) * self.radius)

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour,
                         (self.xPos, self.yPos, self.sizeX, self.sizeY))
