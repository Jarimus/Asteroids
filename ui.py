import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, MENU_FONT, TITLE_FONT

def menu_screen(screen: pygame.Surface):

    choice = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                choice = min( 3, choice + 1 )
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                choice = max( 1, choice - 1 )
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if choice != 3:
                    return choice #return 1 or 2 (the number of players)
                else:
                    quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                quit()
    
        draw_menu(screen, choice)

def draw_menu(screen: pygame.Surface, choice: int):

    screen.fill( (0, 0, 0) )

    lines = []

    title_text = TITLE_FONT.render("Asteroids", True, (255, 255, 255) )

    # Menu has three options: "One player", "Two players", "Quit". Use UP and DOWN and ENTER to choose.
    # 'Choice' arrow updates it's position.
    if choice == 1:
        one_player = MENU_FONT.render("< One player >", True, (255, 255, 255) )
        two_players = MENU_FONT.render(" Two players ", True, (255, 255, 255) )
        quit_text = MENU_FONT.render(" Quit ", True, (255, 255,255) )
    elif choice == 2:
        one_player = MENU_FONT.render(" One player ", True, (255, 255, 255) )
        two_players = MENU_FONT.render("< Two players >", True, (255, 255, 255) )
        quit_text = MENU_FONT.render(" Quit ", True, (255, 255,255) )
    elif choice == 3:
        one_player = MENU_FONT.render(" One player ", True, (255, 255, 255) )
        two_players = MENU_FONT.render(" Two players ", True, (255, 255, 255) )
        quit_text = MENU_FONT.render("< Quit >", True, (255, 255,255) )
    
    lines.extend([title_text, one_player, two_players, quit_text])

    #blit each line menu line
    lines: list[pygame.Surface]
    for i, line in enumerate(lines):
        rect = line.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT / 4 + i*100))
        screen.blit(line, rect)

    # Info text at the bottom of the screen
    info_text = MENU_FONT.render("P1: WASD + Space | P2: Arrows + R-Shift", True, (255, 255, 255) )
    info_rect = info_text.get_rect( center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 40) )
    screen.blit(info_text, info_rect)

    pygame.display.flip()

def score_track(screen: pygame.Surface, score: int):
    score_text = MENU_FONT.render(f"Score: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect( center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 40))
    screen.blit(score_text, score_rect)