from threading import Thread
import time

s = time.time()
for i in range(10000):
	t = Thread(target=print,args=((i,)))
	t.start()
print('-'*20,time.time() - s)

s = time.time()
for i in range(10000):
	print(i)
print('-'*20,time.time() - s)
