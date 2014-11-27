from OpenGL.GL import *
import pygame

from .singleton import Singleton

@Singleton
class ResourceManager(object):
	def __init__(self):
		self._textures = {}

	def add_texture(self, texture):
		if texture in self._textures:
			return self._textures[texture]

		texid = self._textures[texture] = glGenTextures(1)
		surface = pygame.image.load(texture)
		image = pygame.image.tostring(surface, 'RGBA', 1)
		image_x, image_y = surface.get_rect().size

		glBindTexture(GL_TEXTURE_2D, texid)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image_x, image_y, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)

	def get_texture(self, texture):
		if texture in self._textures:
			return self._textures[texture]
		return 0
