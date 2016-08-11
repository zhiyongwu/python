from functools import reduce

x = reduce(lambda x,y : x * y,range(1,1000))