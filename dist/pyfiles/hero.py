import pygame
from hero_constants import *
from constants import *
from groups import *
from tools import *


class Hero(pygame.sprite.Sprite):
    image = load_image('hero.png')
    font = pygame.font.Font(None, image.get_height() // 4)
    text = font.render('RELOAD', True, (255, 0, 0))
    text_x = image.get_width() // 2 - text.get_width() // 2 + 10
    text_y = 0

    def __init__(self, *groups):
        super().__init__(hero_group, *groups)
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = WIDTH // 2, HEIGHT - self.rect.height
        self.bullets = 0
        self.ticks_reload = 0

    def left(self):
        if self.rect.x < 0:
            return
        self.rect = self.rect.move(-MOVING_SPEED, 0)

    def right(self):
        if self.rect.x + self.rect.width > WIDTH:
            return
        self.rect = self.rect.move(MOVING_SPEED, 0)

    def shoot(self):
        if self.bullets < MAG:
            Bullet((self.rect.x, self.rect.y - 10))
            self.bullets += 1

    def first_position(self):
        self.rect.x, self.rect.y = WIDTH // 2, HEIGHT - self.rect.height

    def update(self):
        self.image.blit(Hero.image, (0, 0), (0, 0, self.rect.width, 13), special_flags=pygame.BLEND_RGBA_SUB)
        if self.bullets >= MAG:
            self.image.blit(Hero.text, (Hero.text_x, Hero.text_y))
            self.ticks_reload += 1
            if self.ticks_reload >= RELOAD_TIME:
                self.reset_bullets()
                self.ticks_reload = 0

    def reset_bullets(self):
        self.bullets = 0

    def reload(self):
        self.bullets = 10


class Bullet(pygame.sprite.Sprite):
    image = load_image('bullet.png')

    def __init__(self, coords, *groups):
        super().__init__(bullets_group, *groups)
        self.image = Bullet.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coords
        self.ticks = 0

    def update(self, *args, **kwargs) -> None:
        for zombie in zombies_group.sprites():
            if pygame.sprite.collide_mask(self, zombie):
                self.kill()
                zombie.take_damage(BULLET_DAMAGE)
                return
        if self.ticks >= BULLET_SPEED:
            self.ticks = 0
            self.rect = self.rect.move(0, -3)
        else:
            self.ticks += 1
