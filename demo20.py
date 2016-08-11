class Number():
	def __init__(self,data):
		self.data = data

	def __sub__(self,num):
		return Number(self.data - num)

if __name__ == '__main__':
	x = Number(3)
	y = x - 2
	print(y.__class__)