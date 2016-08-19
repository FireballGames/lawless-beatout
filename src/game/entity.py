#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import resource

import pygame
import pyganim

import d2game.player
import game.animation


SIZE = (2 * config.BLOCK, 5 * config.BLOCK)
TRANSPARENT = "#888888"
MOVE_SPEED = config.BLOCK
JUMP_POWER = config.BLOCK


class EntityState():
    def __init__(self):
        self.value = False
        self.anim = None

    def animate(self, entity):
        entity.image.fill(pygame.Color(TRANSPARENT))
        self.anim.blit(entity.image, (0,0))

    def set_animation(self, animation):
        self.anim = animation
        self.anim.play()

class Entity(d2game.player.Player):
    def __init__(self, x, y):
        d2game.player.Player.__init__(self)

        self.width = SIZE[0]
        self.height = SIZE[1]

        self.image = pygame.Surface(SIZE)
        self.image.fill(pygame.Color(TRANSPARENT))
        self.rect = pygame.Rect((x, y), SIZE)
        self.image.set_colorkey(pygame.Color(TRANSPARENT))

        self.speed = [0, 0]        
        self.onGround = True
        
        s_stay = game.entity.EntityState()
        s_right = game.entity.EntityState()
        s_left = game.entity.EntityState()
        s_up = game.entity.EntityState()
        s_down = game.entity.EntityState()
        s_jump_right = game.entity.EntityState()
        s_jump_left = game.entity.EntityState()

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

        s_right.set_animation(pyganim.PygAnimation(game.animation.RIGHT))
        s_left.set_animation(pyganim.PygAnimation(game.animation.LEFT))
        s_stay.set_animation(pyganim.PygAnimation(game.animation.STAY))

        s_jump_left.set_animation(pyganim.PygAnimation(game.animation.JUMP_LEFT))
        s_jump_right.set_animation(pyganim.PygAnimation(game.animation.JUMP_RIGHT))

        s_up.set_animation(pyganim.PygAnimation(game.animation.JUMP))
        s_down.set_animation(pyganim.PygAnimation(game.animation.JUMP))
        
        self.state = s_stay
        self.state.animate(self)
        

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

        # if self.is_going("jump"):
        #     self.jump()

        # if not self.onGround:
        #     self.fall()

        self.onGround = True

        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        self.collide((0, self.speed[1]), level)
        self.collide((self.speed[0], 0), level)
        # self.collide(self.speed, level)
        
    def collide(self, speed, level):
        if not self.rect.colliderect(level.active_rect):
            if speed[0] > 0:
                self.rect.left = level.active_rect.right - 1
            if speed[0] < 0:
                self.rect.right = level.active_rect.left + 1
            if speed[1] > 0:
                self.rect.top = level.active_rect.bottom - 1
            if speed[1] < 0:
                self.rect.bottom = level.active_rect.top + 1
        pass

        # for p in level.enemies:
            # if pygame.sprite.collide_rect(self, p):
                # if speed[0] > 0:
                    # self.rect.right = p.rect.left
                # if speed[0] < 0:
                    # self.rect.left = p.rect.right
                # if speed[1] > 0:
                    # self.rect.bottom = p.rect.top
                # if speed[1] < 0:
                    # self.rect.top = p.rect.bottom