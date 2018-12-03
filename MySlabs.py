"""
Classes for slab reinforcement calculations
"""

class Slab():
	"""
	Model of a slab
	"""
	def __init__ (self, name: str, thk: float, concrete: float):
		self.name = name
		self.thk = thk
		self.concrete = concrete
	
	def __repr__ (self):
		print(f'Slab({self.name}, {self.thk}, {self.concrete})')

class Band():
	"""
	Model of a band
	"""
	def __init__(self, slab: Slab, width: float, strip_type):
		self.slab = slab
		self.width = width
		self.strip_type = strip_type
	
	def __repr__ (self):
		print(f'Band({self.slab}, {self.width}, {self.strip_type})')
	
	def get_min_reinforcement(self):
		return self.width * self.slab.thk * 0.002
		
class Project():
	"""
	
	"""
	def __init__(self, name: str, number: str, date):
		self.name = name
		self.number = number
		self.date = date
	
	def __repr__ (self):
		print(f'Project({self.name}, {self.number}, {self.date})')
		
	
