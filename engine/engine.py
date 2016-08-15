#!/usr/bin/python
#
# -*- coding: utf-8 -*-
#
import pygame

window = pygame.display.set_mode((800,600))
pygame.display.set_caption('Engine')

screen = pygame.Surface((800,600))

class Sprite:
	def __init__(self,xpos,ypos,filename):
		self.x=xpos
		self.y=ypos
		self.bitmap=pygame.image.load(filename)
	def render(self):
		screen.blit(self.bitmap,(self.x,self.y))

back = Sprite(0,0,'back.png')
hero = Sprite(50,300,'man.png')


done = True
pygame.key.set_repeat(1,1)
while done:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			done = false
# player control block
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_RIGHT:
				if hero.x < 727:
					hero.x += 5
			if e.key == pygame.K_LEFT:
				if hero.x > 1:
					hero.x -= 5
			if e.key == pygame.K_UP:
				if hero.y > 270:
					hero.y -= 5
			if e.key == pygame.K_DOWN:
				if hero.y < 500:
					hero.y += 5
					
	back.render()
	hero.render()
	window.blit(screen, (0,0))
	pygame.display.flip()