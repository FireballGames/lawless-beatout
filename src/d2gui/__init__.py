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


def background(display):
    bg = pygame.Surface(display) # Создание видимой поверхности
                          # будем использовать как фон
    bg.fill(pygame.Color(config.BACKGROUND_COLOR)) # Заливаем поверхность сплошным цветом
    return bg


class GUI():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(config.DISPLAY)
        pygame.display.set_caption(game.TITLE)
        self.bg = background(config.DISPLAY)
        self.entities = None # pygame.sprite.Group()
        self.timer = pygame.time.Clock()
        self.game = None
        self.player = None

    def set_game(self, g):
        self.game = g
        self.player = self.game.hero

        # self.entities.add(self.player)

    def draw(self):
        self.bg = pygame.image.load(self.game.level.background)

        self.screen.blit(self.bg, (0,0))
        self.game.level.entities.draw(self.screen)

        pygame.display.update()     # обновление и вывод всех изменений на экран
        self.timer.tick(30)

    def process_events(self):
        for e in pygame.event.get(): # Обрабатываем события
            if e.type == pygame.QUIT:
                self.game.quit()
            if e.type == pygame.KEYDOWN:
                self.key_event(e.key, True)
            if e.type == pygame.KEYUP:
                self.key_event(e.key, False)

    def key_event(self, key, down):
        direction = DIR_KEYS.get(key)
        if direction:
            self.player.go(direction, down)
