#!/usr/bin/env python
# -*- coding: utf-8 -*-

import animation
import pygame
import pyganim


MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"
JUMP_POWER = 10
GRAVITY = 0.35


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.startX = x
        self.startY = y
        self.speed = {
            "x": 0,
            "y": 0,
        }

        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(pygame.Color(COLOR))

        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)
        self.onGround = False

        self.states = {
            "right": False,
            "left": False,
            "up": False,
        }

        self.image.set_colorkey(pygame.Color(COLOR))

        boltAnim = []
        for anim in animation.RIGHT:
            boltAnim.append((anim, animation.DELAY))
        print(boltAnim)
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()

        boltAnim = []
        for anim in animation.LEFT:
            boltAnim.append((anim, animation.DELAY))
        print(boltAnim)
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        self.boltAnimStay = pyganim.PygAnimation(animation.STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))

        self.boltAnimJumpLeft = pyganim.PygAnimation(animation.JUMP_LEFT)
        self.boltAnimJumpLeft.play()
        self.boltAnimJumpRight = pyganim.PygAnimation(animation.JUMP_RIGHT)
        self.boltAnimJumpRight.play()
        self.boltAnimJump = pyganim.PygAnimation(animation.JUMP)
        self.boltAnimJump.play()


    def go(self, direction, going):
        self.states[direction] = going

    def is_going(self, direction):
        return self.states[direction]

    def jump(self):
        if self.onGround:
            self.speed["y"] = -JUMP_POWER

    def fall(self):
        self.speed["y"] += GRAVITY

    def update(self, level):
        if self.is_going("left"):
            self.speed["x"] = -MOVE_SPEED
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimLeft.blit(self.image, (0,0))
            if self.is_going("up"):
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimJumpLeft.blit(self.image, (0,0))
        if self.is_going("right"):
            self.speed["x"] = MOVE_SPEED
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimRight.blit(self.image, (0,0))
            if self.is_going("up"):
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimJumpRight.blit(self.image, (0,0))

        if not (self.is_going("left") or self.is_going("right")):
            self.speed["x"] = 0
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimStay.blit(self.image, (0,0))

        if self.is_going("up"):
            self.jump()
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimJump.blit(self.image, (0,0))

        if not self.onGround:
            self.fall()

        self.onGround = False

        self.rect.y += self.speed["y"]
        self.collide(0, self.speed["y"], level.platforms)
        self.rect.x += self.speed["x"]
        self.collide(self.speed["x"], 0, level.platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.speed["y"] = 0
                    self.onGround = True
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.speed["y"] = 0
