import pygame
from constants import *
import zombies
from random import randint
from groups import *

pygame.init()
screen = pygame.display.set_mode(SIZE)


pygame.display.set_caption('ZombiesHolidays')
running = True
zombie1 = zombies.Zombie()
zombie2 = zombies.ZombieFather()
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)
