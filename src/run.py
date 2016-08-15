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

    gui.entities.add(hero)
    l = Level(gui.entities)

    g.run()

    while g.is_running():
        for e in pygame.event.get(): # Обрабатываем события
            if e.type == QUIT:
                g.quit()
            if e.type == KEYDOWN and e.key == K_LEFT:
                hero.left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                hero.right = True
            if e.type == KEYDOWN and e.key == K_UP:
                hero.up = True
            if e.type == KEYUP and e.key == K_LEFT:
                hero.left = False
            if e.type == KEYUP and e.key == K_RIGHT:
                hero.right = False
            if e.type == KEYUP and e.key == K_UP:
                hero.up = False

        hero.update(l.platforms)
        gui.draw()

if __name__ == "__main__":
    main()
