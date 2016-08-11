import functools

def bounded(mini,maxi):
	def dector(func):
		@functools.wraps(func)
		def wrapper(*args,**kargs):
			result = func(*args,**kargs)
			if result < mini:
				return mini
			if result > maxi:
				return maxi
			return result
		return wrapper
	return dector

@bounded(0,100)
def percent(amonut,total):
	return (amonut / total) * 100

if __name__ == '__main__':
	print(percent(100,10))
