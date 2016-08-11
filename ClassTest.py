class pair:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __repr__(self):
		return 'Pair({0.x!r},{0.y!r})'.format(self)

	def __str__(self):
		return '({0.x!r},{0.y!r})'.format(self)

if __name__ == '__main__':
	p = pair(3,4)
	import pprint
	pprint.pprint(p)
	print(p)