from multiprocessing import Process
import os
#多个进程

def runProcess(name):
	print('run child process %s pid: %s' % (name,os.getpid()))

if __name__ == '__main__':
	print('Parent process %s running ' % os.getpid())
	p = Process(target= runProcess,args = ('childProcess',))
	p.start()
	p.join()
	print('child process end')