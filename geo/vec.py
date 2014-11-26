from math import sqrt

class Vec3:
	_x = 0.0
	_y = 0.0
	_z = 0.0

	def __init__(self, x, y, z):
		self._x = x;
		self._y = y;
		self._z = z;

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, val):
		self._x = val

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self, val):
		self._y = val

	@property
	def z(self):
		return self._z

	@z.setter
	def z(self, val):
		self._z = val

	def __add__(self, other):
		x = self._x + other.x;
		y = self._y + other.y;
		z = self._z + other.z;
		return Vec3(x, y, z)

	def __sub__(self, other):
		x = self._x - other.x;
		y = self._y - other.y;
		z = self._z - other.z;
		return Vec3(x, y, z)

	def __mul__(self, other):
		x = self._x * other.x;
		y = self._y * other.y;
		z = self._z * other.z;
		return Vec3(x, y, z)

	def __eq__(self, other):
		return self._x == other.x and self._y == other.y and self._z == other.z
	
	def dot(self, v):
		return self._x * v.x + self._y * v.y + self._z * v.z

	def project_over(self, v):
		length = self.dot(v)
		return Vec3(length * v.x, length * v.y, length * v.z)

	def length2(self):
		return self._x * self._x + self._y * self._y + self._z * self._z

	def normalize(self):
		length = self.length2()
		if length == 0: return

		length = sqrt(length)
		self._x = self._x / length;
		self._y = self._y / length;
		self._z = self._z / length;

	def cross(self, v):
		return Vec3(self._y * v.z - self._z * v.y,
					self._z * v.x - self._x * v.z,
					self._x * v.y - self._y * v.x)
