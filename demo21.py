import functools
def positive_result(func):
	def wrapper(*args,**kargs):
		result = func(*args,**kargs)
		assert result > 0,func.__name__ + '() result is not > 0'
		return result
		wrapper.__name__ = func.__name__
		wrapper.__doc__ = func.__doc__
	return wrapper


def positive_res(func):
	@functools.wraps(func)
	def wrapper(*args,**kargs):
		result = func(*args,**kargs)
		assert result > 0,func.__name__ + '() result is not > 0'
		return result
	return wrapper
	
@positive_res
def f(a,b,c):
	return (b ** 2) - (4 * a *c)

if __name__ == '__main__':
	print(f(1,2,2))