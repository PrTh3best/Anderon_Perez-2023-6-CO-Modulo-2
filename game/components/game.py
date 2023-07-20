import pygame
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, WHITE_COLOR
# game.utils.constants -> es un modulo donde tengo "objetos" en memoria como el BG (background)...etc
#   tambien tenemos valores constantes como el title, etc
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components.power_ups.power_up_handler import PowerUpHandler
from game.components import text_utils

# Game es la definicion de la clase (plantilla o molde para sacar objetos)
# self es una referencia que indica que el metodo o el atributo es de cada "objeto" de la clase Game
class Game:
    def __init__(self):
        pygame.init()# este es el enlace con la libreria pygame para poder mostrar la pantalla del juego
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler()
        self.bullet_handler = BulletHandler()
        self.power_up_handler = PowerUpHandler()
        self.score = 0
        self.number_death = 0

    def run(self):
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        # esta expression es la llamada a un metodo pygame.event.get() que devuelve un "iterable"
        for event in pygame.event.get(): # con el for sacamos cada evento del "iterable"
            if event.type == pygame.QUIT: # pygame.QUIT representa la X de la ventana
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset()

# aca escribo ALGO de la logica "necesaria" -> repartimos responsabilidades entre clases
    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(user_input, self.bullet_handler)
            self.enemy_handler.update(self.bullet_handler)
            self.bullet_handler.update(self.player, self.enemy_handler.enemies)
            self.power_up_handler.update(self.player)
            self.score = self.enemy_handler.number_enemy_destroyed
            if not self.player.is_alive:
                pygame.time.delay(300)
                self.playing = False
                self.number_death += 1

    # este metodo "dibuja o renderiza o refresca mis cambios en la pantalla del juego"
  
    def draw(self):
        self.draw_background()
        if self.playing:
            self.clock.tick(FPS)       
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.power_up_handler.draw(self.screen)
            self.draw_score()
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        # le indicamos a pygame que transforme el objeto BG (que es una imagen en memoria, no es un archivo)
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        # blit DIBUJA la imagen en memoria en una posicion (x, y)
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:                                           
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))   
        # blit DIBUJA la imagen en memoria en una posicion (x, y)

            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
    
    def draw_menu(self):
        if self.number_death == 0:
            text, text_rect = text_utils.get_message('Press any Key to Start', 30, WHITE_COLOR)
            self.screen.blit(text, text_rect)
        else:
            text, text_rect = text_utils.get_message('Press any Key to Restart', 30, WHITE_COLOR)
            score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 30, WHITE_COLOR, height=SCREEN_HEIGHT//2 +50)
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
    #  Muestra el mensaje "Your score is: {self.score}" con un tamaño de fuente de 20 y lo ubica en una posición específica (1000, 40) en la pantalla
    def draw_score(self):
        score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 20, WHITE_COLOR, 1000, 40)
        self.screen.blit(score, score_rect)

    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()  # de aca los llama
        self.bullet_handler.reset() # de aca los llama
        self.score = 0
