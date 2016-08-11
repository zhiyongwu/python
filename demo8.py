import time

def countDown(n):
	while n > 0:
		print('T-times',n)
		n -= 1
		time.sleep(5)

from threading import Thread
t = Thread(target = countDown,args=(10,))
t.start()
if t.isAlive():
	print('still running')
else:
	print('completed')