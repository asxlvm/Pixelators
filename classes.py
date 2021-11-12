import pygame, math, random
import logging as log
from dataclasses import dataclass

@dataclass
class GameVariables:
	pos: tuple
	clicking: bool
	running: bool
	debug_menu: bool
	paused: bool
	last_time: float

class RocketSprite:
	BASIC = {"0": {"gun_xy": [], "animation_dir": "data/0/animations/", "static": "data/0/static.png"}}
	DOUBLE = {"1": {"gun_xy": [], "animation_dir": "data/1/animations/", "static": "data/1/static.png"}}
	TRIPLE = {"2": {"gun_xy": [], "animation_dir": "data/2/animations/", "static": "data/2/static.png"}}
	FAST_ROCKET_MINI = {"3": {"gun_xy": [], "animation_dir": "data/3/animations/", "static": "data/3/static.png"}}
	FAST_ROCKET = {"4": {"gun_xy": [], "animation_dir": "data/4/animations/", "static": "data/4/static.png"}}
	BIG_ROCKET = {"5": {"gun_xy": [], "animation_dir": "data/5/animations/", "static": "data/5/static.png"}}
	ROCKET_JET = {"6": {"gun_xy": [], "animation_dir": "data/6/animations/", "static": "data/6/static.png"}}
	UFO = {"7": {"gun_xy": [], "animation_dir": "data/7/animations/", "static": "data/7/static.png"}}
	ALL = [BASIC, DOUBLE, TRIPLE, FAST_ROCKET_MINI, FAST_ROCKET, BIG_ROCKET, ROCKET_JET, UFO]
	
	def __init__(self, _id: int):
		for i in self.ALL:
			for key, val in i.items():
				if key == str(_id):
					self.rocket = val
					break
		self.guncoords = self.rocket["gun_xy"]
		self.animdir = self.rocket["animation_dir"]
		self.staticimg = self.rocket["static"]
		self.id = _id

class Rocket:
	DOWN = 0
	UP = 1
	LEFT = 2
	RIGHT = 3
	def __init__(self, _id: int, x: int, y: int, img, hp:int, bullet_speed: int, bullet_spread: int, bullet_type: int, aim_dir: int):
		self.x = x
		self.y = y
		self.spriteinfo = RocketSprite(_id)
		self.animdir = self.spriteinfo.animdir
		self.staticimg = self.spriteinfo.staticimg
		self.id = _id
		self.guncoords = self.spriteinfo.guncoords
		self.img = img
		self.rect = pygame.Rect((self.x, self.y, self.img.get_width(), self.img.get_height()))
		self.hp = hp
		self.bspeed = bullet_speed
		self.bspread = bullet_spread
		self.btype = bullet_type
		self.aimdir = aim_dir

class Player(Rocket):
	def __init__(self, type: int, x: int, y: int, img, hp:int, bullet_speed: int, bullet_spread: int, bullet_type: int):
		super().__init__(x, y, img, hp, bullet_speed, bullet_spread, bullet_type, aim_dir)
		self.aimdir = Rocket.UP
	
	def calc_spread(self):
		spread = random.randint(-self.bspread, self.bspread)
		self.x += spread
		return spread
	
	def move(self, mx, my, dt):
		"""
		Moves the rect's position to the mouse position that's been passed in, then multiplies it by the deltatime of the last tick for framerate independency.
		"""  
		self.rect.x = mx * dt
		self.rect.y = my * dt

class Bullet:
	NORMAL = 0
	EXPLOSIVE = 1
	FREEZE = 2
	def __init__(self, rect, to_x, to_y, spread):
		"""
		Initialization of the bullet, assign the passed-in variables, calculate the angle and delta positions.
		"""
		self.rect = rect
		self.x = self.rect.x
		self.y = self.rect.y
		spread = random.randint(-spread, spread)
		self.to_x = to_x + spread
		self.to_y = to_y + spread
		angle = math.atan2(
		  self.to_y - self.y, self.to_x - self.x
		)
		self.dx = math.cos(angle)
		self.dy = math.sin(angle)
	
	def move(self, dt, speed):
	    """
	    Move the x and y position by their delta pos which has been calculated on initialization of the Bullet, then we multiply it by the desired speed, and we also multiply it by the deltatime of the last tick for framerate independency.
	    """
	    self.x = self.x + self.dx * speed * dt 
	    self.y = self.y + self.dy * speed * dt
	    self.rect.x = int(self.x)
	    self.rect.y = int(self.y)
	    return [self.dx * speed * dt, self.dy * speed * dt]
