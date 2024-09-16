import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)
        x, y = self.position
        new_asteroid_a = Asteroid(x, y, new_radius)
        new_asteroid_a.velocity = self.velocity.rotate(random_angle) * 1.2
        new_asteroid_b = Asteroid(x, y, new_radius)
        new_asteroid_b.velocity = self.velocity.rotate(-random_angle) * 1.2
