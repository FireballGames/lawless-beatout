#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game
import game.player
import game.level


TITLE = "Beat'em up"
BACKGROUND_IMAGE = "back.png"


class Game(d2game.Game):
    def new_hero(self):
        return game.player.Player(*game.player.START_POS)

    def next_level(self, e):
        self.level = game.level.Level(e)
        return self.level
