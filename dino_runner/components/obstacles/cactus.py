from dino_runner.components.obstacles.obstacle import Obtacle
import random

class Cactus(Obtacle):
    def __init__(self, image):#recordemos que type es el indice de obstaculos que se vana a mostrar
        self.type = random.randint(0, 2)#y qqueremos que uno de esos obstaculos (imagenes),sea a la suerte
        super().__init__(image, self.type)#cuando muestren en el juego
        self.rect.y = 325

    