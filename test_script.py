
import os
from tkFileDialog import askopenfilename
from Tkinter import * 
root=Tk()
root.withdraw() # what does Tk() do ? cretaes instance ?i guess..so create an instance of diff name and use it 
filename = askopenfilename() # this command allows the file browser choosing, whatever u choose here goes to filename
file=filename
os.system('python sem_check.py {}>temp_op.txt'.format(filename))
contents=open('temp_op.txt').read()
T=Text(Tk(),height=contents.count('\n'),width=100)
T.pack()
T.insert(END,contents)
mainloop()
