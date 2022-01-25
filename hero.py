import pygame
from hero_constants import *
from constants import *
from groups import *
from tools import *


class Hero(pygame.sprite.Sprite):
    image = pygame.Surface(HERO_SIZE)

    def __init__(self, *groups):
        super().__init__(hero_group, *groups)
        self.image = Hero.image
        self.image.fill(pygame.Color('green'))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = WIDTH // 2, HEIGHT - self.rect.height

    def left(self):
        if self.rect.x < 0:
            return
        self.rect = self.rect.move(-MOVING_SPEED, 0)

    def right(self):
        if self.rect.x + self.rect.width > WIDTH:
            return
        self.rect = self.rect.move(MOVING_SPEED, 0)

    def shoot(self):
        Bullet((self.rect.x, self.rect.y - 10))

    def first_position(self):
        self.rect.x, self.rect.y = WIDTH // 2, HEIGHT - self.rect.height


class Bullet(pygame.sprite.Sprite):
    image = load_image('bullet.png')

    def __init__(self, coords, *groups):
        super().__init__(bullets_group, *groups)
        self.image = Bullet.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coords
        self.ticks = 0

    def update(self, *args, **kwargs) -> None:
        for zombie in zombies_group.sprites():
            if pygame.sprite.collide_mask(self, zombie):
                self.kill()
                zombie.take_damage(BULLET_DAMAGE)
                return
        if self.ticks >= BULLET_SPEED:
            self.ticks = 0
            self.rect = self.rect.move(0, -1)
        else:
            self.ticks += 1
