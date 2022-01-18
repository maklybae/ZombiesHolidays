import pygame

all_sprites = pygame.sprite.Group()
hero_group = pygame.sprite.Group()
bullets_group = pygame.sprite.Group()
zombies_group = pygame.sprite.Group()
menu_buttons_group = [pygame.sprite.Group(), pygame.sprite.Group()]
cursor_group = pygame.sprite.Group()


def remove_all_sprites():
    all_sprites.remove()
    bullets_group.remove()
    zombies_group.remove()
