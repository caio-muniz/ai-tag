import pygame

class Agent:
    def __init__(self, x, y, vx, vy, color, size):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.size = size

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def update(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy

