import pygame
import player
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    start_x = SCREEN_WIDTH / 2
    start_y = SCREEN_HEIGHT / 2

    # This causes a type error due to passing to many args
    # pc = player.Player(start_x, start_y, PLAYER_RADIUS)
    pc = player.Player(start_x, start_y)
    # Game loop
    while True:
        # Watches for the close button to be pressed
        # Closes the app when it is detected
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        # Fills the screen with black
        screen.fill("black")

        # Key controls
        pc.update(dt)

        # Draw the character on the scree
        pc.draw(screen)

        # Refreshess the screen every loop
        pygame.display.flip()

        # passing the FPS to the clock object
        dt = game_clock.tick(60) / 1000



if __name__ == "__main__":
    main()
