#!/usr/bin/python

import pygame
from pygame.locals import *
import sys

from pyni import PyNI

pygame.init()

pygame.display.set_caption('PyNI')
screen = pygame.display.set_mode((640, 480))

pyni = PyNI()

while pyni.running:
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE): pyni.running = False
	# for

	pyni.update()
	pyni.draw_depth(screen)

	pygame.display.flip()
# while

pyni.quit()
sys.exit(0)