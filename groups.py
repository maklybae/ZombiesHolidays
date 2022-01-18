import pygame

hero_group = pygame.sprite.Group()
bullets_group = pygame.sprite.Group()
zombies_group = pygame.sprite.Group()
menu_buttons_group = [pygame.sprite.Group(), pygame.sprite.Group()]
cursor_group = pygame.sprite.Group()


def remove_all_sprites():
    bullets_group.empty()
    zombies_group.empty()
