#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game.level

import config
import game
import game.enemy

import pygame
import random


ARENA_POS = (100, 400)
ARENA_SIZE = (600, 100)
ENEMY_COUNT = 5
# GRAVITY = 0.35


class Level(d2game.level.Level):
    def __init__(self, player):
        d2game.level.Level.__init__(self, player)
        self.background = "{}/{}".format(config.RES_DIR, game.BACKGROUND_IMAGE)
        self.active_rect = pygame.Rect(ARENA_POS, ARENA_SIZE)

    def generate_enemies(self):
        enemies = []
        for i in range(ENEMY_COUNT):
            x = random.randint(0, ARENA_SIZE[0]) + ARENA_POS[0]
            y = random.randint(0, ARENA_SIZE[1]) + ARENA_POS[1] - game.enemy.ENEMY_SIZE[1]
            enemy = game.enemy.Enemy(x, y)
            enemies.append(enemy)

        return enemies
