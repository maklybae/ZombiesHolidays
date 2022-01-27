import pygame
from copy import copy
from tools import *
from constants import *


class GameOverScreen(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('gameover.png'), SIZE)

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = GameOverScreen.image
        self.rect = self.image.get_rect()
        self.rect.topright = 0, 0

    def update(self) -> None:
        if self.rect.right <= WIDTH:
            self.rect = self.rect.move(1, 0)


def gameover(screen: pygame.Surface):
    clock = pygame.time.Clock()
    screen_background = copy(screen)
    gameover_group = pygame.sprite.Group(GameOverScreen())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return

        gameover_group.update()

        screen.blit(screen_background, (0, 0))
        gameover_group.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)