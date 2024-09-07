import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

#    print("Starting asteroids!")

    # Groups for cleaner code base
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    # Instanciating the pc and adding it to the groups
    pc = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    # Game loop
    while True:
        # Watches for the close button to be pressed
        # Closes the app when it is detected
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Key controls
        for obj in updatable:
            obj.update(dt)

        # Fills the screen with black
        screen.fill("black")

        # Draw the character on the scree
        for obj in drawable:
            obj.draw(screen)

        # Refreshess the screen every loop
        pygame.display.flip()

        # passing the FPS to the clock object
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
