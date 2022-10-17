import pygame, sys, random

from play_music import play_music

BLANCO = (255, 255, 255)
size = 600, 900
screen = pygame.display.set_mode(size)

# set FPS
clock = pygame.time.Clock()
FPS = 60

# cargar imagenes
bg_image = pygame.image.load("img/background.png").convert_alpha()
player_sprite = pygame.image.load("img/Astronaut_Falling.png").convert_alpha()
asteroid_image = pygame.image.load("img/asteroid.png").convert_alpha()
asteroid_image2 = pygame.image.load("img/asteroid2.png").convert_alpha()
asteroid_image3 = pygame.image.load("img/asteroid3.png").convert_alpha()

# Variables
GRAVITY = 1  # Esta variable se encarga de modificar el valor de la gravedad

# scrolling bg
def draw_bg(bg_scroll):
    screen.blit(
        bg_image, (0, 0 + bg_scroll)
    )  # Usa dos fondos p/ dar continuidad, cuando llega al tope de ambos, reinicia el bg_scroll y vuelve a empezar desde 0
    screen.blit(bg_image, (0, -900 + bg_scroll))


class Asteroid(object):
    def __init__(self, type):
        self.type = type
        if self.type == 1:
            self.image = asteroid_image  # Inicializa y reescala el sprite
        if self.type == 2:
            self.image = asteroid_image2
        if self.type == 3: 
            self.image = asteroid_image3
        self.w = 64  # Dependiendo del rango, se puede multiplicar el tamaño para hacer asteroides mas grandes
        self.h = 64
        self.ranPoint = (
            random.randrange(5, 580),
            -15,
        )  # Donde spawnean los asteroides, entre un valor random del ancho de la pantalla y posicion 0 arriba
        self.x, self.y = self.ranPoint
        self.xv = 0                 #Velocidad horizontal en 0 asi salen de arriba
        self.yv = 1 * 3             # Velocidad vertical
        self.rect = pygame.Rect(
            self.x, self.y, 45, 45 
        )  # Agrega un rectangulo para colisiones
        self.rect.center = ((self.rect.width + 15 // 2, self.rect.height // 2))

    def draw(self, screen):
      screen.blit(self.image, (self.x, self.y))
      #pygame.draw.rect(screen, BLANCO, self.rect, 2)
      self.rect.x = self.xv + self.x
      self.rect.y += self.yv


class Player:  # Clase del jugador
    def __init__(self, x, y):
        self.image = pygame.transform.scale(
            player_sprite, (80, 80)
        )  # Inicializa y reescala el sprite
        self.height = 55
        self.width = 40
        self.rect = pygame.Rect(
            0, 0, self.width, self.height
        )  # Agrega un rectangulo para colisiones
        self.rect.center = (
            x,
            y,
        )  # Posiciona este rectangulo en las coordenadas iniciales
        self.vel_y = 0
        self.flip = False  # Inicia con la imagen flipped False
        self.cool_down_count = 0
        #jetpack_amount = 10

    def cool_down(self):
        if self.cool_down_count >= 10:                                  #Si se quiere modificar el tiempo de prevencion de spam, variar este y
            self.cool_down_count == 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def move(self):  # Dependiendo de que tecla se toca:
        scroll = 0
        dx = 0
        dy = 0
        self.cool_down()

        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx -= 12
            self.flip = True
        if key[pygame.K_d]:
            dx += 12
            self.flip = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.cool_down_count == 0:
                        self.vel_y = -20
                        self.cool_down_count = 1

                    if self.cool_down_count == 10:                                              #Si se quiere modificar el tiempo de prevencion de spam, variar este y
                        self.vel_y = -20
                        self.cool_down_count = 1

        # Seteo gravedad
        self.vel_y += GRAVITY
        dy += self.vel_y

        # delimitar el movimiento para evitar cruzar los margenes verticales // Pantalla de Perdiste
        if self.rect.bottom + dy > 900:
            pygame.quit()
            sys.exit()
            #dy = 0      #TEST: para no caer en el vacio, se frena la velocidad de caída

        # delimitar el movimiento para evitar cruzar los margenes laterales
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > 600:
            dx = 600 - self.rect.right

        if self.rect.top <= 200:
            if self.vel_y < 0:
                scroll = -dy

        # actualizo el valor de movimiento por variables almacenando movimiento en pixeles
        self.rect.x += dx
        self.rect.y += dy + scroll

        return scroll

    def draw(
        self,
    ):  # Funcion dedicada a imprimir el sprite // Dependiendo su direccion, se flipea el sprite
        screen.blit(
            pygame.transform.flip(self.image, self.flip, False),
            (self.rect.x - 20, self.rect.y - 5),
        )
        #pygame.draw.rect(screen, BLANCO, self.rect, 2)


def play():

    play_music()

    # Font
    font = pygame.font.Font("./fonts/Jost-Medium.ttf", 28)
    score = 0
    scroll = 0
    bg_scroll = 0
    asteroids = []
    asteroidCount = 0

    # comienzo del juego
    running = True

    player = Player(300, 400)  # Inicializa al Player en X=300 Y=400

    while running:

        clock.tick(FPS)  # Setea los FPS a 60
        asteroidCount += 1
        scroll = player.move()  # Agrega funcionalidad de movimiento en la clase Player
        bg_scroll += (
            scroll  # Esta variable va sumando de manera continua el progreso del scroll
        )

        if (
            bg_scroll >= 900
        ):  # Si se pasa la resolucion del primer fondo, reiniciar a 0 para volver a verlo al principio
            bg_scroll = 0
        draw_bg(bg_scroll)  # Imprimir fondo

        player.draw()  # Imprimir sprites

        for a in asteroids:
            a.draw(screen)
            a.x += a.xv
            a.y += a.yv

            if (player.rect.left >= a.x and player.rect.left <= a.x + a.w) or (             #Deteccion de colisiones con asteroides
                player.rect.right + player.width >= a.x
                and player.rect.right + player.width <= a.x + a.w
            ):

                if (player.rect.top >= a.y and player.rect.top <= a.y + a.h) or (
                    player.rect.bottom + player.height >= a.y
                    and player.rect.bottom + player.height <= a.y + a.h
                ):
                    pygame.quit()                                                           #En caso de morir, correrá esta linea // Pantalla de Perdiste

        #pygame.draw.line(
            #screen, BLANCO, (0, 200), (600, 200)
        #)  # Linea que indica cuando debe empezar a mover la camara (Scroll) TEST

        if asteroidCount % 50 == 0:
            ran = random.choice([1, 1, 1, 2, 2, 3])
            asteroids.append(Asteroid(ran))

        # capturador de eventos
        for event in pygame.event.get():
            # detección de salida de ventana
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        score += 1
        scoreDisplay = font.render("Puntuación: " + str(score), True, (255, 255, 255))
        screen.blit(scoreDisplay, (10, 10))
        pygame.display.update()
