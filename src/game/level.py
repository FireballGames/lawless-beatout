#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game.level

import config
import game
import game.enemy

import random


ARENA_POS = (0, 400)
ARENA_SIZE = (800, 200)
ENEMY_COUNT = 5


class Level(d2game.level.Level):
    def __init__(self, player):
        d2game.level.Level.__init__(self, player)
        self.background = "{}/{}".format(config.RES_DIR, game.BACKGROUND_IMAGE)

    def generate_enemies(self):
        enemies = []
        for i in range(ENEMY_COUNT):
            x = random.randint(0, ARENA_SIZE[0]) + ARENA_POS[0]
            y = random.randint(0, ARENA_SIZE[1]) + ARENA_POS[1] - game.enemy.ENEMY_SIZE[1]
            enemy = game.enemy.Enemy(x, y)
            enemies.append(enemy)

        return enemies
