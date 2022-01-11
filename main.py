import pygame
from constants import *
from tools import *

pygame.init()
screen = pygame.display.set_mode(SIZE)


pygame.display.set_caption('ZombiesHolidays')
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

    all_sprites.update()

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)
