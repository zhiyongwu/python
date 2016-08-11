from multiprocessing import Queue,Process
import os,time,random

def write(q):
	print('Process to write %s ' % os.getpid())
	for value in ['a','b','c']:
		print('put %s to q' % value)
		q.put(value)
		time.sleep((random.random()))

def read(q):
	print('Process to read %s ' % os.getpid())
	while True:
		print(1)
		value = q.get()
		print('Get %s from q' % value)


if __name__ == '__main__':
	print('Parent process pid: %s ' % os.getpid())
	q = Queue()
	pw = Process(target=write,args = (q,))
	pr = Process(target=read,args = (q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()