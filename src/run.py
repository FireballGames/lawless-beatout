#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame import *

WIN_WIDTH = 800 #Ширина создаваемого окна
WIN_HEIGHT = 640 # Высота
BACKGROUND_COLOR = "#004400"
RUNNING = True


def main():
    DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
    pygame.init() # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
    pygame.display.set_caption("Beat'em Up")
    bg = Surface((WIN_WIDTH,WIN_HEIGHT)) # Создание видимой поверхности
                                         # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))     # Заливаем поверхность сплошным цветом

    while RUNNING: # Основной цикл программы
        for e in pygame.event.get(): # Обрабатываем события
            if e.type == QUIT:
                raise (SystemExit, "QUIT")
        screen.blit(bg, (0,0))      # Каждую итерацию необходимо всё перерисовывать
        pygame.display.update()     # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()
