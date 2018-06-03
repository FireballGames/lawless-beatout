#!/usr/bin/env python
# -*- coding: utf-8 -*-

import resource
import config

import pygame

import game.entity


ENEMY_COLOR = "#FF6262"
ENEMY_IMAGE = resource.HERO
MOVE_SPEED = config.BLOCK

class Enemy(game.entity.Entity):
    def move(self, level):
        import random

        x = y = 0
        if random.random() > 0.5:
            x = random.randint(-MOVE_SPEED, MOVE_SPEED)
            y = random.randint(-MOVE_SPEED, MOVE_SPEED)
            if x > 0:
                self.states["right"].value = True
            if x < 0:
                self.states["left"].value = True
            if y > 0:
                self.states["down"].value = True
            if y < 0:
                self.states["up"].value = True
                
            # self.rect.x += x
            # self.rect.y += y

        self.update(level)
        
        self.states["right"].value = False
        self.states["left"].value = False
        self.states["down"].value = False
        self.states["up"].value = False       