import sys, pygame
from button import Button
from play import play

# inicializo pygame
pygame.init()
# tamaño de ventana
size = 600, 900
screen = pygame.display.set_mode(size)

# Font
font = pygame.font.Font("freesansbold.ttf", 28)


def getFont(fontSize):
    return pygame.font.Font("freesansbold.ttf", fontSize)


# cargar imagenes
bg_image = pygame.image.load("img/background.png").convert_alpha()
pygame.display.set_icon(pygame.image.load("img/logo.png").convert_alpha())
player_sprite = pygame.image.load("img/Astronaut_Falling.png").convert_alpha()

# Menu principal
def main_menu():
    # titulo de la ventana
    pygame.display.set_caption("Space Fall")
    while True:
        screen.blit(bg_image, (0, 0))
        screen.blit(bg_image, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = getFont(75).render("Space Fall", True, "#ffffff")
        MENU_RECT = MENU_TEXT.get_rect(center=(250, 140))

        PLAY_BUTTON = Button(
            image=pygame.image.load("img/play.png"),
            pos=(300, 350),
            text_input="Jugar",
            font=getFont(50),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        TUTORIAL_BUTTON = Button(
            image=pygame.image.load("img/quit.png"),
            pos=(300, 480),
            text_input="Tutorial",
            font=getFont(40),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        QUIT_BUTTON = Button(
            image=pygame.image.load("img/quit.png"),
            pos=(300, 610),
            text_input="Salir del juego",
            font=getFont(30),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        screen.blit(MENU_TEXT, MENU_RECT)
        screen.blit(
            pygame.transform.flip(
                pygame.transform.scale(player_sprite, (120, 120)), True, False
            ),
            (430, 60),
        )
        for button in [PLAY_BUTTON, TUTORIAL_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if TUTORIAL_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pass
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
