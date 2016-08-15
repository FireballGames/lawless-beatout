#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game.level
import config
import game
import game.blocks

LEVEL_MAP = [
    "-------------------------",
    "-                       -",
    "-                       -",
    "-                       -",
    "-            --         -",
    "-                       -",
    "--                      -",
    "-                       -",
    "-                   --- -",
    "-                       -",
    "-                       -",
    "-      ---              -",
    "-                       -",
    "--   -----------        -",
    "-                       -",
    "-                -      -",
    "-                   --  -",
    "-                       -",
    "-                       -",
    "-------------------------"]

class Level(d2game.level.Level):
    def __init__(self, entities):
        self.background = "{}/{}".format(config.RES_DIR, game.BACKGROUND_IMAGE)
        self.level_map = LEVEL_MAP
        self.entities = entities
        self.platforms = []

        x=y=0
        for row in self.level_map:
            for col in row:
                if col == "-":
                    pf = game.blocks.Platform(x, y)
                    self.entities.add(pf)
                    self.platforms.append(pf)
                x += pf.width
            y += pf.height
            x = 0
