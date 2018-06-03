#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config

import game.entity

START_POS = (16 * config.BLOCK, 15 * config.BLOCK)


class Player(game.entity.Entity):
    def __init__(self):
        game.entity.Entity.__init__(self, *START_POS)