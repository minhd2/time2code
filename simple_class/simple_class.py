

class Animal:

	def __init__(self, name='', weight=0):
		self.name = name
		self.weight = weight

	def __gt__(self, other_animal):
		if self.weight > other_animal.weight:
			return True
		return False


	def __str__(self):
		return 'name: {}, weight: {}'.format(self.name, self.weight)


#inherit Animal class and having color
class Cat(Animal):

	def __init__(self, name='', weight=0, color=''):
		super().__init__(name, weight)
		self.color = color

	def __str__(self):
		return 'name: {}, weight: {}, color: {}'.format(self.name, self.weight, self.color)


dog = Animal('dog', 23)
small_cat = Cat('billy', 15, 'yellow')


print(dog > small_cat)
print(dog)
print(small_cat)
