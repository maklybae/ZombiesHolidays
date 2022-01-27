import pygame
from constants import *


pygame.init()
screen = pygame.display.set_mode(SIZE)


from groups import *
import hero
import zombies
from tools import *
from menu import show_menu
from win import win


pygame.display.set_caption('ZombiesHolidays')


if (lvl := show_menu(screen)) is None:
    lvl = load_lastlvl()
spawn_time, spawn_zombie, spawn_coords = load_level(lvl)

clock = pygame.time.Clock()
hero = hero.Hero()
key_left = False
key_right = False
ticks = 0
background = pygame.transform.scale(load_image('background.png'), SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_lastlvl(lvl)
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                key_left = True
            if event.key == pygame.K_RIGHT:
                key_right = True
            if event.key == pygame.K_SPACE:
                hero.shoot()
            if event.key == pygame.K_r:
                hero.reload()
            if event.key == pygame.K_ESCAPE:
                save_lastlvl(lvl)
                key_left, key_right = False, False
                tmp = show_menu(screen)
                if tmp is None:
                    continue
                else:
                    lvl = tmp
                    spawn_time, spawn_zombie, spawn_coords = load_level(lvl)
                    remove_all_sprites()
                    hero.first_position()
                    hero.reset_bullets()
                    ticks = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                key_left = False
            if event.key == pygame.K_RIGHT:
                key_right = False

    for zombie in zombies_group.sprites():
        if zombie.check_gameover():
            save_lastlvl(lvl)
            key_left, key_right = False, False
            tmp = show_menu(screen)
            if tmp is not None:
                lvl = tmp
            spawn_time, spawn_zombie, spawn_coords = load_level(lvl)
            remove_all_sprites()
            hero.first_position()
            hero.reset_bullets()
            ticks = 0

    ticks += DELTA_TICKS
    if spawn_time and ticks >= spawn_time[0]:
        eval(f'zombies.{spawn_zombie.pop(0)}({spawn_coords.pop(0)})')
        spawn_time.pop(0)
    if not spawn_time and not zombies_group.sprites():
        win(screen)
        save_lastlvl(lvl)
        key_left, key_right = False, False
        tmp = show_menu(screen)
        if tmp is not None:
            lvl = tmp
        spawn_time, spawn_zombie, spawn_coords = load_level(lvl)
        remove_all_sprites()
        hero.first_position()
        hero.reset_bullets()
        ticks = 0
    if key_left:
        hero.left()
    if key_right:
        hero.right()

    hero_group.update()
    bullets_group.update()
    hero_group.update()
    zombies_group.update()

    screen.blit(background, (0, 0))
    bullets_group.draw(screen)
    hero_group.draw(screen)
    zombies_group.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)
