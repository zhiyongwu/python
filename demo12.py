from multiprocessing import Pool
import os,time,random

def run_process(name):
	print('run task %s pid : %s'%(name,os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	print('task runs %.2f' % (time.time()- start))


if __name__ == '__main__':
	print('Parent process pid: %s'%(os.getpid()) )
	p = Pool(4)
	for i in range(5):
		p.apply_async(run_process,args=(i,))
	print('wating for process stop')
	p.close()
	p.join()
	print('All subprocess done')