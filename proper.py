class Person:
	def __init__(self,first_name):
		self.first_name = first_name

	@property
	def first_name(self):
		return self._first_name
	
	@first_name.setter
	def first_name(self,value):
		if not isinstance(value,str):
			raise TypeError('Exceped a string')
		self._first_name = value

	@first_name.deleter
	def first_name():
		raise AttributeError('Can\'t delete attribute')


if __name__ == '__main__':
	a = Person('Guido')
	print(a)
	a.first_name = '42'
	del a.first_name