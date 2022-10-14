import sys, pygame

# inicializo pygame
pygame.init()

# tamaño de ventana
size = 600, 900
screen = pygame.display.set_mode(size)

# titulo de la ventana
pygame.display.set_caption("Space Jump")

#cargar imagenes
bg_image = pygame.image.load("bg.png").convert_alpha()

# comienzo del juego
running = True
while running:

  #imprimir fondo
  screen.blit(bg_image, (0,0))

  # capturador de eventos
  for event in pygame.event.get():
    # detección de salida de ventana
    if event.type == pygame.QUIT:
      run = False
      # salir de pygame
      pygame.quit()

  pygame.display.update()

