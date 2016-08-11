import re,sys,io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

f = open('a.java',encoding='utf-8')
for line in f.readlines():
	if '豆豆' in line:
		line = line.replace('豆豆','%s')
		line = line.replace('{"','{String.format("')
		line = line.replace(' "','{String.format("')
		re.sub(r' "',"{String.format()\"",line)
		re.sub(r'[^\({ ]{0}"',',DEVICE_NAME)',line)
		print(line)