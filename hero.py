import pygame
from main import all_sprites
from hero_constants import *


class Hero(pygame.sprite.Sprite):
    image = pygame.Surface((20, 20))
    image.fill(pygame.Color('red'))

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Hero.image
        self.rect = self.image.get_rect()


class Bullet(pygame.sprite.Sprite):
    image = pygame.Surface((5, 5))
    image.fill(pygame.Color('green'))

    def __init__(self, *groups, coords):
        super().__init__(*groups)
        self.image = Bullet.image
        self.rect = self.image.get_rect()
        self.x, self.y = coords
        self.ticks = 0

    def update(self, *args, **kwargs) -> None:
        if self.ticks >= BULLET_SPEED:
            self.ticks = 0
            self.rect.move(0, -1)
        else:
            self.ticks += 1
