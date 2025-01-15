import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH

class Shot(CircleShape):
    def __init__(self, x, y, radius=SHOT_RADIUS):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt: float):
        self.position += self.velocity * dt
        
        if self.position.x < 0 - self.radius or self.position.x > SCREEN_WIDTH + self.radius:
            self.kill()
        if self.position.y < 0 - self.radius or self.position.y > SCREEN_HEIGHT + self.radius:
            self.kill()