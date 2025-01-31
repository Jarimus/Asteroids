import pygame, sys
from time import sleep

from constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE_FONT
from circleshape import CircleShape
from players import Player1, Player2
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from ui import menu_screen, score_track

def main_loop(player_count):
    

    time = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    players = pygame.sprite.Group()
    score = 0

    #Init players
    Player1.containers = (updatable, drawable, players)
    Player2.containers = (updatable, drawable, players)
    if player_count == 2:
        player1 = Player1(SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2)
    else:
        player1 = Player1(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    if player_count == 2:
        player2 = Player2(SCREEN_WIDTH * 2 / 3, SCREEN_HEIGHT / 2)
    else:
        player2 = None

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
                    game_over(score)
        #check for collision (shot-asteroid):
        shot: Shot; asteroid: Asteroid
        for shot in shots:
            for asteroid in asteroids:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
                    score += 1
        
        #check for collision (player - player):
        if player2 and player1.collision(player2):
            p1_p2_v1 = pygame.Vector2.normalize( pygame.Vector2(player1.position.x - player2.position.x, player1.position.y - player2.position.y) )
            p1_p2_sum = pygame.Vector2.length( player1.speed - player2.speed )
            player1.speed = p1_p2_v1 * p1_p2_sum * 0.5
            player2.speed = - p1_p2_v1 * p1_p2_sum * 0.5

        #draw screen
        screen.fill( (0,0,0) )
        for sprite in drawable:
            sprite.draw(screen)
        
        #draw ui
        score_track(screen, score)

        dt = time.tick(FPS) / 1000

        pygame.display.flip()

def game_over(score: int):
    print(f"Game over! You scored {score} points!")
    game_over_text = TITLE_FONT.render("Game Over!", True, (255, 100, 100))
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(game_over_text, game_over_rect)
    pygame.display.flip()
    sleep(2)
    pygame.display.quit()
    pygame.quit()
    sys.exit()



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
