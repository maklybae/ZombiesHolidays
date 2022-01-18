import pygame
from zombies_constants import *
from random import randint
from constants import WIDTH
from groups import *
from constants import *
from tools import load_image


class Zombie(pygame.sprite.Sprite):  # класс стандартного зомби
    image = pygame.transform.scale(load_image('zombie.png'), (40, 45))

    def __init__(self, coord_x):
        super().__init__(zombies_group)
        self.image = Zombie.image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = coord_x
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

    def __init__(self, coord_x):
        super().__init__(coord_x)
        self.image = ZombieFather.image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = coord_x
        self.rect.y = 0
        self.hp = 100
