import pygame
from constants import *


# настройка окна
pygame.init()
screen = pygame.display.set_mode(SIZE)


from groups import *
import hero
import zombies
from tools import *
from menu import show_menu
from win import win
from gameover import gameover

# установка начальных значений
pygame.display.set_caption('ZombiesHolidays')
pygame.display.set_icon(load_image('icon.png'))

lvl = -1
spawn_time, spawn_zombie, spawn_coords = [], [], []

clock = pygame.time.Clock()
hero = hero.Hero()
key_left = False
key_right = False
ticks = 0
background = pygame.transform.scale(load_image('background.png'), SIZE)


def select_lvl_in_menu(special_flag=None):  # функция запуска меню
    global lvl, spawn_zombie, spawn_coords, spawn_time, key_left, key_right, ticks
    if special_flag is not None:
        if special_flag == 'first_boot':  # запуск меню при открытии приложения
            tmp = show_menu(screen, load_lastlvl())
            if tmp is None:
                lvl = load_lastlvl()
            else:
                lvl = tmp
        if special_flag == 'lose' or special_flag == 'win' or special_flag == 'escape':
            key_left, key_right = False, False
            if special_flag == 'lose':  # проигрыш уровня
                gameover(screen)
            elif special_flag == 'win':  # выигрыш уровня
                win(screen)  # анимация выигрыша
                if lvl == 6:
                    set_end()
                save_lastlvl(min(max(load_lastlvl(), lvl + 1), 6))  # обновление номера уровня
            tmp = show_menu(screen, load_lastlvl())  # запуск меню
            if tmp is not None:
                lvl = tmp
            else:
                if special_flag == 'escape':  # продолжение игры, если другой уровень не выбран
                    return
                lvl = load_lastlvl()
            remove_all_sprites()
            hero.first_position()
            hero.reset_bullets()
            ticks = 0
        counter_pp()  # обновление количества попыток
        spawn_time, spawn_zombie, spawn_coords = load_level(lvl)  # загрузка уровня


select_lvl_in_menu('first_boot')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # выход из приложения
            save_lastlvl(lvl)
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # движение влево
                key_left = True
            if event.key == pygame.K_RIGHT:  # движение вправо
                key_right = True
            if event.key == pygame.K_SPACE:  # стрельба
                hero.shoot()
            if event.key == pygame.K_r:  # перезарядка
                hero.reload()
            if event.key == pygame.K_ESCAPE:  # выход в меню
                select_lvl_in_menu('escape')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:  # движение влево
                key_left = False
            if event.key == pygame.K_RIGHT:  # движение вправо
                key_right = False

    for zombie in zombies_group.sprites():  # проверка на проигрыш
        if zombie.check_gameover():
            select_lvl_in_menu('lose')

    ticks += DELTA_TICKS  # инкремент тиков
    if spawn_time and ticks >= spawn_time[0]:  # создание зомби
        eval(f'zombies.{spawn_zombie.pop(0)}({spawn_coords.pop(0)})')
        spawn_time.pop(0)
    if not spawn_time and not zombies_group.sprites():  # проверка на выигрыш
        select_lvl_in_menu('win')
    if key_left:  # движение влево
        hero.left()
    if key_right:  # движение вправо
        hero.right()

    # обновление картинки
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
