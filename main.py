import sys, pygame

# inicializo pygame
pygame.init()

# tamaño de ventana
size = 800, 600
screen = pygame.display.set_mode(size)

# titulo de la ventana
pygame.display.set_caption("Space Jump")

# comienzo del juego
running = True
while running:
  # capturador de eventos
  for event in pygame.event.get():
    
    # detección de salida de ventana
    if event.type == pygame.QUIT:
      run = False

# salir de pygame
pygame.quit()
