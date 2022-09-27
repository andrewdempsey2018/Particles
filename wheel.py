from particle import Particle
import random


class Wheel:
    def __init__(self, parts):

        colour = random.randrange(0, 6)
        radius = random.randrange(10, 100)
        orbitCenterX = random.randrange(1, 800)
        orbitCenterY = random.randrange(1, 600)

        for angle in range(1, 360, 20):
            parts.append(Particle(sizeX=3, sizeY=3, speedX=0.0625, speedY=0, orbitCenterX=orbitCenterX,
                                  orbitCenterY=orbitCenterY, angle=angle, radius=radius, colour=colour))
