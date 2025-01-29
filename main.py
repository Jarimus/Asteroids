import pygame
from time import sleep

from constants import *
from circleshape import *
from players import *
from shot import *
from asteroid import *
from asteroidfield import AsteroidField

def main_loop():


    #initialization
    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    time = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    players = pygame.sprite.Group()

    #Init players
    Player1.containers = (updatable, drawable, players)
    Player2.containers = (updatable, drawable, players)
    player1 = Player1(SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2)
    player2 = Player2(SCREEN_WIDTH * 2 / 3, SCREEN_HEIGHT / 2)

    #Init asteroids
    Asteroid.containers = (asteroids, updatable, drawable)

    #Init asteroidfield (for asteroid spawning)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    #Init shots
    Shot.containers = (updatable, drawable, shots)

    #main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        #update positions
        updatable.update(dt)

        #check for collision (player-asteroid)
        player: CircleShape; asteroid: Asteroid
        for asteroid in asteroids:
            for player in players:
                if player.collision(asteroid):
                    print("Game over!")
                    sleep(1)
                    return
        
        #check for collision (shot-asteroid):
        shot: Shot; asteroid: Asteroid
        for shot in shots:
            for asteroid in asteroids:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

        #draw screen
        screen.fill( (0,0,0) )
        for sprite in drawable:
            sprite.draw(screen)


        pygame.display.flip()
        dt = time.tick(FPS) / 1000


if __name__ == "__main__":
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    main_loop()