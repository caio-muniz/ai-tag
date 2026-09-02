import pygame
from agent import Agent

pygame.init()
screen = pygame.display.set_mode((1000, 700))
running = True

agent1 = Agent(400, 300, 0.4, 0, (255, 255, 0), 50)
agent2 = Agent(200, 100, 0.4, 1,(255, 255, 255), 10)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((0,0,0))
    agent1.draw(screen)
    agent2.draw(screen)
    agent1.update()
    agent2.update()

    pygame.display.flip()

pygame.quit()