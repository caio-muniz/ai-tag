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

    #cérebro do vermelho
    red_trainer = DQNTrainer()

    #cérebro do azul
    blue_trainer = DQNTrainer()

    previous_distance_red = red.distance_to(blue)
    previous_distance_blue = blue.distance_to(red)

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        state_red = red.get_state(blue)
        state_blue = blue.get_state(red)

        action_red = red_trainer.select_action(state_red)
        action_blue = blue_trainer.select_action(state_blue)

        red.apply_action(action_red)
        blue.apply_action(action_blue)


        red.update(WIDTH, HEIGHT)
        blue.update(WIDTH, HEIGHT)


        distance = red.distance_to(blue)


        reward_red = red.calculate_reward(
            blue,
            previous_distance_red
        )

        reward_blue = blue.calculate_flee_reward(
            red,
            previous_distance_blue
        )


        done = distance < 30

        # Recompensa pela captura
        if done:
            reward_red += 100
            reward_blue -= 100


        next_state_red = red.get_state(blue)
        next_state_blue = blue.get_state(red)

        red_trainer.memory.add(
            state_red,
            action_red,
            reward_red,
            next_state_red,
            done
        )


        blue_trainer.memory.add(
            state_blue,
            action_blue,
            reward_blue,
            next_state_blue,
            done
        )


        red_trainer.train_step()
        blue_trainer.train_step()


        previous_distance_red = distance
        previous_distance_blue = distance


        if done:

            print(
                "PEGOU!",
                "Epsilon vermelho:",
                round(red_trainer.epsilon, 3),
                "Epsilon azul:",
                round(blue_trainer.epsilon, 3)
            )

            red.x = 200
            red.y = 300

            blue.x = 700
            blue.y = 400

            red.vx = 0
            red.vy = 0

            blue.vx = 0
            blue.vy = 0

            previous_distance_red = red.distance_to(blue)
            previous_distance_blue = blue.distance_to(red)


        screen.fill((0, 0, 0))

        blue.draw(screen)
        red.draw(screen)

        pygame.display.flip()

        clock.tick(60)


    red_trainer.save("dqn_red.pth")
    blue_trainer.save("dqn_blue.pth")

    pygame.quit()


if __name__ == "__main__":
    main()
