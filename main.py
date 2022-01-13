import pygame
from constants import *


pygame.init()
screen = pygame.display.set_mode(SIZE)


from groups import *
import hero
import zombies
from tools import *
from menu import show_menu


pygame.display.set_caption('ZombiesHolidays')

show_menu(screen)

clock = pygame.time.Clock()
hero = hero.Hero()
zomb1 = zombies.Zombie()
zomb2 = zombies.ZombieFather()
key_left = False
key_right = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                key_left = True
            if event.key == pygame.K_RIGHT:
                key_right = True
            if event.key == pygame.K_SPACE:
                hero.shoot()
            if event.key == pygame.K_ESCAPE:
                show_menu(screen)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                key_left = False
            if event.key == pygame.K_RIGHT:
                key_right = False
    if key_left:
        hero.left()
    if key_right:
        hero.right()

    all_sprites.update()

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)
