import math


class Particle:
    def __init__(self, x, y, speedX, speedY, life, size):
        self.xPos = x
        self.yPos = y
        self.size = size
        self.speedX = speedX
        self.speedY = speedY
        self.life = life
        self.angle = 0

    def move(self, interpolation):
        self.xPos += self.speedX * interpolation
        self.yPos += self.speedY * interpolation

    def orbit(self, interpolation, originX, originY):
        self.angle += 0.025 * interpolation
        self.xPos = (originX + math.cos(self.angle) * 150)
        self.yPos = (originY + math.sin(self.angle) * 150)

        #https://franzeus.medium.com/math-for-circular-object-movement-in-a-game-cae101474a65
        #B.x = A.x + cos(a) * radius;
        #B.y = A.y + sin(a) * radius;

        # X := originX + cos(angle)*radius;
        # Y := originY + sin(angle)*radius;
        # https://gamedev.stackexchange.com/questions/9607/moving-an-object-in-a-circular-path
        # x=a+(r*cos θ)
        # y=b+(r*sin θ)
