import logging as log
# Initialization of logging
log.basicConfig(level=log.DEBUG, format='(%(asctime)s): [%(levelname)s] - %(message)s [at line %(lineno)d in %(funcName)s from %(filename)s]')

# Basic imports + importing classes #
import pygame, pygame.freetype, sys, time
from classes import *
from pygame.locals import *

# Initialization of pygame
pygame.init()
log.info(f"Imported and initiated modules")

# Constants ----------------------- #
START_TIME = time.time()
FONT = pygame.freetype.Font("UbuntuMono-Bold.ttf", 15)
CLOCK = pygame.time.Clock()
WIDTH, HEIGHT = SCREEN_RES = (
 pygame.display.Info().current_w,
 pygame.display.Info().current_h
)
SCREEN = pygame.display.set_mode(
  SCREEN_RES, pygame.FULLSCREEN
)
IDEAL_FRAMERATE = 60
TICKRATE = 60

# ^ The difference between these two
# is that IDEAL_FRAMERATE is the max
# FPS the game will run on, but
# TICKSPEED is how fast everything
# in the game will go.

# Variables ----------------------- #
game = classes.GameVariables(
  pos = (0, 0),
  clicking = False,
  debug_menu = False,
  running = True,
  last_time = time.time()
  paused = False
)

# Game Loop ----------------------- #

def main():
	while game.running:
		# FPS Independent Mechanics #
		deltatime = time.time() - game.last_time
		deltatime *= TICKRATE

		# Event Handling ---------- #
		for event in pygame.event.get():
			if event.type == QUIT:
				game.running = False

		# Ensures that FPS isn't higher \
		# than IDEAL_FRAMERATE
		CLOCK.tick(IDEAL_FRAMERATE)

	if not game.running:
		log.info(f"User exiting game")
		pygame.quit()
		sys.exit()

if __name__ == "__main__":
	log.info(f"Game starting")
	main()