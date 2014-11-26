from geo.vec import Vec3

def giftwrap(points):
	polygons = []
	open_edges = []
	created_edges = {}

	def edge_exists(e):
		key = '{0}_{1}'.format(e[0], e[1])
		return key in created_edges

	def add_edge(e):
		key = '{0}_{1}'.format(e[0], e[1])
		created_edges[key] = True
		if not edge_exists(e[::-1]):
			open_edges.append(e[::-1])

	p1 = lower(points)
	p2 = next_point(points, p1, -1)

	print('lower', p1)
	print('next', p2)

	add_edge((p2, p1))

	while len(open_edges):
		edge = open_edges.pop()

		if edge_exists(edge):
			continue

		p1 = edge[0]
		p2 = edge[1]
		p3 = next_point(points, p1, p2)

		polygons.append((points[p1], points[p2], points[p3]))
		add_edge((p1, p2))
		add_edge((p2, p3))
		add_edge((p3, p1))

	return polygons

def lower(points):
	lowpi = 0
	for i, p in enumerate(points):
		lowp = points[lowpi]
		
		if p.z < lowp.z:
			lowpi = i
		elif p.z == lowp.z:
			if p.y < lowp.y:
				lowpi = i
			elif p.y == lowp.y:
				if p.x < lowp.x:
					lowpi = i
	return lowpi

def next_point(points, p1i, p2i):
	p1 = points[p1i]
	p2 = None

	if p2i < 0:
		p2 = p1 - Vec3(1, 1, 0)
	else:
		p2 = points[p2i]

	edge = p2 - p1
	edge.normalize()

	p3i = -1

	for i, p in enumerate(points):
		if i == p1i or i == p2i:
			continue

		if p3i == -1:
			p3i = i
			continue

		v = p - p1
		v = v - v.project_over(edge)
		p3 = points[p3i] - p1
		p3 = p3 - p3.project_over(edge)

		cross = p3.cross(v)
		if cross.dot(edge) > 0:
			p3i = i

	return p3i
