class Zoo(object):
	def __init__(self, animal_type):
		self.animal_type = animal_type
		self.animals = {}
	def add_animal(self, animal):
		animal_id = id(animal)
		if animal_id in self.animals:
			return
		self.animals[animal_id] = animal
		if not hasattr(self, animal_type):
			setattr(self, animal_type, [animal])
		else:
			self[animal_type].append(animal)

from abc import ABCMeta, abstractmethod
class Animal(metaclass=ABCMeta):
	@abstractmethod
	def __init__(self, species, shape, character):
		self.species = species
		self.shape = shape
		self.character = character
	@property
	def is_beast(self):
		if self.species == "食肉"
			and self.character == "凶猛"
			and (self.shape == "中" or self.shape == "大"):
			return True
		return False

class Cat(Animal):
	sound = "miao"
	def __init__(self, name, species, shape, character):
		super(Cat, self).__init__(species, shape, character)
		self.name = name
	@property
	def is_pet(self):
		return not self.is_beast

if __name__ == "__main__":
	z = Zoo('时间动物园')
	cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
	z.add_animal(cat1)
	have_cat = getattr(z, 'Cat')
