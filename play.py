import pygame

BLANCO = (255, 255, 255)
size = 600, 900
screen = pygame.display.set_mode(size)

#set FPS
clock = pygame.time.Clock()
FPS = 60

#cargar imagenes
bg_image = pygame.image.load("img/background.png").convert_alpha()
player_sprite = pygame.image.load("img/Astronaut_Falling.png").convert_alpha()

#Variables
GRAVITY = 1                                                             #Esta variable se encarga de modificar el valor de la gravedad

#scrolling bg
def draw_bg(bg_scroll):
  screen.blit(bg_image, (0,0 + bg_scroll))                              #Usa dos fondos p/ dar continuidad, cuando llega al tope de ambos, reinicia el bg_scroll y vuelve a empezar desde 0
  screen.blit(bg_image, (0, -900 + bg_scroll))

class Player():                                                         #Clase del jugador 
  def __init__(self, x, y):
    self.image = pygame.transform.scale(player_sprite, (80,80))         #Inicializa y reescala el sprite
    self.height = 75
    self.width = 40        
    self.rect = pygame.Rect(0, 0, self.width, self.height)              #Agrega un rectangulo para colisiones
    self.rect.center = (x,y)                                            #Posiciona este rectangulo en las coordenadas iniciales
    self.vel_y = 0
    self.flip = False  

  def move(self):                                                       #Dependiendo de que tecla se toca:
    scroll = 0
    dx = 0 
    dy = 0

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
      dx -= 12
      self.flip = True
    if key[pygame.K_d]:
      dx += 12
      self.flip = False
    if key[pygame.K_SPACE]:
      dy = 0
      self.vel_y = -20

    #Seteo gravedad
    self.vel_y += GRAVITY
    dy += self.vel_y

    #delimitar el movimiento para evitar cruzar los margenes verticales
    if self.rect.bottom + dy > 900:
      dy = 0      #TEST: para no caer en el vacio, se frena la velocidad de caída
    
    #delimitar el movimiento para evitar cruzar los margenes laterales
    if self.rect.left + dx <0:
      dx = -self.rect.left
    if self.rect.right + dx > 600:
      dx = 600 - self.rect.right

    if self.rect.top <= 200:
      if self.vel_y < 0:
        scroll = -dy

    #actualizo el valor de movimiento por variables almacenando movimiento en pixeles
    self.rect.x += dx
    self.rect.y += dy + scroll

    return scroll

  def draw(self):                                                       #Funcion dedicada a imprimir el sprite // Dependiendo su direccion, se flipea el sprite
    screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 20, self.rect.y - 5))
    pygame.draw.rect(screen, BLANCO, self.rect, 2)

def play():
  # Font
  font = pygame.font.Font('freesansbold.ttf',28)
  score = 0
  scroll = 0
  bg_scroll = 0

  # comienzo del juego
  running = True
  score += 1
  scoreDisplay = font.render("Puntuación: " + str(score), True, (255,255,255))
  screen.blit(scoreDisplay,(10,10))
  player = Player(300, 750)                                               #Inicializa al Player en X=300 Y=750
  while running:

    clock.tick(FPS)                                                       #Setea los FPS a 60
    scroll = player.move()                                                #Agrega funcionalidad de movimiento en la clase Player
    bg_scroll += scroll                                                   #Esta variable va sumando de manera continua el progreso del scroll
    if bg_scroll >= 900:
      bg_scroll =0
    draw_bg(bg_scroll)                                                       #Imprimir fondo
    player.draw()                                                         #Imprimir sprites

    #pygame.draw.line(screen, BLANCO, (0, 200), (600, 200))                #Linea que indica cuando debe empezar a mover la camara (Scroll) TEST

    # capturador de eventos
    for event in pygame.event.get():
      # detección de salida de ventana
      if event.type == pygame.QUIT:
        run = False
        # salir de pygame
        pygame.quit()

    pygame.display.update()