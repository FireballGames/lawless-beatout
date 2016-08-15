#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import game

import pygame
from pygame import *

from player import Player
from level import Level

RUNNING = True


def background(display):
    bg = Surface(display) # Создание видимой поверхности
                          # будем использовать как фон
    bg.fill(Color(config.BACKGROUND_COLOR)) # Заливаем поверхность сплошным цветом
    return bg

def main():
    pygame.init() # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(config.DISPLAY) # Создаем окошко
    pygame.display.set_caption(game.TITLE)

    bg = background(config.DISPLAY)

    hero = Player(55, 55)
    left = right = False
    up = False

    entities = pygame.sprite.Group()
    entities.add(hero)
    l = Level(entities)

    timer = pygame.time.Clock()

    while RUNNING: # Основной цикл программы
        for e in pygame.event.get(): # Обрабатываем события
            if e.type == QUIT:
                raise (SystemExit, "QUIT")
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_UP:
                up = False

        screen.blit(bg, (0,0))

        hero.update(left, right, up, l.platforms)
        entities.draw(screen)

        pygame.display.update()     # обновление и вывод всех изменений на экран
        timer.tick(60)

if __name__ == "__main__":
    main()
