import pygame
from zombies_constants import *
from random import randint
from constants import WIDTH
from groups import *
from constants import *
from tools import load_image


class Zombie(pygame.sprite.Sprite):  # класс стандартного зомби
    image = load_image("Zombie.png")

    def __init__(self, coord_x):
        super().__init__(zombies_group)
        self.image = Zombie.image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = coord_x, 0
        self.ticks = 0
        self.dx = 0
        self.dy = 1
        self.hp = ZOMBIE_HP
        self.speed = ZOMBIE_SPEED

    def update(self, *args, **kwargs) -> None:
        if self.hp <= 0:
            self.kill()
            return
        if self.ticks >= self.speed:
            self.ticks = 0
            self.rect = self.rect.move(self.dx, self.dy)
        else:
            self.ticks += 1

    def take_damage(self, damage):
        self.hp -= damage

    def check_gameover(self):
        if self.rect.top >= HEIGHT - 147:
            return True


class ZombieFather(Zombie):
    image = load_image('zombiefather2.png')

    def __init__(self, coord_x):
        super().__init__(coord_x)
        self.image = ZombieFather.image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = coord_x, 0
        self.hp = ZOMBIE_FATHER_HP
        self.speed = ZOMBIE_FATHER_SPEED


class ZombieVarvara(Zombie):
    image = load_image('zombievarvara.png')

    def __init__(self, coord_x):
        super().__init__(coord_x)
        self.image = ZombieVarvara.image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = coord_x, 0
        self.hp = ZOMBIE_VARVARA_HP
        self.speed = ZOMBIE_VARVARA_SPEED