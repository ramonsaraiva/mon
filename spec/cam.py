from math import sin, cos, pi

from OpenGL.GL import *
from OpenGL.GLU import *

from geo.vec import Vec3
from control import input

class Cam(object):
	def __init__(self, angle, width, height, depth):
		self._position = Vec3.zero()
		self._direction = Vec3.zero()

		self._angle = angle
		self._width = width
		self._height = height
		self._depth = depth
		self._speed = 0.05

		self.compute_direction()
		self.reset_view()

	def refresh(self):
		kb = input.keyboard_status()

		if kb['moving_ws'] != 0:
			self.move(kb['moving_ws'])
		if kb['moving_da'] != 0:
			self.strafe(kb['moving_da'])

		if kb['looking']:
			mouse = input.mouse_status()
			self.direction_y(mouse['y'])
			self.angle(mouse['x'])

	def compute_lookat(self):
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

		gluLookAt(self._position.x,
				  self._position.y,
				  self._position.z,
				  self._direction.x,
				  self._position.y + self._direction.y,
				  self._direction.z,
				  0.0, 1.0, 0.0)

	def compute_direction(self):
		self._direction.x = cos(self._angle * pi / 180) + self._position.x
		self._direction.z = sin(self._angle * pi / 180) + self._position.z

	def reset_view(self):
		glViewport(0, 0, self._width, self._height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()

		gluPerspective(45.0, self._width/float(self._height), 0.2, self._depth)
		self.compute_lookat()

	def angle(self, angle):
		self._angle += angle
		self._angle = self._angle % 360.

		self.compute_eye()

	def direction_y(self, y):
		self._direction.y += y
		self.compute_lookat()

	def speed(self, speed):
		self._speed = s

	def move(self, direction):
		self._position.x += self._speed * direction * cos(self._angle * pi / 180)
		self._position.y += self._speed * direction * self._direction.y
		self._position.z += self._speed * direction * sin(self._angle * pi / 180)

		self.compute_eye()


	def strafe(self, direction):
		angle = self._angle * pi / 180 - (pi / 2)
		self._position.x += self._speed * cos(angle) * direction
		self._position.z += self._speed * sin(angle) * direction

		self.compute_eye()

	def compute_eye(self):
		self.compute_direction()
		self.compute_lookat
