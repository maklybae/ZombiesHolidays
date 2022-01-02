import pygame
from zombies_constants import *
from random import randint
from constants import WIDTH


class Zombie(pygame.sprite.Sprite):  # класс стандартного зомби
    image = pygame.Surface((20, 20))  # zombie image

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Zombie.image
        self.image.fill(pygame.Color("red"))  # temp
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, WIDTH - self.rect.width)
        self.rect.y = 0
        self.ticks = 0
        self.dx = 0
        self.dy = 1

    def update(self, *args, **kwargs) -> None:
        if self.ticks >= ZOMBIE_SPEED:
            self.ticks = 0
            self.rect = self.rect.move(self.dx, self.dy)
        else:
            self.ticks += 1
