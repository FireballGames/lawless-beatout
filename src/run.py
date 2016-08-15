#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game
import d2gui

# import config
import game

import pygame

from player import Player
from level import Level

def main():
    g = d2game.Game()
    gui = d2gui.GUI()

    g.hero = Player(*game.PLAYER_START)

    gui.entities.add(g.hero)
    g.l = Level(gui.entities)

    g.run()

    while g.is_running():
        for e in pygame.event.get(): # Обрабатываем события
            if e.type == pygame.QUIT:
                g.quit()
            if e.type == pygame.KEYDOWN:
                gui.key_down(e.key, g.hero)
            if e.type == pygame.KEYUP:
                gui.key_up(e.key, g.hero)

        g.hero.update(g.l.platforms)
        gui.draw()

if __name__ == "__main__":
    main()
