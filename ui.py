import pygame, sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, MENU_FONT, TITLE_FONT, P1_DOWN, P1_UP, P1_SHOOT, P2_DOWN, P2_UP, P2_SHOOT
from time import sleep


def menu_screen(screen: pygame.Surface):

    #Status: tracks what to draw and when to proceed from the menus. settings stores settings. choice is used to navigate the menu.
    status = "menu"
    settings = {}
    choice = 1

    #Logic for the main menu of the game
    while status == "menu":
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and (event.key == P1_DOWN or event.key == P2_DOWN):
                choice = min( 3, choice + 1 )
            elif event.type == pygame.KEYDOWN and (event.key == P1_UP or event.key == P2_UP):
                choice = max( 1, choice - 1 )
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == P1_SHOOT or event.key == P2_SHOOT):
                if choice == 1:
                    status = "P2 ready" #this signifies in the weapon choice menu, that there is no player 2.
                    settings["player_count"] = choice
                    break
                elif choice == 2:
                    status = "Continue" #proceed to the weapon menu.
                    settings["player_count"] = choice
                elif choice == 3:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
    
        draw_menu(screen, choice)


    #short pause between menu screens
    sleep(0.5)

    p1_choice = 1
    p2_choice = 1
    
    #Logic for the weapon choice screen if new game is started
    while status != "Play":
        for event in pygame.event.get():

            #Player1 menu controls
            if event.type == pygame.KEYDOWN and event.key == P1_DOWN:
                p1_choice = min( 2, p1_choice + 1 )
            elif event.type == pygame.KEYDOWN and event.key == P1_UP:
                p1_choice = max( 1, p1_choice - 1 )

            elif event.type == pygame.KEYDOWN and event.key == P1_SHOOT:
                #Check if the other player is ready. If they are, start playing. Otherwise, set yourself as ready.
                if status == "P2 ready":
                    status = "Play"
                elif status != "P1 ready":
                    status = "P1 ready"

                #Save the weapon choice
                if p1_choice == 1:
                    settings["P1 weapon"] = "Single shot"
                elif p1_choice == 2:
                    settings["P1 weapon"] = "Shotgun"

            #Player2 menu controls
            if event.type == pygame.KEYDOWN and event.key == P2_DOWN:
                p2_choice = min( 2, p2_choice + 1 )
            elif event.type == pygame.KEYDOWN and event.key == P2_UP:
                p2_choice = max( 1, p2_choice - 1 )

            elif event.type == pygame.KEYDOWN and event.key == P2_SHOOT:
                #Check if the other player is ready. If they are, start playing. Otherwise, set yourself as ready.
                if status == "P1 ready":
                    status = "Play"
                elif status != "P2 ready":
                    status = "P2 ready"

                #Save the weapon choice
                if p2_choice == 1:
                    settings["P2 weapon"] = "Single shot"
                elif p2_choice == 2:
                    settings["P2 weapon"] = "Shotgun"
        
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
        
        #Draw the weapons menu
        if status != "Play":
            draw_choose_weapon_ui(screen, status, p1_choice, p2_choice)
    
    #Short pause so that the game does not begin with one player shooting
    sleep(0.5)
    return status, settings


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


def draw_choose_weapon_ui(screen: pygame.Surface, status, p1_choice: int, p2_choice: int):
    screen.fill( (0, 0, 0) )

    lines = []
    lines: list[pygame.Surface]

    title_text = TITLE_FONT.render("Choose a weapon", True, (255, 255, 255) )
    lines.append(title_text)

    # Menu has two options: "Single shot", "Shotgun". Use W and S and SPACE to choose.
    # 'Choice' arrow updates it's position.
    if status != "P1 ready":

        p1_text = MENU_FONT.render("Player 1:", True, (255, 255, 255) )

        if p1_choice == 1:
            p1_single_shot = MENU_FONT.render("< Single shot >", True, (255, 255, 255) )
            p1_shotgun = MENU_FONT.render(" Shotgun ", True, (255, 255, 255) )
        elif p1_choice == 2:
            p1_single_shot = MENU_FONT.render(" Single shot ", True, (255, 255, 255) )
            p1_shotgun = MENU_FONT.render("< Shotgun >", True, (255, 255, 255) )
    
        lines.extend([p1_text, p1_single_shot, p1_shotgun])
    
    if status != "P2 ready":

        p2_text = MENU_FONT.render("Player 2:", True, (255, 255, 255) )

        if p2_choice == 1:
            p2_single_shot = MENU_FONT.render("< Single shot >", True, (255, 255, 255) )
            p2_shotgun = MENU_FONT.render(" Shotgun ", True, (255, 255, 255) )
        elif p2_choice == 2:
            p2_single_shot = MENU_FONT.render(" Single shot ", True, (255, 255, 255) )
            p2_shotgun = MENU_FONT.render("< Shotgun >", True, (255, 255, 255) )
    
        lines.extend([p2_text, p2_single_shot, p2_shotgun])


    #Blit the elements
    for i, line in enumerate(lines):
        rect = line.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT / 6 + i*90))
        screen.blit(line, rect)

    pygame.display.flip()


def score_track(screen: pygame.Surface, score: int):
    score_text = MENU_FONT.render(f"Score: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect( center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 40))
    screen.blit(score_text, score_rect)