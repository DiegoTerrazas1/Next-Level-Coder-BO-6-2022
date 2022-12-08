from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH



class Obtacle(Sprite):
    def __init__(self, image, type):
        self.image = image 
        self.type = type  #el indice de la lista    ###el self.image ya nos devolvera una imagen por el indice type
        self.rect = self.image[self.type].get_rect()# self.rect,ya viene con sus medidas en el sprite,
        self.rect.x = SCREEN_WIDTH                   ###despues que obtengamos la imagen obtendremos las medidas
        #apareceran al final de la pantalla derecha por la coordenada x

    def draw (self, screen):
        screen.blit(self.image[self.type], self.rect)
        
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed #Vamos a restar con el width para que vaya degrandando el valor hacia la izquierda
        if self.rect.x < 0:       #
            obstacles.pop()#nos va a eliminar el ultimo elemento de la lista