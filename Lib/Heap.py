from BiTree import *

class Heap(LinkBiTree):
    def __init__(self, cmp_priority):
        super(Heap, self).__init__()
        self.elem=0
        self.tail=self.root
        self.cmp=lambda x, y:cmp_priority(x, y) if (not(x is None or y is None)) else None if(x is None and y is None) else (y is None)
        pass
    
    def isEmpty(self):
        return self.elem==0
    
    def Insert_without_Update(self, data):#O(log n)
        if(self.isEmpty()):
            self.root.data=data
        else:
            p=self.tail
            while(True):
                if(p is self.root):
                    break
                if(p is p.par.lsib):
                    if(not p.par.rsib is None):
                        p=p.par.rsib
                        break
                    else:
                        p.par.rsib=BTNode(data, None, None, p.par)
                        self.tail=p.par.rsib
                        self.elem+=1
                        return
                else:
                    p=p.par
            while(not p.lsib is None):
                p=p.lsib
            p.lsib=BTNode(data, None, None, p)
            self.tail=p.lsib
        self.elem+=1
        pass

    def Insert(self, data):
        self.Insert_without_Update(data)
        self.Update()
        pass
    
    def Update(self):
        self.Sift_Up()
        pass
    
    def Heapify(self):
        self.Sift_Down(0)
        pass
    
    def Locate(self, index):
        p=self.root
        if(index==0):
            return p
        s=[]
        while(index!=0):
            s.append((index+1)%2)
            index=(index-1)//2
        for i in s[::-1]:
            if(i==1):
                p=p.rsib
            else:
                p=p.lsib
        return p

    def __getitem__(self, index):
        return self.Locate(index).data

    def __setitem__(self, index, data):
        p=self.Locate(index)
        p.data=data
        self.Sift_Up(p)
        if(p.data==data):
            self.Sift_Down(p)
        pass
    
    def Sift_Down(self, index):
        p=index if(type(index) is BTNode) else self.Locate(index)
        while(True):
            if(p.lsib is None and p.rsib is None):
                return
            elif(p.rsib is None or (not(p.lsib is None) and self.cmp(p.lsib.data, p.rsib.data) is True)):
                if(self.cmp(p.lsib.data, p.data) is True):
                    p.lsib.data, p.data=p.data, p.lsib.data
                    p=p.lsib
                else:
                    return
            else:#(p.lsib is None or (not(p.rsib is None) and self.cmp(p.rsib.data, p.lsib.data) is True))
                if(self.cmp(p.rsib.data, p.data) is True):
                    p.rsib.data, p.data=p.data, p.rsib.data
                    p=p.rsib
                else:
                    return
        pass
    
    def Sift_Up(self, index=-1):
        p=self.tail if(index==-1 or index==self.elem-1) else index if(type(index) is BTNode) else self.Locate(index)
        while(not p.par is None and self.cmp(p.data, p.par.data) is True):
            p.data, p.par.data=p.par.data, p.data
            p=p.par
        pass
    
    def GetTop(self):
        return self.root.data
    
    def Delete(self):
        if(self.elem==1):
            self.root.data=None
            self.elem=0
            return
        self.root.data=self.tail.data
        self.elem-=1
        
        #Locate New Tail, or use p=self.Locate(self.elem-1)
        p=self.tail
        while(True):
            if(p is self.root):
                break
            if(p is p.par.rsib):
                p=p.par.lsib
                break
            else:
                p=p.par
        while(not p.rsib is None):
            p=p.rsib
        
        if(self.tail.par.lsib is self.tail):
            self.tail.par.lsib=None
        else:
            self.tail.par.rsib=None
        self.tail=p
        
        self.Sift_Down(0)
        pass

    def Pop(self):
        x=self.GetTop()
        self.Delete()
        return x
    
    def ElemCount(self):
        return self.elem
