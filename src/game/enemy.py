#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

ENEMY_SIZE = (73, 100)
ENEMY_COLOR = "#FF6262"
ENEMY_IMAGE = "res/player/man.png"

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.width = ENEMY_SIZE[0]
        self.height = ENEMY_SIZE[1]

        # self.image = Surface((self.width, self.height))
        # self.image.fill(Color(PLATFORM_COLOR))
        self.image = pygame.image.load(ENEMY_IMAGE)
        self.rect = pygame.Rect(x, y, self.width, self.height)
