import pygame

from agent import Agent
from trainer import DQNTrainer


WIDTH = 1000
HEIGHT = 700


def main():

    pygame.init()

    screen = pygame.display.set_mode(
        (WIDTH, HEIGHT)
    )

    clock = pygame.time.Clock()

    running = True

    blue = Agent(
        700,
        400,
        0,
        0,
        (0, 0, 255),
        20
    )

    red = Agent(
        200,
        300,
        0,
        0,
        (255, 0, 0),
        20
    )

    trainer = DQNTrainer()

    previous_distance = red.distance_to(blue)

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        state = red.get_state(blue)

        action = trainer.select_action(state)

        red.apply_action(action)

        red.update(WIDTH, HEIGHT)

        blue.vx = 1
        blue.vy = 0

        blue.update(WIDTH, HEIGHT)

        distance = red.distance_to(blue)

        reward = red.calculate_reward(
            blue,
            previous_distance
        )

        done = distance < 30

        next_state = red.get_state(blue)

        trainer.memory.add(
            state,
            action,
            reward,
            next_state,
            done
        )

        trainer.train_step()

        previous_distance = distance

        if done:

            print("PEGOU!")

            red.x = 200
            red.y = 300

            blue.x = 700
            blue.y = 400

            previous_distance = red.distance_to(blue)

        screen.fill((0, 0, 0))

        blue.draw(screen)
        red.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    trainer.save("dqn_red.pth")

    pygame.quit()


if __name__ == "__main__":
    main()
