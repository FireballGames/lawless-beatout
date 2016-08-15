#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game
import d2gui

def main():
    gui = d2gui.GUI()
    g = d2game.Game()

    gui.set_game(g)
    g.run(gui.entities)

    while g.is_running():
        gui.process_events()
        g.turn()
        gui.draw()
    g.quit()

if __name__ == "__main__":
    main()
