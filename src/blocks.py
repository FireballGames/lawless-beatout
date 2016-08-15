#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *

PLATFORM_HEIGHT = 32
PLATFORM_WIDTH = 32
PLATFORM_COLOR = "#FF6262"

class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)

        self.width = PLATFORM_WIDTH
        self.height = PLATFORM_HEIGHT

        self.image = Surface((self.width, self.height))
        self.image.fill(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, self.width, self.height)
