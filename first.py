import re
error_list=[]
first_line=-1
last_line=-1
string=''
def dummy(node):
	pass
def fun1(node):
	'S-> if_block S'
	if node.children[0].correct and 'lambda' not in node.children[1].production:
		print '---ERROR---'
		global string
		string=''
		t.pre_order(node.children[1],print_=0)#y is it printing?it should come before those statements?first should get printed..then those statements..i am passing 0!!oh..
		print 'Following statements are unreachable. Line {} to {}'.format(_f[:_f.index(string.split(';')[0].strip())].count('\n')+1,_f[:_f.index(string.split(';')[0].strip())].count('\n')+len(string.split(';'))-1)
		print string		

		node.correct=node.children[0].correct
	elif 'lambda' in node.children[1].production: node.correct=node.children[0].correct
	else: node.correct=node.children[1].correct
def fun2(node):
	'S-> statement SC S'
	'S-> Decl SC S'
	'S-> EX SC S'
	node.correct=node.children[2].correct
def fun3(node):
	'S-> return *'
	node.correct=True
def fun4(node):
	'S-> Block S'
	Block,S=node.children[0],node.children[1]
	node.correct=Block.correct or S.correct
def fun5(node):
	'S-> lambda'
	node.correct=False
def fun6(node):
	'Block-> OP S CP'
	node.correct=node.children[1].correct
def fun7(node):
	'if_block-> if_cond Block temp_if'
	Block,temp_if=node.children[1],node.children[2]
	node.correct=Block.correct and temp_if.correct
def fun8(node):
	'temp_if-> else Block'
	node.correct=node.children[1].correct
def fun9(node):
	'temp_if-> lambda'
	node.correct=False

def get_leaf_nodes(node):
	if node.production=='':
		return [node.value]
	l=[]
	for i in node.children:
		l+=get_leaf_nodes(i)
	return l

def fun10(node):
    'expr -> id EQ expr'
    id_type={'int':1,'float':2,'double':3}[t.symtab[node.children[0].children[0].value]]
    if id_type < node.children[2].type: 
	print '---ERROR---'#oh..we should print line numbers here!for expressions we have printed no?no..wait..1 min job..
	_l=get_leaf_nodes(node.children[2])
        print 'Error in following expression at line ',_f[:_f.index(''.join(_l))].count('\n')+1#there should be no spaces in exp!
        t.pre_order(node)
	print '\nType of l-value is ',t.symtab[node.children[0].children[0].value]
	for i in _l:
		if i in t.symtab and {'int':1,'float':2,'double':3}[t.symtab[i]]>id_type:
			print '\t',i,'is of type',t.symtab[i]
		elif '.' in i and 'f' in i and id_type<2:
			print '\t',i,'is of type','float'
		elif '.' in i and id_type<3:
			print '\t',i,'is of type','double'


def fun11(node):
    'expr-> expr OPR expr'
    node.type = max(node.children[0].type, node.children[2].type)
def fun12(node):
    'expr-> FNUM'
    node.type = 2
def fun13(node):
    'expr-> DNUM'
    node.type = 3
def fun14(node):
    'expr-> NUM'
    node.type = 1
def fun15(node):
    'expr-> ID'
    node.type={'int':1,'float':2,'double':3}[t.symtab[node.children[0].children[0].value]]
rules={'S : if_block S':fun1,'S : statement SC S':fun2,'':dummy,'S : Decl SC S':fun2,"S : Return ID SC":fun3,"S : Block S":fun4,"S : lambda": fun5,"Block : OP S CP":fun6,"if_block : IF_COND Block temp_if":fun7,'temp_if : ELSE Block':fun8,
       'temp_if : lambda':fun9,'EX : ID EQ EXPR':fun10, 'EXPR : EXPR OPR EXPR':fun11, 'EXPR : FNUM':fun12,'EXPR : DNUM':fun13,'EXPR : NUM':fun14,'S : EX SC S':fun2,'EXPR : ID':fun15}
class Node:
    def __init__(self):
        self.children=[]
        self.value=''
class Tree:
    def __init__(self):
        self.root=Node()
        self.root.value='Start'
        self.list=[]
	self.list_statements=[]
    def searchR(self,root,k):
        if root.value==k and root.children==[]:
            self.found=True
            return root
        res=None
        for r in root.children[::-1]:
            if not(self.found):
                res=self.searchR(r,k)
            else:
                break
        return res
    def search(self,k):
        self.found=False
        return self.searchR(self.root,k)

    def insert(self,head,body):
        r=self.search(head)
        if body=='':body='lambda'
        r.production=head.strip()+' : '+body.strip()
        if body=='':
            t=Node()
            t.value=''
            t.production=''
            r.children.append(t)
            self.list.append(t)
            return
        for i in body.strip().split():
            t=Node()
            if i=='lambda':i=''
            t.value=i
            t.production=''
            r.children.append(t)
            self.list.append(t)
    def pre_order(self,root,print_=1):
	global string
        if root.children==[]:
            string+=root.value+' '
	    
            if print_==1:print root.value,
            return
        for i in root.children:
            self.pre_order(i,print_)

    def check_unreachable(self,root=1):
        if root==1:
            root=self.root.children[4]
        if root!=None:
            
            for i in root.children:
                if i.value not in ['S','if_block','Block','temp_if']:continue
                self.check_unreachable(i)
            rules[root.production](root)
    def traverse_exp_tree(self,root):
        if root!=None:
	    for i in root.children:
                self.traverse_exp_tree(i)
	    if root.production in rules: rules[root.production](root)
    def check_expression(self,root=1):
        if root==1:
            root=self.root.children[4]
        if root!=None:
	    if root.production == 'S : EX SC S':
                self.traverse_exp_tree(root.children[0])
            for i in root.children:
            	self.check_expression(i)
		
            	
    def check_returntypes(self,root=1):
        if root==1:
                self.returntype=self.root.children[0].children[0].children[0].value
                self.symtab={}
                root=self.root
        if root!=None:
            if 'Decl' in root.production and 'ID' in root.production:
                ret_type=root.children[0].children[0].children[0].value
                variable=root.children[1].children[0].value[0]
                self.symtab[variable]=ret_type
            if 'Return' in root.production and len(root.children)>1:
                var=root.children[1].children[0].value[0]
                if self.symtab[var]!=self.returntype:
                    x=root.children[0].value.lower()+' '+var+';'
		    if x not in self.list_statements:
			print('---ERROR---')
                        print('Error in function {} at line {}: '.format(t.root.children[1].children[0].value,_f[:_f.index(x)].count('\n'))+x)
                        print(var+' is of type '+self.symtab[var]+'. Expected return type: '+self.returntype);
                        self.list_statements+=[x]
            for i in root.children:self.check_returntypes(i)
    def __str__(self):
        self.pre_order(self)
        return ''
f=open('./op.txt')
import sys
file=sys.argv[1]
_f=open(file)
_f=_f.read()
l=f.readlines()[::-1]
t=Tree()
for i in l:
    i=i.strip()+' '
    prod_head=i[:i.index('->')]
    prod_body=i[i.index('-> ')+3:].strip()
    if 'lambda' in prod_body:
        prod_body=''
    t.insert(prod_head,prod_body)
    #t.pre_order(t.root)
    #print

t.check_returntypes()
t.check_unreachable()
t.check_expression()
if t.root.children[4].correct!=True:
	print('---ERROR---')
	print('Function '+t.root.children[1].children[0].value+' may not return anything')

