"""
Classes for slab reinforcement calculations
"""

class Slab():
	"""
	Model of a slab
	"""
	def __init__ (self, name: str, thk: float, concrete: float)
		self.name = name
		self.thk = thk
		self.concrete = concrete
	
	def __repr__ (self)
		print(f'Slab({self.name}, {self.thk}, {self.concrete})')

class Band():
	"""
	Model of a band
	"""
	def __init__(self, slab: Slab, width: float, support)
		self.slab = slab
		self.width = width
		self.support = support
	
	def __repr__ (self)
		print(f'Band({self.slab}, {self.width}, {self.support})')
