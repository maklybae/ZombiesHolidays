import pygame
import random
from tools import *
from constants import *
from copy import copy


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)


class Particle(pygame.sprite.Sprite):
    fire = [load_image("star.png")]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy, screen, group):
        super().__init__(group)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = GRAVITY

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(self.screen.get_rect()):
            self.kill()


def create_particles(position, screen, group):
    particle_count = 100
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers), screen, group)


def win(screen: pygame.Surface) -> None:
    clock = pygame.time.Clock()
    particles = pygame.sprite.Group()
    ticks = 0
    screen_background = copy(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return
        if ticks >= 100:
            create_particles((random.randint(WIDTH // 2 - 200, WIDTH // 2), random.randint(HEIGHT // 2 - 200, HEIGHT // 2)), screen, particles)
            ticks = 0
        ticks += 1
        screen.blit(screen_background, (0, 0))
        particles.update()
        particles.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    win(screen)