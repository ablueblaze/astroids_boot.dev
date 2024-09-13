import pygame

# Base class for game objects


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision_check(self, circle_object):
        if self.position.distance_to(circle_object.position) < self.radius + circle_object.radius:
            return True
        return False

# Each CircleShape's position property is a pygame.Vector2.
#     Use its distance_to method to calculate the distance between the two shapes.
# After the update step in your game loop,
#   iterate over all of the objects in your asteroids group.
#     Check if any of them collide with the player.
#         If a collision is detected, the program should print Game over!
#     and immediately exit the program.
