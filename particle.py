import math
import pygame

colours = {
    0: (255, 0, 0), #red
    1: (255, 165, 0), #orange
    2: (255, 255, 0), #yellow
    3: (0, 128, 0), #green
    4: (0, 0, 255), #blue
    5: (128, 0, 255), #purple
    6: (255, 0, 128) #pink

}

class Particle:
    def __init__(self, xPos=400, yPos=300, speedX=1, speedY=1, sizeX=3, sizeY=3,
                 orbitCenterX=400, orbitCenterY=300, radius=150, angle=0, colour=1):
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
        self.colour = colours[colour]

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
