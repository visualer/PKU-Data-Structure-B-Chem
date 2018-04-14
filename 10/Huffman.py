import sys
sys.path.append("Lib")
from Heap import *
from BiTree import *
from numbers import *
from Stack import *
class HuffmanCoding(ListBiTree):
    def __init__(self, lst, weight_func, index_func):
        #weight is the weight function.
        #for example, lst=list of struct A {char label; int weight;}; then weight_func=lambda x:x.weight
        #index_func is the index function
        #for example, index_func=lambda x:x.label
        
        super(HuffmanCoding, self).__init__()
        d=lambda x:x.root.data if(isinstance(x.root.data, Number)) else weight_func(x.root.data)
        h=Heap(lambda x, y:d(x)<d(y))
        for i in lst:
            h.Insert(LinkBiTree(i))
        while(h.ElemCount()>1):
            c=LinkBiTree()
            c.SetLTree(h.Pop())
            c.SetRTree(h.Pop())
            c.root.data=d(c.GetLTree())+d(c.GetRTree())
            h.Insert(c)

        self.root=h.GetTop().root

        s1=Stack()
        self.dict=dict()
        p=self.root
        
        while(True):
            if(p.lsib==None):
                if(p.rsib!=None):
                    p=p.rsib
                    s1.Push(1)
                else:
                    while(not p is self.root):
                        if(p==p.par.lsib and p.par.rsib!=None):
                            p=p.par.rsib
                            s1.Pop()
                            s1.Push(1)
                            break
                        else:#(p==p.par.rsib)
                            p=p.par
                            s1.Pop()
                    if(p is self.root):
                        return
            else:
                p=p.lsib
                s1.Push(0)
            if((p.lsib is None) and (p.rsib is None)):
                self.dict[index_func(p.data)]=''.join(str(i) for i in s1.Iterable())
        pass
    
    def Construct(self):
        self.__init__()


p=sys.stdin
sys.stdin=open("freq.csv")
a=[[1, 2]]*26
for i in range(26):
    a[i]=str(input()).split(',')
    a[i][1]=float(a[i][1])

s=HuffmanCoding(a, lambda x:x[1], lambda x:x[0])
sys.stdin=p

c=str(input())
for i in c:
    print(s.dict[i], end='')
print()
