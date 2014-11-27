import os.path

from OpenGL.GL import *
import pygame

from control.resources import ResourceManager

class MTL(object):
	"""Material info for a 3-D model as represented in an MTL file"""
	def __init__(self, filename):
		"""Read data from the file"""
		self.contents = {}
		mtl = None
		for line in open(filename, "r"):
			if line.startswith('#'): continue
			values = line.split()
			if not values: continue
			if values[0] == 'newmtl':
				mtl = self.contents[values[1]] = {}
			elif mtl is None:
				raise ValueError, "mtl file doesn't start with newmtl stmt"
			elif values[0] == 'map_Kd':
				mtl[values[0]] = os.path.join(os.path.dirname(filename), values[1])
			else:
				mtl[values[0]] = map(float, values[1:])

	def generate(self):
		"""Generate the textures necessary for any materials"""
		for mtl in self.contents.values():
			if "map_Kd" not in mtl: continue
			ResourceManager.Instance().add_texture(mtl['map_Kd'])

	def bind(self, material):
		mtl = self.contents[material]
		tex = ResourceManager.Instance().get_texture(mtl['map_Kd'])
		if tex:
			glBindTexture(GL_TEXTURE_2D, tex)
		else:
			glBindTexture(GL_TEXTURE_2D, 0)
			glColor(*mtl['Kd'])
