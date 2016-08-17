#!/usr/bin/env python
# -*- coding: utf-8 -*-

import resource
import pyganim


DELAY = 100
RIGHT = [(resource.HERO, DELAY)]
LEFT = [(resource.HERO, DELAY)]
JUMP_RIGHT = [(resource.HERO, DELAY)]
JUMP_LEFT = [(resource.HERO, DELAY)]
JUMP = [(resource.HERO, DELAY)]
STAY = [(resource.HERO, DELAY)]

allImages = pyganim.getImagesFromSpriteSheet(resource.HERO, rects=[], width=resource.HERO_SIZE[0], height=resource.HERO_SIZE[1])
MOVE = list(zip(allImages, [DELAY] * len(allImages)))
