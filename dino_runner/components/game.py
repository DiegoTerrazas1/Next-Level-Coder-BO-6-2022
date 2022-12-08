import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur

from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.obstacles.cloud import Cloud

colors ={
    "RED": (255, 0, 0),
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "BLUE": (0, 0, 255),
    "GREEN": (0, 255, 0),
}
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 18
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_maganer = ObstacleManager()
        self.cloud = Cloud()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()#Nos devolvera la tecla que se va,a presionar dentro del juego
        self.player.update(user_input)#para que se actulize con el teclado
        self.obstacle_maganer.update(self.game_speed, self)
        self.cloud.update(self.game_speed)


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill(colors["WHITE"])#se maneja por "RGB" ,los colores ejemplo:R= rojo, G = verde, B = azul
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_maganer.draw(self.screen) #para cambiar el color ,bajar los valores ...
        self.cloud.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
