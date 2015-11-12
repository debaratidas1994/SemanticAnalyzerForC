import os
import sys
if __name__=='__main__':

	file=sys.argv[1]
	os.system("yacc -d -v sdd2.y && lex lex.l && gcc y.tab.c lex.yy.c && ./a.out<{}>op.txt && python first.py {}>temp.txt".format(file,file))
	f=open('temp.txt').read()#whatever is there in temp.txt, sem_check.py will print!!oh..ok..
	l=open('temp.txt').read().split('---ERROR---')
	print len(l)-1,'Errors Found.'
	for i in l[1:]:
		print i
	os.system('rm a.out && rm op.txt && rm temp.txt && rm y.output && rm y.tab.c && rm y.tab.h && rm lex.yy.c')

	
