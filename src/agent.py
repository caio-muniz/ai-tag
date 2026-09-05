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

        self.speed = 2

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.x), int(self.y)),
            self.size
        )

    def update(self, border_x, border_y):
        self.x += self.vx
        self.y += self.vy

        self.check_bounds(border_x, border_y)

    def check_bounds(self, border_x, border_y):

        if self.x >= border_x - self.size:
            self.x = border_x - self.size
            self.vx = -abs(self.vx)

        if self.x <= self.size:
            self.x = self.size
            self.vx = abs(self.vx)

        if self.y >= border_y - self.size:
            self.y = border_y - self.size
            self.vy = -abs(self.vy)

        if self.y <= self.size:
            self.y = self.size
            self.vy = abs(self.vy)

    def distance_to(self, agent):
        dx = self.x - agent.x
        dy = self.y - agent.y

        return math.sqrt(dx**2 + dy**2)

    def get_state(self, alvo):
        dx = alvo.x - self.x
        dy = alvo.y - self.y

        return [dx, dy]

    def apply_action(self, action):

        if action == 0:
            self.vx = 0
            self.vy = self.speed

        elif action == 1:
            self.vx = 0
            self.vy = -self.speed

        elif action == 2:
            self.vx = self.speed
            self.vy = 0

        elif action == 3:
            self.vx = -self.speed
            self.vy = 0

    def calculate_reward(self, alvo, distancia_anterior):
        distancia_atual = self.distance_to(alvo)

        if distancia_atual < distancia_anterior:
            return 1
        else:
            return -1
