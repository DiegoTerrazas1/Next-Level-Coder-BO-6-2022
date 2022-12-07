import pygame


from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING , DUCKING, JUMPING_HAMMER


class Dinosaur(Sprite):
    POS_X = 80   # obtenemos las medidas  de x /derecha/izquierda
    POS_Y = 310   #obtenems las medidas de y /arriba/abajo
    POS_Y_DUCKING = 340
    JUMP_VEL = 8.5

    def __init__(self):        # accediendo al indice de la lista de constantes RuNNING
        self.image = RUNNING[0]           ##Es un cuadrado que se posciona en el eje de cordenadas x, y
        self.dino_rect = self.image.get_rect()##image.get_rect() obtenemos la imgamen con las medidas que no esta dando dino rect
        self.dino_rect.x = self.POS_X  #cuando hay constantes globales fuera de nuestro metodo
        self.dino_rect.y = self.POS_Y  #se les asigna el self.(dentro de nuestra clase)
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        
    def update(self, user_input):
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        
        if user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        
        elif user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True

        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

        if self.step_index >= 10:
            self.step_index = 0 #usamos este if para que una vez que llegue a 10
        # que vuelva a ser 0 asi para que muestre las dos imagenes

        
        self.step_index += 1

    def draw(self, screen):#Metodo que implementa la imagen con sus dichas medidas.
        screen.blit(self.image, self.dino_rect)#usando el screnn.blit.

    def run(self):
        self.image = RUNNING [0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y
        self.step_index += 1 #Estamos suamando para que la condicon
        # if se cumpla si es < 5 ,se mostrara la primera imagen,si self.step_index
        #es > muestra la otra imagen.

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y_DUCKING
        self.step_index += 1
        print("Agracharse")

    def jump(self):
        self.image = JUMPING_HAMMER
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4 #Salto
            self.jump_vel -= 0.8   #Salto, cuando  llega a negativo, baja
        if self.jump_vel < -self.JUMP_VEL:#cuando llega a jump_vel en negativo, este  se detiene
            self.dino_rect.y = self.POS_Y
            self.dino_jump = False #
            self.jump_vel = self.JUMP_VEL
