#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game
import d2gui

from level import Level

def main():
    gui = d2gui.GUI()
    g = d2game.Game()

    gui.set_game(g)
    g.l = Level(gui.entities)

    g.run()

    while g.is_running():
        gui.process_events()
        g.turn()
        gui.draw()

if __name__ == "__main__":
    main()
