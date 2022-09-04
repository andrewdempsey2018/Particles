import pygame

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load("assets/gfx/block.bmp")

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))