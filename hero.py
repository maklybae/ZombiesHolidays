import pygame


class Hero(pygame.sprite.Sprite):
    image = pygame.Surface((20, 20))
    image.fill(pygame.Color('red'))

    def __init__(self):
        super().__init__()
        self.image = Hero.image
        self.rect = self.image.get_rect()
