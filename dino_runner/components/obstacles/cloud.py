from pygame.sprite import Sprite
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH
import random


class Cloud(Sprite):

    def __init__(self):
        self.image = CLOUD
        self.cloud_rect = self.image.get_rect()
        self.cloud_rect.x = SCREEN_WIDTH   


    def draw(self, screen):
        screen.blit(self.image, self.cloud_rect)

    def update(self, game_speed):
        self.cloud_rect.x  -= game_speed
        if self.cloud_rect.x < 0:
            self.cloud_rect.x = SCREEN_WIDTH
            self.cloud_rect.y = random.randint(0, 100)
