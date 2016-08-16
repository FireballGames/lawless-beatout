#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import pygame

ENEMY_SIZE = (73, 100)
ENEMY_COLOR = "#FF6262"
ENEMY_IMAGE = config.RES_DIR + "/player/man.png"
MOVE_SPEED = 7

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.width = ENEMY_SIZE[0]
        self.height = ENEMY_SIZE[1]

        # self.image = Surface((self.width, self.height))
        # self.image.fill(Color(PLATFORM_COLOR))
        self.image = pygame.image.load(ENEMY_IMAGE)
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def move(self, level):
        import random

        x = y = 0
        if random.random() > 0.5:
            x = random.randint(-MOVE_SPEED, MOVE_SPEED)
            y = random.randint(-MOVE_SPEED, MOVE_SPEED)
            self.rect.x += x
            self.rect.y += y

        self.collide(x, y, level)

    def collide(self, xvel, yvel, level):
        if not self.rect.colliderect(level.active_rect):
            if xvel > 0:
                self.rect.left = level.active_rect.right - 1
            if xvel < 0:
                self.rect.right = level.active_rect.left + 1
            if yvel > 0:
                self.rect.top = level.active_rect.bottom - 1
            if yvel < 0:
                self.rect.bottom = level.active_rect.top + 1

        # for p in level.enemies:
            # if pygame.sprite.collide_rect(self, p):
                # if xvel > 0:
                    # self.rect.right = p.rect.left
                # if xvel < 0:
                    # self.rect.left = p.rect.right
                # if yvel > 0:
                    # self.rect.bottom = p.rect.top
                # if yvel < 0:
                    # self.rect.top = p.rect.bottom
