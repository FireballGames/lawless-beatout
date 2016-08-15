#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blocks import Platform

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

class Level():
    def __init__(self, entities):
        self.level_map = LEVEL_MAP
        self.entities = entities
        self.platforms = []

        x=y=0
        for row in self.level_map:
            for col in row:
                if col == "-":
                    pf = Platform(x, y)
                    self.entities.add(pf)
                    self.platforms.append(pf)
                x += pf.width
            y += pf.height
            x = 0
