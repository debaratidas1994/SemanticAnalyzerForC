from Tkinter import Tk
#from Tkinter import *
from tkFileDialog import askopenfilename
#import subprocess as sub
import os
import sys

# this file only opens file browser..can u just run this? ok

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file


if __name__=='__main__':
	file=filename
	#file=sys.argv[1]
	#p = sub.Popen('./script',stdout=sub.PIPE,stderr=sub.PIPE)
	os.system("yacc -d -v sdd2.y && lex lex.l && gcc y.tab.c lex.yy.c && ./a.out<{}>op.txt && python first.py {}>temp.txt".format(file,file))
	f=open('temp.txt').read()#whatever is there in temp.txt, sem_check.py will print!!oh..ok..
	l=open('temp.txt').read().split('---ERROR---')
	print len(l)-1,'Errors Found.'
	for i in l[1:]:
		print i
	os.system('rm a.out && rm op.txt && rm temp.txt && rm y.output && rm y.tab.c && rm y.tab.h && rm lex.yy.c')
	
	
	

