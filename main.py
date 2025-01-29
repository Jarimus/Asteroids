import pygame
from time import sleep

from constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from circleshape import CircleShape
from players import Player1, Player2
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from menu import menu_screen

def main_loop(player_count):
    

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
    if player_count == 2:
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

        dt = time.tick(FPS) / 1000

        pygame.display.flip()



if __name__ == "__main__":
    #initialization
    pygame.init()
    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player_count = menu_screen(screen)
    
    main_loop(player_count)