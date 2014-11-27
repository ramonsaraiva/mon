from OpenGL.GL import *

from geo.vec import Vec3
from model.object import OBJ_vbo

class Entity(object):
	def __init__(self):
		self._translate = Vec3.zero()
		self._rotate = Vec3.zero()
		self._scale = Vec3(1, 1, 1)

		self._model = None

	def load_model(self, filename):
		self._model = OBJ_vbo(filename)

	@property
	def translate(self):
		return self._translate

	@translate.setter
	def translate(self, val):
		if isinstance(val, list):
			self._translate = Vec3(*val)
			return
		if isinstance(val, Vec3):
			self._translate = val

	@property
	def rotate(self):
		return self._rotate

	@rotate.setter
	def rotate(self, val):
		if isinstance(val, list):
			self._rotate = Vec3(*val)
			return
		if isinstance(val, Vec3):
			self._rotate = val

	@property
	def scale(self):
		return self._scale

	@scale.setter
	def scale(self, val):
		if isinstance(val, list):
			self._scale = Vec3(*val)
			return
		if isinstance(val, Vec3):
			self._scale = val

	def render(self):
		glPushMatrix()
		glTranslatef(self._translate.x, self._translate.y, self._translate.z)
		glRotatef(self._rotate.x, 1, 0, 0);
		glRotatef(self._rotate.y, 0, 1, 0);
		glRotatef(self._rotate.z, 0, 0, 1);
		glScalef(self._scale.x, self._scale.y, self._scale.z)
		self._model.render()
		glPopMatrix()
