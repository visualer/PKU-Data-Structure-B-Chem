from Classes import *

class Dict:
    def __init__(self, keyfunc):
        self.tree=LinkBiTree()
        self.keyfunc=keyfunc
        pass
    def Insert(self, _record):
        k=hash(self.keyfunc(_record))
        if(self.tree.isEmpty()):
            self.tree.root.data=[k, _record]
        elif(self.tree.root.data[0]==k):
            self.tree.root.data.append(_record)
        else:
            p=self.tree.root
            while(True):
                if(p.data[0]>k):
                    if(p.rsib is None):
                        p.rsib=BTNode([k, _record], None, None, p)
                        return
                    else:
                        p=p.rsib
                elif(p.data[0]<k):
                    if(p.lsib is None):
                        p.lsib=BTNode([k, _record], None, None, p)
                        return
                    else:
                        p=p.lsib
                else:
                    p.data.append(_record)
                    return
        pass
    def Search(self, _key): #returns the record if found
        k=hash(_key)
        p=self.tree.root
        if(self.tree.isEmpty()):
            return None
        while(True):
            if(p.data[0]>k):
                if(p.rsib is None):
                    return None
                else:
                    p=p.rsib
            elif(p.data[0]<k):
                if(p.lsib is None):
                    return None
                else:
                    p=p.lsib
            else:
                for i in p.data[1:]:
                    if(self.keyfunc(i)==_key):
                        return i
                return None
        pass
    
    def Delete(self, _key):
        k=hash(_key)
        p=self.tree.root
        if(self.tree.isEmpty()):
            return False
        while(True):
            if(p.data[0]>k):
                if(p.rsib is None):
                    return False
                else:
                    p=p.rsib
            elif(p.data[0]<k):
                if(p.lsib is None):
                    return False
                else:
                    p=p.lsib
            else:
                for i in range(1, len(p.data)-1):
                    if(self.keyfunc(i)==_key):
                        del p.data[i]
                        if(len(p.data)==1):
                            if(p is self.tree.root):
                                p.data=None
                                return
                            if(p.rsib is None):
                                if(p is p.par.lsib):
                                    p.par.lsib=p.lsib
                                    p.lsib.par=p.par
                                else:
                                    p.par.rsib=p.lsib
                                    p.lsib.par=p.par
                            elif(p.lsib is None):
                                if(p is p.par.lsib):
                                    p.par.lsib=p.rsib
                                    p.rsib.par=p.par
                                else:
                                    p.par.rsib=p.rsib
                                    p.rsib.par=p.par
                            else:
                                q=p.lsib
                                while(q.rsib is None):
                                    q=q.lsib
                                while(q.rsib is not None):
                                    q=q.rsib
                                q.rsib=p.rsib
                                p.rsib.par=q
                        return True
                return False
        pass
    pass

#TEST
l=Dict(lambda x:x[0])
s, sys.stdin=sys.stdin, open("in.csv")
print("source: in.csv")
while(True):
    try:
        x=input()
    except(EOFError):
        break
    x=str(x).split(',')
    l.Insert((x[0],x[1]))

sys.stdin=s
'''while(True):
    x=l.Search(str(input("word:")))
    print(x[1] if x else x)'''

l.tree.Visualize()


        
