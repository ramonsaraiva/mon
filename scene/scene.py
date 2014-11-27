from entity import Entity

class Scene:
	def __init__(self):
		self._entities = []

	def add_entity(self, entity=None):
		if entity is None:
			entity = Entity()
		self._entities.append(entity)
		return entity

	def render(self):
		for e in self._entities:
			e.render()
