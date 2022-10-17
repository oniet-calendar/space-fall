import pygame

def tutorial():
    quit_game = False
    size = 600, 900
    screen = pygame.display.set_mode(size)
    tutorial_bg = pygame.image.load("img/bg_tutorial.png").convert_alpha()
    screen.blit(tutorial_bg, (0,0))
    while not quit_game:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    quit_game = True
        pygame.display.update()
