def manaul_iter():
	with open('demo.py') as f:
		try:
			while True:
				line = next(f)
				print(line,end=' ')
		except StopIteration:
			...

if __name__ == '__main__':
	manaul_iter(