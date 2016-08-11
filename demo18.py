import threading,time

threads = []

count = 1
def task(n):
	x = 2
	x *= 5 ** 15 + 2 ** 100
	x += 1 / x ** 101
	time.sleep(1)
	print(x)
	print(threading.active_count())

if __name__ == '__main__':
	for n in range(1000):
		threads.append(threading.Thread(target=task,args=(n,)))
	for i in threads:
		i.start()

