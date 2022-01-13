import pygame
from tools import *
from constants import *
from groups import menu_buttons_group, cursor_group

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)


class Cursor(pygame.sprite.Sprite):
    image = load_image('cursor3.png')

    def __init__(self, *groups):
        super().__init__(cursor_group, *groups)
        self.image = Cursor.image
        self.rect = self.image.get_rect()

    def update(self, coords) -> None:
        self.rect.x, self.rect.y = coords


class Button(pygame.sprite.Sprite):
    def __init__(self, title: str, pos: tuple, size: tuple, slide:int, *groups):
        super().__init__(menu_buttons_group[slide], *groups)
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        font = pygame.font.Font(None, size[1] // 2)
        text = font.render(title, True, (100, 255, 100))
        text_x = size[0] // 2 - text.get_width() // 2
        text_y = size[1] // 2 - text.get_height() // 2
        self.image.blit(text, (text_x, text_y))

    def update(self, pos, *args, **kwargs) -> None:
        x, y = pos
        if self.rect.left <= x <= self.rect.right and self.rect.top <= y <= self.rect.bottom:
            pass  # action


def show_menu(screen: pygame.Surface):
    slides = [pygame.Surface((WIDTH, HEIGHT)), pygame.Surface((WIDTH, HEIGHT))]
    slides[0].fill(pygame.Color('blue'))
    slides[1].fill(pygame.Color('yellow'))
    cur_slide = 0
    pygame.mouse.set_visible(False)
    Cursor()
    Button('Test', (20, 20), (300, 50), 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_focused():
                    cursor_group.update(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                menu_buttons_group[cur_slide].update(event.pos)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
        screen.blit(slides[cur_slide], (0, 0))
        menu_buttons_group[cur_slide].draw(screen)
        cursor_group.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    show_menu(screen)
