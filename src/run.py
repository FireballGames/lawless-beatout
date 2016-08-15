#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game
import d2gui
import config
# import game

import pygame
from pygame import *

from player import Player
from level import Level

def main():
    g = d2game.Game()
    gui = d2gui.GUI()

    hero = Player(55, 55)
    left = right = False
    up = False

    gui.entities.add(hero)
    l = Level(gui.entities)

    g.run()

    while g.is_running():
        for e in pygame.event.get(): # Обрабатываем события
            if e.type == QUIT:
                g.quit()
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

        hero.update(left, right, up, l.platforms)
        gui.draw()

if __name__ == "__main__":
    main()
