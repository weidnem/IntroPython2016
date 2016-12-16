import sys

class Person(object):
    _registry = []

    def __init__(self, first, last):
        self._registry.append(self)
        self.first = first
        self.last = last

p1 = Person('Ninad', 'Naik')
p2 = Person('Rashmi', "Ashok")
p3 = Person(sys.argv[1], sys.argv[2])

for p in Person._registry:
    print ('{} {}'.format(p.first, p.last))
'''

class Employee:

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

emp_1 = Employee('Ninad', "Naik", 100000)
emp_2 = Employee('Ram', "Madhav", 123000)

print (emp_1.last)'''