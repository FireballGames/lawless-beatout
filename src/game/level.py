#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game.level
import config
import game
import game.blocks

import pygame


ENEMY_COUNT = 5


class Level(d2game.level.Level):
    def __init__(self, player):
        self.background = "{}/{}".format(config.RES_DIR, game.BACKGROUND_IMAGE)

        self.entities = pygame.sprite.Group()
        self.entities.add(player)

        self.enemies = []

        for i in range(ENEMY_COUNT):
            enemy = game.blocks.Platform(i*50, i*50)
            self.entities.add(enemy)
            self.enemies.append(enemy)
