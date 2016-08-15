#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game.player

import game
import game.animation

import pygame
import pyganim


START_POS = (400, 300)
PLAYER_SIZE = (73, 100)
MOVE_SPEED = 7
COLOR = "#888888"
JUMP_POWER = 10
GRAVITY = 0.35


class PlayerState():
    def __init__(self):
        self.value = False
        self.anim = None

    def animate(self, player):
        player.image.fill(pygame.Color(COLOR))
        self.anim.blit(player.image, (0,0))


class Player(d2game.player.Player):
    def __init__(self, x, y):
        d2game.player.Player.__init__(self)

        # self.startX = x
        # self.startY = y
        self.pos = START_POS
        self.speed = [0, 0]

        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill(pygame.Color(COLOR))

        self.rect = pygame.Rect(x, y, PLAYER_SIZE[0], PLAYER_SIZE[1])
        self.onGround = False

        s_right = PlayerState()
        s_left = PlayerState()
        s_up = PlayerState()
        s_jump_right = PlayerState()
        s_jump_left = PlayerState()
        s_stay = PlayerState()

        self.states = {
            "stay": s_stay,
            "right": s_right,
            "jump_right": s_jump_right,
            "left": s_left,
            "jump_left": s_jump_left,
            "up": s_up,
        }

        self.image.set_colorkey(pygame.Color(COLOR))

        s_right.anim = pyganim.PygAnimation(game.animation.RIGHT)
        s_right.anim.play()

        s_left.anim = pyganim.PygAnimation(game.animation.LEFT)
        s_left.anim.play()

        s_stay.anim = pyganim.PygAnimation(game.animation.STAY)
        s_stay.anim.play()

        s_jump_left.anim = pyganim.PygAnimation(game.animation.JUMP_LEFT)
        s_jump_left.anim.play()
        s_jump_right.anim = pyganim.PygAnimation(game.animation.JUMP_RIGHT)
        s_jump_right.anim.play()
        s_up.anim = pyganim.PygAnimation(game.animation.JUMP)
        s_up.anim.play()

        s_stay.animate(self)


    def go(self, direction, going):
        self.states[direction].value = going

    def is_going(self, direction):
        return self.states[direction].value

    def jump(self):
        if self.onGround:
            self.speed[1] = -JUMP_POWER

    def fall(self):
        self.speed[1] += GRAVITY

    def update(self, level):
        if self.is_going("left"):
            self.speed[0] = -MOVE_SPEED
            self.states["left"].animate(self)
            if self.is_going("up"):
                self.states["jump_left"].animate(self)
        if self.is_going("right"):
            self.speed[0] = MOVE_SPEED
            self.states["right"].animate(self)
            if self.is_going("up"):
                self.states["jump_right"].animate(self)

        if not (self.is_going("left") or self.is_going("right")):
            self.speed[0] = 0
            self.states["stay"].animate(self)

        if self.is_going("up"):
            self.jump()
            self.states["up"].animate(self)

        if not self.onGround:
            self.fall()

        self.onGround = False

        self.rect.y += self.speed[1]
        self.collide(0, self.speed[1], level.platforms)
        self.rect.x += self.speed[0]
        self.collide(self.speed[0], 0, level.platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.speed[1] = 0
                    self.onGround = True
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.speed[1] = 0
