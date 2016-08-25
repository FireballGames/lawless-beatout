#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import config
import game


DIR_KEYS = {
    pygame.K_LEFT: "left",
    pygame.K_RIGHT: "right",
    pygame.K_UP: "up",
    pygame.K_DOWN: "down",
}


def load_image(name):
    try:
        image = pygame.image.load(name)
    except pygame.error as e:
        print("Can't load image: {}".format(name))
        raise SystemExit(e)
    image = image.convert_alpha()
    return image, image.get_rect()


def background(background):
    screen = pygame.display.get_surface()
    bg = pygame.Surface(screen.get_size())  # (display) # Создание видимой поверхности
    bg = bg.convert()
    # bg.fill(pygame.Color(config.BACKGROUND_COLOR)) # Заливаем поверхность сплошным цветом
    bg.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    back, back_rect = load_image(background)
    screen.blit(back, (0, 0))
    pygame.display.flip()
    return back


class GUI():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(config.DISPLAY)
        pygame.display.set_caption(game.TITLE)

        # self.bg = background(config.DISPLAY)
        # self.entities = pygame.sprite.Group()
        self.entities = None
        self.timer = pygame.time.Clock()
        self.game = None
        self.player = None

    def set_game(self, g):
        self.game = g
        self.player = self.game.hero
        # self.entities.add(self.player)

    def draw(self):
        # self.bg = pygame.image.load(self.game.level.background)

        # self.window.blit(self.bg, (0,0))
        self.bg = background(self.game.level.background)  # config.DISPLAY)
        self.game.level.entities.draw(self.window)

        pygame.display.update()     # обновление и вывод всех изменений на экран
        self.timer.tick(30)

    def process_events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.game.quit()
            if e.type == pygame.KEYDOWN:
                self.key_event(e.key, True)
            if e.type == pygame.KEYUP:
                self.key_event(e.key, False)

    def key_event(self, key, down):
        if key == pygame.K_ESCAPE:
            self.game.quit()
        direction = DIR_KEYS.get(key)
        if direction:
            self.player.go(direction, down)
