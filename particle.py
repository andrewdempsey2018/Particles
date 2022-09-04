class Particle:
    def __init__(self, x, y, speedX, speedY, life, size):
        self.xPos = x
        self.yPos = y
        self.size = size
        self.speedX = speedX
        self.speedY = speedY
        self.life = life
        

    def move(self, interpolation):
        self.xPos += self.moveSpeedX * interpolation
        self.yPos += self.moveSpeedY * interpolation