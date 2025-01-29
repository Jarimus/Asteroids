import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN, PLAYER_FRICTION
from shot import Shot

class Player1(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.recharge = 0
        self.speed = pygame.Vector2(0, 0)

        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        colour = (255, 255 - self.recharge/PLAYER_SHOOT_COOLDOWN*255, 255 - self.recharge/PLAYER_SHOOT_COOLDOWN*255)
        pygame.draw.polygon(screen, colour, self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        #handle key press
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_v]:
            self.shoot()

        #apply friction, update position
        self.speed *= PLAYER_FRICTION
        self.position += self.speed * dt
        
        #cooldown for shots
        if self.recharge != 0:
            self.recharge = max(0, self.recharge - dt)
    
    def move(self, dt):
        self.speed += pygame.Vector2(0, 1).rotate(self.rotation) * dt * PLAYER_SPEED
        
    
    def shoot(self):
        if self.recharge == 0:
            self.recharge = PLAYER_SHOOT_COOLDOWN
            velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
            for i in [-1, 0 ,1]:
                shot = Shot(self.position.x, self.position.y)
                shot.velocity = velocity.rotate(15 * i)

class Player2(Player1):

    def __init__(self, x, y):
        super().__init__(x, y)
    
    def update(self, dt):
        #handle key press
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_PERIOD]:
            self.shoot()

        #apply friction, update position
        self.speed *= PLAYER_FRICTION
        self.position += self.speed * dt
        
        #cooldown for shots
        if self.recharge != 0:
            self.recharge = max(0, self.recharge - dt)