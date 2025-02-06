import pygame

from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_RECOIL, 
    PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN,
    PLAYER_FRICTION, SCREEN_WIDTH, SCREEN_HEIGHT,
    P1_DOWN, P1_LEFT, P1_RIGHT, P1_SHOOT, P1_UP,
    P2_DOWN, P2_LEFT, P2_RIGHT, P2_SHOOT, P2_UP)
from shot import Shot

class Player1(CircleShape):

    def __init__(self, x: int, y: int, weapon: str):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.weapon = weapon
        self.recharge = 0
        self.speed = pygame.Vector2(0, 0)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        #Color changes from red to white when the gun is in cooldown.
        colour = (255, 255 - self.recharge/PLAYER_SHOOT_COOLDOWN*255, 255 - self.recharge/PLAYER_SHOOT_COOLDOWN*255)
        pygame.draw.polygon(screen, colour, self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        #Handle key presses
        self.handle_keys(dt)

        #apply friction, update position
        self.speed *= PLAYER_FRICTION
        self.position += self.speed
        
        #cooldown for shots
        if self.recharge != 0:
            self.recharge = max(0, self.recharge - dt)

        #Edge collision
        if self.position.x - self.radius <= 0:
            self.speed.x *= -1
            self.position += self.speed
        elif self.position.x + self.radius >= SCREEN_WIDTH:
            self.speed.x *= -1
            self.position += self.speed
        elif self.position.y - self.radius <= 0:
            self.speed.y *= -1
            self.position += self.speed
        elif self.position.y + self.radius >= SCREEN_HEIGHT:
            self.speed.y *= -1
            self.position += self.speed
    
    def move(self, dt):
        self.speed += pygame.Vector2(0, 1).rotate(self.rotation) * dt * PLAYER_SPEED

    def handle_keys(self, dt):
        """Handles feedback for pressing keys"""
        keys = pygame.key.get_pressed()

        if keys[P1_LEFT]:
            self.rotate(-dt)
        if keys[P1_RIGHT]:
            self.rotate(dt)
        if keys[P1_UP]:
            self.move(dt)
        if keys[P1_DOWN]:
            self.move(-dt)
        if keys[P1_SHOOT]:
            self.shoot()
        
    
    def shoot(self):
        if self.recharge == 0:
            
            if self.weapon == "Single shot":

                # Cooldown after firing.
                self.recharge = PLAYER_SHOOT_COOLDOWN / 3

                # Fire a single shot
                shot = Shot(self.position.x, self.position.y)
                shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_SHOOT_SPEED

                #apply recoil to the player
                recoil = pygame.Vector2(0,1).rotate(self.rotation + 180) * PLAYER_RECOIL * 0.5
                self.speed += recoil


            if self.weapon == "Shotgun":

                # Cooldown after firing.
                self.recharge = PLAYER_SHOOT_COOLDOWN

                #Fire 3 shots in a spread
                velocity = pygame.Vector2(0, 1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
                for i in [-1, 0 ,1]:
                    shot = Shot(self.position.x, self.position.y)
                    shot.velocity = velocity.rotate(15 * i)

                #apply recoil to the player
                recoil = pygame.Vector2(0,1).rotate(self.rotation + 180) * PLAYER_RECOIL
                self.speed += recoil
            


class Player2(Player1):

    def __init__(self, x: int, y: int, weapon: str):
        super().__init__(x, y, weapon)

    def handle_keys(self, dt):
        """Handles feedback for pressing keys"""
        keys = pygame.key.get_pressed()

        if keys[P2_LEFT]:
            self.rotate(-dt)
        if keys[P2_RIGHT]:
            self.rotate(dt)
        if keys[P2_UP]:
            self.move(dt)
        if keys[P2_DOWN]:
            self.move(-dt)
        if keys[P2_SHOOT]:
            self.shoot()