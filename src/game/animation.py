#!/usr/bin/env python
# -*- coding: utf-8 -*-

import resource
import pyganim


DELAY = 100
# RIGHT = [(resource.HERO, DELAY)]
# LEFT = [(resource.HERO, DELAY)]
JUMP_RIGHT = [(resource.HERO, DELAY)]
JUMP_LEFT = [(resource.HERO, DELAY)]
JUMP = [(resource.HERO, DELAY)]

moveRect = (0, 0, resource.HERO_SIZE[0], resource.HERO_SIZE[1])
moveImages = pyganim.getImagesFromSpriteSheet(resource.HERO_WALK, rows=1, cols=4, rects=[moveRect,]) #, width=resource.HERO_SIZE[0], height=resource.HERO_SIZE[1])
MOVE = list(zip(moveImages, [DELAY] * len(moveImages)))

stayImages = pyganim.getImagesFromSpriteSheet(resource.HERO_STAY, rows=1, cols=4, rects=[moveRect,])
STAY = list(zip(stayImages, [250] * len(stayImages)))

