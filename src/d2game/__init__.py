#!/usr/bin/env python
# -*- coding: utf-8 -*-

import game
import player

STATE_START = 0
STATE_RUNNING = 1
STATE_EXIT = 2

class Game():
    def __init__(self):
        self.state = STATE_START
        self.hero = player.Player(*game.PLAYER_START)

    def run(self):
        self.state = STATE_RUNNING

    def turn(self):
        self.hero.update(self.l.platforms)

    def quit(self):
        self.state = STATE_EXIT
        # raise (SystemExit, "QUIT")

    def is_running(self):
        return self.state == STATE_RUNNING
