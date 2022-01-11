import pygame
from hero_constants import *
from constants import *
from groups import *

class Hero(pygame.sprite.Sprite):
    image = pygame.Surface((20, 20))

    def __init__(self, *groups):
        super().__init__(hero_group, all_sprites, *groups)
        self.image = Hero.image
        self.image.fill(pygame.Color('green'))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = WIDTH // 2, HEIGHT - self.rect.height

    def left(self):
        self.rect.move(-3)

    def right(self):
        self.rect.move(3)


class Bullet(pygame.sprite.Sprite):
    image = pygame.Surface((5, 5))
    image.fill(pygame.Color('green'))

    def __init__(self, coords, *groups):
        super().__init__(all_sprites, bullets_group, *groups)
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
