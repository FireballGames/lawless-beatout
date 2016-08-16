#!/usr/bin/env python
# -*- coding: utf-8 -*-

import d2game.player

import game
import game.animation

import pygame
import pyganim


START_POS = (400, 450)
PLAYER_SIZE = (73, 100)
MOVE_SPEED = 7
TRANSPARENT_COLOR = "#888888"
JUMP_POWER = 10


class PlayerState():
    def __init__(self):
        self.value = False
        self.anim = None

    def animate(self, player):
        player.image.fill(pygame.Color(TRANSPARENT_COLOR))
        self.anim.blit(player.image, (0,0))


class Player(d2game.player.Player):
    def __init__(self, x, y):
        d2game.player.Player.__init__(self)

        # self.startX = x
        # self.startY = y
        self.pos = START_POS
        self.speed = [0, 0]

        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill(pygame.Color(TRANSPARENT_COLOR))

        self.rect = pygame.Rect((x, y), PLAYER_SIZE)
        self.onGround = True

        s_stay = PlayerState()
        s_right = PlayerState()
        s_left = PlayerState()
        s_up = PlayerState()
        s_down = PlayerState()
        s_jump_right = PlayerState()
        s_jump_left = PlayerState()

        self.states = {
            "stay": s_stay,
            "right": s_right,
            "left": s_left,
            "jump": s_jump_right,
            "jump_right": s_jump_right,
            "jump_left": s_jump_left,
            "up": s_up,
            "down": s_down,
        }

        self.image.set_colorkey(pygame.Color(TRANSPARENT_COLOR))

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

        s_down.anim = pyganim.PygAnimation(game.animation.JUMP)
        s_down.anim.play()

        s_stay.animate(self)


    def go(self, direction, going):
        self.states[direction].value = going

    def is_going(self, direction):
        return self.states[direction].value

    def is_staying(self):
        return not(self.is_going("left") or self.is_going("right") or self.is_going("up") or self.is_going("down"))

    def jump(self):
        if self.onGround:
            self.speed[1] = -JUMP_POWER

    def fall(self):
        self.speed[1] += 0 # GRAVITY

    def update(self, level):
        if self.is_going("left"):
            self.speed[0] = -MOVE_SPEED
            self.states["left"].animate(self)
        if self.is_going("right"):
            self.speed[0] = MOVE_SPEED
            self.states["right"].animate(self)

        if self.is_staying():
            self.speed[0] = 0
            self.speed[1] = 0
            self.states["stay"].animate(self)

        if self.is_going("up"):
            self.speed[1] = -MOVE_SPEED
            self.states["up"].animate(self)
        if self.is_going("down"):
            self.speed[1] = MOVE_SPEED
            self.states["down"].animate(self)

        if self.is_going("jump"):
            self.jump()

        if not self.onGround:
            self.fall()

        self.onGround = True

        self.rect.y += self.speed[1]
        self.collide(0, self.speed[1], level)
        self.rect.x += self.speed[0]
        self.collide(self.speed[0], 0, level)

    def collide(self, xvel, yvel, level):
        if not self.rect.colliderect(level.active_rect):
            if xvel > 0:
                self.rect.left = level.active_rect.right - 1
            if xvel < 0:
                self.rect.right = level.active_rect.left + 1
            if yvel > 0:
                self.rect.top = level.active_rect.bottom - 1
            if yvel < 0:
                self.rect.bottom = level.active_rect.top + 1
        else:
            print("In active")

        for p in level.enemies:
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
