import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH

pygame.font.init()
title_font = pygame.font.SysFont("Arial", 90)
menu_font = pygame.font.SysFont("Arial", 48)

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

    title_text = title_font.render("Asteroids", True, (255, 255, 255) )

    # Menu has three options: "One player", "Two players", "Quit". Use UP and DOWN and ENTER to choose.
    # 'Choice' arrow updates it's position.
    if choice == 1:
        one_player = menu_font.render("< One player >", True, (255, 255, 255) )
        two_players = menu_font.render(" Two players ", True, (255, 255, 255) )
        quit_text = menu_font.render(" Quit ", True, (255, 255,255) )
    elif choice == 2:
        one_player = menu_font.render(" One player ", True, (255, 255, 255) )
        two_players = menu_font.render("< Two players >", True, (255, 255, 255) )
        quit_text = menu_font.render(" Quit ", True, (255, 255,255) )
    elif choice == 3:
        one_player = menu_font.render(" One player ", True, (255, 255, 255) )
        two_players = menu_font.render(" Two players ", True, (255, 255, 255) )
        quit_text = menu_font.render("< Quit >", True, (255, 255,255) )
    
    lines.extend([title_text, one_player, two_players, quit_text])

    #blit each line menu line
    lines: list[pygame.Surface]
    for i, line in enumerate(lines):
        rect = line.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT / 4 + i*100))
        screen.blit(line, rect)

    # Info text at the bottom of the screen
    info_text = menu_font.render("P1: WASD + Space | P2: Arrows + Period", True, (255, 255, 255) )
    info_rect = info_text.get_rect( center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 40) )
    screen.blit(info_text, info_rect)

    pygame.display.flip()