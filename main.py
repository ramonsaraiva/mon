import sys 
from sdl2 import *
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

from spec.cam import Cam
from control import input
from geo.vec import Vec3
from model.object import OBJ_vbo
from algorithm.convexhull.giftwrap import *

width = 800
height = 600
cam = None

buildings = []
bsize = 2

def setup_sdl():
	SDL_Init(SDL_INIT_EVERYTHING)
	window = SDL_CreateWindow('mon',
							  SDL_WINDOWPOS_CENTERED,
							  SDL_WINDOWPOS_CENTERED,
							  width, height, SDL_WINDOW_SHOWN)
	surface = SDL_GetWindowSurface(window)
	return window

def setup_gl():
	glClearColor(0.27451, 0.50, 0.70, 0)
	glClearDepth(1.0)

	glEnable(GL_DEPTH_TEST)
	glEnable(GL_LIGHT0)
	glEnable(GL_LIGHTING)
	glEnable(GL_TEXTURE_2D)
	glEnable(GL_COLOR_MATERIAL)

	glDepthFunc(GL_LESS)
	glEnable(GL_DEPTH_TEST)

	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

	glViewport(0, 0, width, height)

	light_position = [1.0, 1.0, 1.0, 0.0]
	light_specular = [1.0, 1.0, 1.0,1.0]
	light_diffuse = [1.0, 1.0, 1.0,1.0]
	ambient_light = [0.5, 0.5, 0.5, 1.0]

	glShadeModel(GL_SMOOTH)

	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient_light)

	glLightfv(GL_LIGHT0, GL_POSITION, light_position)
	glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()

	gluPerspective(60.0, width / height, 1.0, 1024.0)

def render():
	glClearDepth(1.0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

	cam.compute_lookat()

	for i in xrange(-bsize, bsize):
		for j in xrange(-bsize, bsize):
			for k in xrange(-bsize, bsize):
				glPushMatrix()
				glTranslatef(i*10, j, k*10)
				buildings[i*j+k].render()
				glPopMatrix()


if __name__ == '__main__':
	window = setup_sdl()
	glutInit()
	setup_gl()

	cam = Cam(90, 800, 600, 1000.0)
	cam._position.y = 30
	cam._position.z = -40
	cam.compute_eye()

	for i in xrange(-bsize, bsize):
		for j in xrange(-bsize, bsize):
			for k in xrange(-bsize, bsize):

				buildings.append(OBJ_vbo('resources/b3x1x5.obj'))

	while True:
		input.check()
		cam.refresh()
		render()
		SDL_GL_SwapWindow(window)

	SDL_DestroyWindow(window)
	SDL_Quit()
