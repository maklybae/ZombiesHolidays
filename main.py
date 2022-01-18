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


if (lvl := show_menu(screen)) is None:
    lvl = 1
spawn_time, spawn_zombie, spawn_coords = load_level(lvl)

clock = pygame.time.Clock()
hero = hero.Hero()
key_left = False
key_right = False
ticks = 0
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
                if (lvl := show_menu(screen)) is None:
                    continue
                else:
                    spawn_time, spawn_zombie, spawn_coords = load_level(lvl)
                    remove_all_sprites()
                    hero.first_position()
                    ticks = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                key_left = False
            if event.key == pygame.K_RIGHT:
                key_right = False
    ticks += DELTA_TICKS
    if spawn_time and ticks >= spawn_time[0]:
        eval(f'zombies.{spawn_zombie.pop(0)}({spawn_coords.pop(0)})')
        spawn_time.pop(0)
    if key_left:
        hero.left()
    if key_right:
        hero.right()

    all_sprites.update()

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)
