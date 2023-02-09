import math
from abc import ABC, abstractmethod

## The first class will be an abstract base class, not to be instantiated ##
class Dog(ABC):
	## Class attributes ##
	species = "Canis familiaris"

	## How to initialize class instantiations ##
	def __init__(self, name, age):
		self.name = name
		self.age = age

	## Instance methods ##
	def __str__(self):
		return f"{self.name} is {self.age} years old."

	def speak(self, sound):
		return f"{self.name} says {sound}."

	## Abstract method that will need to be overridden in instantiated derived classes ##
	@abstractmethod
	def BFQ(self):
		pass

## Child class ##
class Schnauzer(Dog):
	breed = "Schnauzer"
	def speak(self, sound = "ruff"):
		return f"{self.name} says {sound}."

	## We'll treat the bite force of a Schnauzer as negligible ##
	## Note that the abstract method needs to be overridden for this class to be instantiated ##
	def BFQ(self):
		return 0

## Demonstrating inheritance and extension ##
class Pitbull(Dog):
	breed = "Pitbull"
	def __init__(self, name, age, body_mass = 180, bite_force = 120):
		super().__init__(name, age)
		self.body_mass = body_mass
		self.bite_force = bite_force
	## BFQ stands for "Bite Force Quotient"
	def BFQ(self):
		return round(self.bite_force / (10 ** (0.5703 * (math.log(self.body_mass, 10)) + 0.1096)), 1)

## More inheritance ##
class GShepherd(Pitbull):
	breed = "German Shepherd"
	def __init__(self, name, age, body_mass = 200, bite_force = 100, color = "Gray"):
		super().__init__(name, age, body_mass, bite_force)
		self.color = color
	## we'll derive BFQ from Pitbull to keep BFQ consistent across classes in the event the formula changes ##
	def BFQ(self):
		bfq = super().BFQ()
		return bfq

## A class returning the respective BFQs of a list of Dogs ##
class BiteForceIndex:
	def calculate_bfq(self, animals):
		print("Calculating bite force quotients")
		print("================================")
		for animal in animals:
			if isinstance(animal, Dog):
				print(f"Bite force quotient of the {animal.breed} {animal.name}: {animal.BFQ()}")
			else:
				print(f"Bite force quotient of the average {animal.__class__.__name__}: {animal.BFQ()}")

## A non-Dog class that still allows BFQ computation ##
## Note the class BiteForceIndex required if-then statement to circumnavigate the use of breed, name ##
class Hyena:
	def __init__(self, body_mass, bite_force):
		self.body_mass = body_mass
		self.bite_force = bite_force
	def BFQ(self):
		return round(self.bite_force / (10 ** (0.5703 * (math.log(self.body_mass, 10)) + 0.1096)), 1)

c = Schnauzer("Gretchen", 12)
d = Pitbull("Perry", 4)
e = GShepherd("Eliza", 3)
h = Hyena(250, 300)
print(e.BFQ())
BFQs = BiteForceIndex()
BFQs.calculate_bfq([d, e, h])
print(type(BiteForceIndex))
