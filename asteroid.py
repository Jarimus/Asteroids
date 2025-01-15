import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt: float):
        self.position += self.velocity * dt

        if self.position.x < 0 - self.radius * 3 or self.position.x > SCREEN_WIDTH + self.radius * 3:
            self.kill()
        if self.position.y < 0 - self.radius * 3 or self.position.y > SCREEN_HEIGHT + self.radius * 3:
            self.kill()

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            split_angle = random.uniform(20, 50)
            velocity_left = self.velocity.rotate(-split_angle)
            velocity_right = self.velocity.rotate(split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = velocity_left * 1.2
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = velocity_right * 1.2
            self.kill()