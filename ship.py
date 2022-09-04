import pygame

class Ship:
    def __init__(self, x, y, life):
        self.xPos = x
        self.yPos = y
        self.life = 5
        self.xSpeed = 5
        self.ySpeed = 5
        

    def move(self, interpolation):
        self.xPos += 5 * interpolation
        self.yPos += 5 * interpolation

    def draw(self, screen):
        pygame.draw.rect(screen, pygame.Color(10, 255, 10), (self.xPos, self.yPos, 20, 20))

    def getInput(self, interpolation):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.yPos -= 5 * interpolation
        
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.yPos += 5 * interpolation

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.xPos -= 5 * interpolation

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.xPos += 5 * interpolation
