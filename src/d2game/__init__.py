#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game.player
import d2game.level


STATE_START = 0
STATE_RUNNING = 1
STATE_EXIT = 2

class Game():
    def __init__(self):
        self.state = STATE_START
        self.hero = self.new_hero()

    def run(self, e):
        self.next_level(e)
        self.state = STATE_RUNNING

    def turn(self):
        self.hero.update(self.level)

    def quit(self):
        self.state = STATE_EXIT
        # raise (SystemExit, "QUIT")

    def new_hero(self):
        return d2game.player.Player()

    def next_level(self, e):
        self.level = d2game.level.Level()
        return self.level

    def is_running(self):
        return self.state == STATE_RUNNING
