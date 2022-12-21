import pygame

hero_group = pygame.sprite.Group()
bullets_group = pygame.sprite.Group()
zombies_group = pygame.sprite.Group()
menu_buttons_group = [pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()]
cursor_group = pygame.sprite.Group()


def remove_all_sprites():  # удаление игровых объектов с экрана
    bullets_group.empty()
    zombies_group.empty()


def remove_all_buttons():  # удаление объектов меню с экрана
    menu_buttons_group[0].empty()
    menu_buttons_group[1].empty()
