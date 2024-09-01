# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    # Game loop
    while True:
        # Watches for the close button to be pressed
        # Closes the app when it is detected
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fills the screen with black
        screen.fill("black")
        # Refreshess the screen every loop
        pygame.display.flip()

        # passing the FPS to the clock object
        game_clock.tick(60)


if __name__ == "__main__":
    main()
