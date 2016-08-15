#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config

import pygame
from pygame import *

from player import Player
from blocks import Platform, PLATFORM_WIDTH, PLATFORM_HEIGHT

RUNNING = True
LEVEL = [
    "-------------------------",
    "-                       -",
    "-                       -",
    "-                       -",
    "-            --         -",
    "-                       -",
    "--                      -",
    "-                       -",
    "-                   --- -",
    "-                       -",
    "-                       -",
    "-      ---              -",
    "-                       -",
    "--   -----------        -",
    "-                       -",
    "-                -      -",
    "-                   --  -",
    "-                       -",
    "-                       -",
    "-------------------------"]



def main():
    DISPLAY = (config.WIN_WIDTH, config.WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
    pygame.init() # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
    pygame.display.set_caption("Beat'em Up")
    bg = Surface(DISPLAY) # Создание видимой поверхности
                          # будем использовать как фон
    bg.fill(Color(config.BACKGROUND_COLOR))     # Заливаем поверхность сплошным цветом

    hero = Player(55, 55)
    left = right = False
    up = False

    entities = pygame.sprite.Group()
    platforms = []
    entities.add(hero)

    x=y=0
    for row in LEVEL:
        for col in row:
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0

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

        hero.update(left, right, up, platforms)
        entities.draw(screen)

        pygame.display.update()     # обновление и вывод всех изменений на экран
        timer.tick(60)

if __name__ == "__main__":
    main()
