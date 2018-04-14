from Stack import *
class BTNode:
    def __init__(self, data, lsib, rsib, par):
        self.data=data
        self.lsib=lsib
        self.rsib=rsib
        self.par=par
        pass

class LinkBiTree:
#回溯有不使用标志位，不使用栈
#和递归进行两种
    def __init__(self, data=None):
        self.root=BTNode(data, None, None, None)
        pass
    
    def _Construct(self, root):
        self.root=root
        pass
    
    def ConstructFromList(self, expr):
        p=self.root
        for s in expr:
            if(s=="#"):
                if(p is p.par.lsib):
                    p=p.par
                    p.lsib=None
                    p.rsib=BTNode(None, None, None, p)
                    p=p.rsib
                elif(p is p.par.rsib):
                    p=p.par
                    p.rsib=None
                    while(not p is self.root):
                        p=p.par
                        if(p.rsib==None):
                            p.rsib=BTNode(None, None, None, p)
                            p=p.rsib
                            break
                if(p is self.root):
                    return
                continue
            p.data=s
            p.lsib=BTNode(None, None, None, p)
            p=p.lsib
        pass
    
    def GetHeadTree(self):
        return LinkBiTree(self.root.data)
    
    def GetLTree(self):
        if(self.root.lsib==None):
            return None
        s=LinkBiTree()
        s._Construct(self.root.lsib)
        return s
    
    def GetRTree(self):
        if(self.root.rsib==None):
            return None
        s=LinkBiTree()
        s._Construct(self.root.rsib)
        return s

    def SetLTree(self, lt):
        if(type(lt) is LinkBiTree):
            self.root.lsib=lt.root
            self.root.lsib.par=self.root
        pass
    
    def SetRTree(self, rt):
        if(type(rt) is LinkBiTree):
            self.root.rsib=rt.root
            self.root.rsib.par=self.root
        pass
    
    def isEmpty(self):
        return self.root.data==None
    
    def Depth(self):
        maxDepth=0
        if(self.isEmpty()):
            return 0
        else:
            d=1
        p=self.root
        while(True):
            if(p.lsib==None):
                if(p.rsib!=None):
                    p=p.rsib
                    d+=1
                    maxDepth=d if(d>maxDepth) else maxDepth
                else:
                    while(not p is self.root):
                        if(p==p.par.lsib and p.par.rsib!=None):
                            p=p.par.rsib
                            break
                        else:#(p==p.par.rsib)
                            p=p.par
                            d-=1
                    if(p is self.root):
                        break
            else:
                p=p.lsib
                d+=1
                maxDepth=d if(d>maxDepth) else maxDepth
        return maxDepth
    
    def Depth_recursive(self):
        return max(
            self.GetLTree().Depth_recursive() if(not self.root.lsib is None) else 0,
            self.GetRTree().Depth_recursive() if(not self.root.rsib is None) else 0
            )+1
    
    def PreOrderTravel(self, func):
        p=self.root
        yield func(p)
        while(True):
            if(p.lsib==None):
                if(p.rsib!=None):
                    p=p.rsib
                else:
                    while(not p is self.root):
                        if(p==p.par.lsib and p.par.rsib!=None):
                            p=p.par.rsib
                            break
                        else:#(p==p.par.rsib)
                            p=p.par
                    if(p is self.root):
                        return
            else:
                p=p.lsib
            yield func(p)
        pass
    
    def toPreOrderExpr(self):
        s=[]
        p=self.root
        s.append(p.data)
        while(True):
            if(p.lsib==None):
                s.append("#")
                if(p.rsib!=None):
                    p=p.rsib
                else:
                    s.append("#")
                    while(not p is self.root):
                        if(p==p.par.lsib and p.par.rsib!=None):
                            p=p.par.rsib
                            break
                        else:
                            if(p.par.rsib==None):
                                s.append("#")
                            p=p.par
                    if(p is self.root):
                        break
            else:
                p=p.lsib
            s.append(p.data)
        return s
    
    def InOrderTravel(self, func):
        p=self.root
        target=self.root
        while(target.rsib!=None):
            target=target.rsib
        while(p.lsib!=None):
            p=p.lsib
        yield func(p)
        while(True):
            if(p.rsib!=None):
                p=p.rsib
                while(p.lsib!=None):
                    p=p.lsib
            else:
                while(not p is self.root):
                    if(p.par.lsib==p):
                        p=p.par
                        yield func(p)
                        if(p==target):
                            return
                        if(p.rsib!=None):
                            p=p.rsib
                            while(p.lsib!=None):
                                p=p.lsib
                            break
                    else:
                        p=p.par
            yield func(p)
        pass
    
    def PostOrderTravel(self, func):
        p=self.root
        while(p.lsib!=None):
            p=p.lsib
        yield func(p)
        while(True):
            if(p.rsib!=None):
                while(p.lsib==None and p.rsib!=None):
                    p=p.rsib
                while(p.lsib!=None):
                    p=p.lsib
            else:
                while(not p is self.root):
                    if(p!=p.par.rsib and p.par.rsib!=None):
                        p=p.par.rsib
                        while(p.lsib==None and p.rsib!=None):
                            p=p.rsib
                        while(p.lsib!=None):
                            p=p.lsib
                        break
                    else:
                        p=p.par
                        yield func(p)
                if(p is self.root):
                    return
            yield func(p)
        pass
    
    def PreOrderTravel_Stack(self, func):
        s=Stack()
        p=self
        while(not(p is None and s.isEmpty())):
            if(p is None):
                p=s.Pop()
                continue
            yield func(p.root)
            s.Push(p.GetRTree())
            p=p.GetLTree()
        pass
    
    def InOrderTravel_Stack(self, func):
        s=Stack()
        p=self
        while(not p is None):
            s.Push(p)
            p=p.GetLTree()
        while(not p is None or not s.isEmpty()):
            if(p is None):
                p=s.Pop()
                continue
            yield func(p.root)
            p=p.GetRTree()
            while(not p is None):
                s.Push(p)
                p=p.GetLTree()
        pass
                
    def PostOrderTravel_Stack(self, func):
        s=Stack()
        p=self
        while(not p is None):
            s.Push(p)
            p=p.GetLTree()
        while(not p is None or not s.isEmpty()):
            if(p is None):
                p=s.Pop()
                continue
            if(p.GetRTree() is None):
                yield func(p.root)
                p=None
            else:
                s.Push(p.GetHeadTree())
                p=p.GetRTree()
                while(not p is None):
                    s.Push(p)
                    p=p.GetLTree()
        pass
                    
    def PreOrderTravel_Recursive(self, func):
        yield func(self.root)
        if(not self.GetLTree() is None):
            for i in self.GetLTree().PreOrderTravel_Recursive(func):
                yield i
        if(not self.GetRTree() is None):
            for i in self.GetRTree().PreOrderTravel_Recursive(func):
                yield i
        pass
    
    def InOrderTravel_Recursive(self, func):
        if(not self.GetLTree() is None):
            for i in self.GetLTree().InOrderTravel_Recursive(func):
                yield i
        yield func(self.root)
        if(not self.GetRTree() is None):
            for i in self.GetRTree().InOrderTravel_Recursive(func):
                yield i
        pass

    def PostOrderTravel_Recursive(self, func):
        if(not self.GetLTree() is None):
            for i in self.GetLTree().PostOrderTravel_Recursive(func):
                yield i
        if(not self.GetRTree() is None):
            for i in self.GetRTree().PostOrderTravel_Recursive(func):
                yield i
        yield func(self.root)
        pass
    
class ListBiTree:
#该类：广义表实现(类Scheme)
#没有实际价值
    def __init__(self, data=[None, None, None]):
        if(type(data) is list):
            self.data=data
        else:
            self.data=[data, None, None]
        pass
    def Reset(self, data):
        self.__init__(data)
    def GetRoot(self):
        return self.data[0]
    def GetLTree(self):
        return ListBiTree(self.data[1])
        pass
    def GetRTree(self):
        return ListBiTree(self.data[2])
        pass
    def SetRoot(self, data):
        self.data[0]=data
    def SetLTree(self, lt):
        if(type(lt) is list):
            self.data[1]=lt
        elif(type(lt) is ListBiTree):
            self.data[1]=lt.data
        pass
    def SetRTree(self, rt):
        if(type(rt) is list):
            self.data[2]=rt
        elif(type(lt) is ListBiTree):
            self.data[2]=rt.data
        pass
    def isEmpty(self):
        return self.data[0] is None
        pass

    
