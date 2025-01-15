import pygame

from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #initialization
    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    time = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #Spawn player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Spawn asteroids
    Asteroid.containers = (asteroids, updatable, drawable)

    #Set asteroidfield where new asteroids can spawn
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    #main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return


        updatable.update(dt)

        screen.fill( (0,0,0) )
        for sprite in drawable:
            sprite.draw(screen)


        pygame.display.flip()
        dt = time.tick(FPS) / 1000


if __name__ == "__main__":
    main()