import subprocess

p = subprocess.Popen(['python'],stdin = subprocess.PIPE,stdout = subprocess.PIPE,stderr = subprocess.PIPE)
output,err= p.communicate(b'demo12.py')
print(p.returncode)