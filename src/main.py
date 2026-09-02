import pygame
from agent import Agent

pygame.init()
screen = pygame.display.set_mode((1000, 700))
running = True

agent1 = Agent(400, 300, 1, 1, (255, 255, 0), 50)
agent2 = Agent(200, 100, 1, 3,(255, 255, 255), 10)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    agent1.check_bounds(1000,700)
    agent2.check_bounds(1000,700)

    agent1.update()
    agent2.update()
    

    screen.fill((0,0,0))

    agent1.draw(screen)
    agent2.draw(screen)

    pygame.display.flip()

pygame.quit()
