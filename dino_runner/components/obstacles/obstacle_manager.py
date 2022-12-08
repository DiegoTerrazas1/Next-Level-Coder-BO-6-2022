import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.large_cactus import LargeCactus
from dino_runner.components.obstacles.bird import Bird

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

import random


class ObstacleManager():

    def __init__(self):
        self.obstacles = []#para tener varios obstacles ,utilizaremos una lista[]


    def update(self, game_speed, game):#si no tenemos ningun obstaculo en mi lista agregamos el cactus
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))#añadiendo una nueva instancia#de Cactus que agregue a mis lista de obstacles,que es smmal cactus
            elif random.randint(0, 2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(400)
                game.playing = False
                break

        

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
