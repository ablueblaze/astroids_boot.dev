import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    pc = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        # Watches for the close button to be pressed
        # Closes the app when it is detected
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Key controls
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            # check for collisions
            if pc.collision_check(asteroid):
                print("hit")

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
