#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import config
import game


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
        self.entities = pygame.sprite.Group()
        self.timer = pygame.time.Clock()

    def draw(self):
        self.screen.blit(self.bg, (0,0))
        self.entities.draw(self.screen)

        pygame.display.update()     # обновление и вывод всех изменений на экран
        self.timer.tick(60)
