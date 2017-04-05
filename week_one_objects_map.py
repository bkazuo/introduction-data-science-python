class Person:
	department = 'School of Information' # a class variable

	def set_name(self, new_name):
		self.name = new_name
	def set_location(self, new_location):
		self.location = new_location


## Class in python
person = Person()
person.set_name('Christopher Brooks')
person.set_location('Ann Arbor, MI, USA')
print('{} live in {} and works in the department {}').format(person.name, person.location, person.department)
print("---------------")


# Example of mapping the min function between two lists.
store1 = [10.00, 11.00, 12.34, 2.34]
stoore2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, stoore2)
print(cheapest)
print("---------------")
