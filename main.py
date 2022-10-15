import sys, pygame
from button import Button

# inicializo pygame
pygame.init()

# tamaño de ventana
size = 600, 900
screen = pygame.display.set_mode(size)

#set FPS
clock = pygame.time.Clock()
FPS = 60

#Variables
GRAVITY = 1                                                             #Esta variable se encarga de modificar el valor de la gravedad

# Font
font = pygame.font.Font('freesansbold.ttf',28)
def getFont(fontSize):
  return pygame.font.Font('freesansbold.ttf', fontSize)

# titulo de la ventana
pygame.display.set_caption("Space Fall")

#cargar imagenes
bg_image = pygame.image.load("./img/background.png").convert_alpha()
player_sprite = pygame.image.load("./img/Astronaut_Falling.png").convert_alpha()

#colores
BLANCO = (255, 255, 255)

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

    #actualizo el valor de movimiento por variables almacenando movimiento en pixeles
    self.rect.x += dx
    self.rect.y += dy

  def draw(self):                                                       #Funcion dedicada a imprimir el sprite // Dependiendo su direccion, se flipea el sprite
    screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 20, self.rect.y - 5))
    pygame.draw.rect(screen, BLANCO, self.rect, 2)                      #DEBUG // Imprime el box collision

def play():
  # comienzo del juego
  score = 0
  running = True
  player = Player(300, 750)                                               #Inicializa al Player en X=300 Y=750
  jumping = False
  while running:

    clock.tick(FPS)                                                       #Setea los FPS a 60
    player.move()                                                         #Agrega funcionalidad de movimiento en la clase Player
    screen.blit(bg_image, (0,0))                                          #Imprimir fondo
    player.draw()                                                         #Imprimir sprites
    score += 1
    scoreDisplay = font.render("Puntuación: " + str(score), True, (255,255,255))
    screen.blit(scoreDisplay,(10,10))

    # capturador de eventos
    for event in pygame.event.get():
      # detección de salida de ventana
      if event.type == pygame.QUIT:
        run = False
        # salir de pygame
        pygame.quit()

    pygame.display.update()

# Menu principal
def main_menu():
    while True:
        screen.blit(bg_image, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = getFont(100).render("Space Fall", True, "#ffffff")
        MENU_RECT = MENU_TEXT.get_rect(center=(300, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("img/play.png"), pos=(300, 350), 
                            text_input="Jugar", font=getFont(50), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("img/quit.png"), pos=(300, 480), 
                            text_input="Opciones", font=getFont(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("img/quit.png"), pos=(300, 610), 
                            text_input="Salir del juego", font=getFont(30), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pass
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
