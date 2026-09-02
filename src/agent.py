import pygame
import math

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

    def check_bounds(self, borderX , borderY):
        if self.x >= borderX - self.size:
            self.x = borderX - self.size
            self.vx = -abs(self.vx)

        if self.x <= self.size:
            self.x = self.size
            self.vx = abs(self.vx)

        if self.y >= borderY - self.size:
            self.y = borderY - self.size
            self.vy = -abs(self.vy)

        if self.y <= self.size:
            self.y = self.size
            self.vy = abs(self.vy)

    def distance_to(self, agent):
        dx = self.x - agent.x
        dy = self.y - agent.y

        return math.sqrt(dx**2 + dy**2)

    def move_towards(self, alvo):
        dx = alvo.x - self.x
        dy = alvo.y - self.y

        distance = math.sqrt(dx**2 + dy**2)

        dx /= distance
        dy /= distance

        self.vx = dx * 2
        self.vy = dy * 2



