from tkinter import *
from tkinter import ttk
import requests,sys,io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
def func(*args):
	url = 'http://localhost:19200/dialog?deviceid=012345678997&question='
	value = st.get()
	r = requests.get(url + value)
	result.set(value+(15 * '-')+r.content.decode())	

root = Tk()
root.title('test')

mainframe = ttk.Frame(root,padding = '3 3 12 12')
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)

st = StringVar()
result = StringVar()

st_entry = ttk.Entry(mainframe,width=50,textvariable = st)
st_entry.grid(column = 2,row = 1,sticky = (W,E))
ttk.Label(mainframe,textvariable=result).grid(column=2,row = 2,sticky=(W,E))
ttk.Button(mainframe,text = 'Test',command= func).grid(column=3,row = 3,sticky=W)

for child in mainframe.winfo_children():
	child.grid_configure(padx=5,pady=5)

st_entry.focus()
root.bind('<Return>',func)

root.mainloop()