import pygame
from zombies_constants import *
from random import randint
from constants import WIDTH
from groups import *
from constants import *


class Zombie(pygame.sprite.Sprite):  # класс стандартного зомби
    image = pygame.Surface((20, 20))  # zombie image

    def __init__(self, *groups):
        super().__init__(all_sprites, zombies_group, *groups)
        self.image = Zombie.image
        self.image.fill(pygame.Color("red"))  # temp
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, WIDTH - self.rect.width)
        self.rect.y = 0
        self.ticks = 0
        self.dx = 0
        self.dy = 1
        self.hp = 10

    def update(self, *args, **kwargs) -> None:
        if self.hp <= 0:
            self.kill()
            return
        if self.rect.bottom >= HEIGHT:
            # game over !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            self.kill()
            return
        if self.ticks >= ZOMBIE_SPEED:
            self.ticks = 0
            self.rect = self.rect.move(self.dx, self.dy)
        else:
            self.ticks += 1

    def take_damage(self, damage):
        self.hp -= damage


class ZombieFather(Zombie):
    image = pygame.Surface((50, 50))  # zombie image
    image.fill(pygame.Color("red"))

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = ZombieFather.image
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, WIDTH - self.rect.width)
        self.rect.y = 0
        self.hp = 100