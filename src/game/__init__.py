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

    def next_level(self):
        self.level = game.level.Level(self.hero)
        return self.level

    def turn(self):
        d2game.Game.turn(self)
        for e in self.level.enemies:
            e.move(self.level)
