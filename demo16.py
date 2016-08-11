import time,threading

def loop():
	print('thread %s start' % threading.currentThread().getName())
	time.sleep(1)
	print('thread %s stop' % threading.currentThread().getName())

if __name__ == '__main__':
	 print('thread %s start' % threading.currentThread().getName())
	 t = threading.Thread(target=loop,args=())
	 t.start()
	 t.join()
	 print('thread %s stop' % threading.current_thread().name)