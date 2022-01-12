import pygame
from tools import *
from constants import *
from constants import *


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)


class Cursor(pygame.sprite.Sprite):
    image = load_image('cursor.png', -1)

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Cursor.image
        self.rect = self.image.get_rect()

    def update(self, coords) -> None:
        self.rect.x, self.rect.y = coords


def show_menu(screen: pygame.Surface):
    # fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    fon = pygame.Surface((WIDTH, HEIGHT))
    fon.fill(pygame.Color('blue'))
    pygame.mouse.set_visible(False)
    screen.blit(fon, (0, 0))
    cursor_group = pygame.sprite.Group(Cursor())
    cursor_coords = (0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_focused():
                    cursor_coords = event.pos
        screen.blit(fon, (0, 0))
        cursor_group.update(cursor_coords)
        cursor_group.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    show_menu(screen)
