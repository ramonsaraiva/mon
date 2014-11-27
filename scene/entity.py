from OpenGL.GL import *

from geo.vec import Vec3
from model.object import OBJ_vbo

class Entity:
	def __init__(self):
		self._translate = Vec3.zero()
		self._rotate = Vec3.zero()
		self._scale = Vec3(1, 1, 1)

		self._model = None

	def load_model(self, filename):
		self._model = OBJ_vbo(filename)

	def render(self):
		glPushMatrix()
		glTranslatef(self._translate.x, self._translate.y, self._translate.z)
		glRotatef(self._rotate.x, 1, 0, 0);
		glRotatef(self._rotate.y, 0, 1, 0);
		glRotatef(self._rotate.z, 0, 0, 1);
		glScalef(self._scale.x, self._scale.y, self._scale.z)
		self._model.render()
		glPopMatrix()
