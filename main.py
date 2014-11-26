import sys
from geo.vec import Vec3
from algorithm.convexhull.giftwrap import *

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

spin = 0

#  Initialize material property, light source, lighting model,
#  and depth buffer.
def init():
   glClearColor (1.0, 1.0, 1.0, 0.0)
   glShadeModel (GL_SMOOTH)
   glEnable(GL_LIGHTING)
   glEnable(GL_LIGHT0)
   glEnable(GL_DEPTH_TEST)


#  Here is where the light position is reset after the modeling
#  transformation (glRotated) is called.  This places the
#  light at a new position in world coordinates.  The cube
#  represents the position of the light.
def display():
   position =  [0.0, 0.0, 1.5, 1.0]

   glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   glPushMatrix ()
   gluLookAt (0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
   glPushMatrix()
   glColor3f(0, 0, 0)
   glBegin(GL_TRIANGLES)
   points = []
   polygons = []
   points.append(Vec3(0.500000, -0.500000, -0.500000))
   points.append(Vec3(0.500000, -0.500000, 0.500000))
   points.append(Vec3(-0.500000, -0.500000, 0.500000))
   points.append(Vec3(-0.500000, -0.500000, -0.500000))
   points.append(Vec3(0.500000, 0.500000, -0.499999))
   points.append(Vec3(0.499999, 0.500000, 0.500000))
   points.append(Vec3(-0.500000, 0.500000, 0.500000))
   points.append(Vec3(-0.500000, 0.500000, -0.500000))

   polygons = giftwrap(points)
   for poly in polygons:
      for p in poly:
         print(p.x, p.y, p.z)
         glNormal3f(p.x, p.y, p.z)
         glVertex3f(p.x, p.y, p.z)
   glEnd()
   glPopMatrix()
   glFlush ()

def reshape (w, h):
   glViewport (0, 0, w, h)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity()
   gluPerspective(40.0, w/h, 1.0, 20.0)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()

def mouse(button, state, x, y):
   global spin
   if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
       spin = (spin + 30) % 360
       glutPostRedisplay()

def keyboard(key, x, y):
   if key == chr(27):
       sys.exit(0)
   if key == chr(32):
       glutPostRedisplay()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (500, 500);
glutInitWindowPosition(100, 100)
glutCreateWindow("movelight")
init()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMouseFunc(mouse)
glutKeyboardFunc(keyboard)
glutMainLoop()
