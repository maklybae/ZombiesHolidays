import pygame
from tools import *
from constants import *
from groups import menu_buttons_group, cursor_group, remove_all_buttons

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)

cur_slide = 0
change_level_to = -1


def change_slide(slide):
    global cur_slide
    cur_slide = slide


def change_level(lvl):
    global change_level_to
    change_level_to = lvl


def change_to_lastlvl():
    global change_level_to
    change_level_to = None


def reset():
    reset_stat()
    terminate()


class Cursor(pygame.sprite.Sprite):
    image = load_image('cursor3.png')

    def __init__(self, *groups):
        super().__init__(cursor_group, *groups)
        self.image = Cursor.image
        self.rect = self.image.get_rect()

    def update(self, coords) -> None:
        self.rect.x, self.rect.y = coords


class Button(pygame.sprite.Sprite):
    def __init__(self, title: str, pos: tuple, size: tuple, slide: int, func, arg=None):
        super().__init__(menu_buttons_group[slide])
        self.func = func
        self.arg = arg
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        if slide == 0:
            pygame.draw.rect(self.image, BUTTONS_BORDER_COLOR, self.rect)
            pygame.draw.rect(self.image, MENU_COLOR, (
                self.rect.x + 2, self.rect.y + 2, self.rect.width - 4, self.rect.height - 4))
        elif 1 <= slide <= 2:
            self.image.fill(MENU_COLOR)
        self.rect.x, self.rect.y = pos
        font = pygame.font.Font(None, size[1] // 2)
        text = font.render(title, True, BUTTONS_BORDER_COLOR)
        text_x = size[0] // 2 - text.get_width() // 2
        text_y = size[1] // 2 - text.get_height() // 2
        self.image.blit(text, (text_x, text_y))

    def update(self, pos, *args, **kwargs) -> None:
        x, y = pos
        if self.rect.left <= x <= self.rect.right and self.rect.top <= y <= self.rect.bottom:
            if self.arg is not None:
                self.func(self.arg)
            else:
                self.func()


def show_menu(screen: pygame.Surface, lastlvl: int):
    global change_level_to
    change_level_to = -1
    slides = [pygame.Surface((WIDTH, HEIGHT)), pygame.Surface((WIDTH, HEIGHT)), pygame.Surface((WIDTH, HEIGHT))]
    slides[0] = pygame.transform.scale(load_image('slide.png'), SIZE)
    slides[1] = pygame.transform.scale(load_image('slide.png'), SIZE)
    slides[2] = pygame.transform.scale(load_image('slide3.png'), SIZE)
    pygame.mouse.set_visible(False)
    Cursor()
    Button('????????????????????', (WIDTH // 2 - SLIDE1_BUTTON_SIZE[0] // 2, 150), SLIDE1_BUTTON_SIZE, 0, change_to_lastlvl)
    Button('?????? ????????????', (WIDTH // 2 - SLIDE1_BUTTON_SIZE[0] // 2, 170 + SLIDE1_BUTTON_SIZE[1]), SLIDE1_BUTTON_SIZE, 0, change_slide, 1)
    Button('???? ????????', (WIDTH // 2 - SLIDE1_BUTTON_SIZE[0] // 2, 190 + 2 * SLIDE1_BUTTON_SIZE[1]), SLIDE1_BUTTON_SIZE, 0, change_slide, 2)
    Button('???????????????? ????????????????????', (WIDTH // 2 - SLIDE1_BUTTON_SIZE[0] // 2, 210 + 3 * SLIDE1_BUTTON_SIZE[1]), SLIDE1_BUTTON_SIZE, 0, reset)
    for i in range(1, lastlvl + 1):
        eval(f"""Button(str({i}), {LVL_BUTTONS_COORDS[i]}, SLIDE2_BUTTON_SIZE, 1, change_level, arg={i})""")
    Button('??????????', (WIDTH - SLIDE1_BUTTON_SIZE[0], HEIGHT - SLIDE1_BUTTON_SIZE[1]), SLIDE1_BUTTON_SIZE, 1, change_slide, 0)
    Button('??????????', (WIDTH - SLIDE1_BUTTON_SIZE[0], HEIGHT - SLIDE1_BUTTON_SIZE[1]), SLIDE1_BUTTON_SIZE, 2, change_slide, 0)

    font = pygame.font.Font(None, 60)
    text = font.render('??????????????: ' + str(get_counter()), True, BUTTONS_BORDER_COLOR)
    text_end = font.render('???????? ????????????????! ??????????????????????!', True, BUTTONS_BORDER_COLOR)
    if_end = get_end()

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
                remove_all_buttons()
                return None
        if change_level_to != -1:
            remove_all_buttons()
            return change_level_to
        screen.blit(slides[cur_slide], (0, 0))
        menu_buttons_group[cur_slide].draw(screen)
        cursor_group.draw(screen)
        screen.blit(text, (0, 0))
        if if_end:
            screen.blit(text_end, (WIDTH - 630, 0))
        pygame.display.flip()


if __name__ == '__main__':
    show_menu(screen)
