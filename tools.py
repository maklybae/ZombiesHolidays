import os
import pygame
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def load_level(lvl_num):
    with open(f'data/levels/lvl{lvl_num}.txt') as lvl:
        spawn_time = list(map(int, lvl.readline().rstrip().split(';')))
        spawn_zombie = lvl.readline().rstrip().split(';')
        spawn_coords = list(map(int, lvl.readline().rstrip().split(';')))
    return spawn_time, spawn_zombie, spawn_coords


def load_lastlvl():
    with open(f'data/lastlvl') as lvl:
        return int(lvl.readline().rstrip())


def save_lastlvl(lvl):
    with open('data/lastlvl', 'w') as f:
        f.write(str(lvl))


def counter_pp():
    with open('data/counter') as f:
        k = int(f.readline().rstrip()) + 1
    with open('data/counter', 'w') as f:
        f.write(str(k))


def get_counter():
    with open('data/counter') as f:
        return int(f.readline().rstrip())


def reset_stat():
    with open('data/counter', 'w') as f:
        f.write('0')
    with open('data/lastlvl', 'w') as f:
        f.write('1')
