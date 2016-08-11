from abc import ABCMeta,abstractmethod

class Super(metaclass = ABCMeta):
	def __init__(self):
		pass
	@abstractmethod
	def method(self):
		pass
	def method1(self):
		pass



if __name__ == '__main__':
	x = Super()
	x.method1()