import sys
import os
import copy
import time

class LNode:
    def __init__(self, elem, prev, next_):
        self.elem=elem
        self.next=next_
        self.prev=prev
        pass

class LCList():
    def __init__(self):
        self._head=None
        self._length=0
        pass
    def Length(self):
        return self._length
    def isEmpty(self):
        return self._length==0
    def isValid(self):
        return not(self._length==0 or self._length==1)
    def Iterable(self):
        it=self._head
        for i in range(self._length):
            yield it.elem
            it=it.next
        pass

    def Seek(self, pos):
        it=self._head
        if(pos>=self._length/2):
            for i in range(self._length-pos):
                it=it.prev
        else:
            for i in range(pos):
                it=it.next
        return it
        
    def __getitem__(self, pos):
        return self.Seek(pos).elem
    def __setitem__(self, pos, elem):
        self.Seek(pos).elem=elem
        pass
    
    def Append(self, elem):
        if(self._length==0):
            s=LNode(elem, None, None)
            self._head, s.prev, s.next=s, s, s
        else:
            s=LNode(elem, self._head.prev, self._head)
            self._head.prev.next, self._head.prev=s, s
        self._length+=1
        pass
    
    def Prepend(self, elem):
        self.Append(elem)
        self._head=self._head.prev
        pass

    def InsertAfter(self, elem, pos):
        if(self._length==0 or self._length==1 or pos==self._length-1):
            self.Append(elem)
        else:
            it=self.Seek(pos)
            s=LNode(elem, it, it.next)
            it.next.prev, it.next=s, s
            self._length+=1
        pass
    
    def InsertBefore(self, elem, pos):
        if(self._length==0 or self._length==1 or pos==0):
            self.Prepend(elem)
        else:
            self.InsertAfter(elem, pos-1)
        pass
    
    def Delete(self, pos):
        if(self._length==1):
            e=self._head.elem
            self._head=None
            self._length-=1
            return e
        else:
            it=self.Seek(pos)
            if(it is self._head):
                #print("Deleting self._head while self._length>1, self._head moving to next domain")
                self._head=self._head.next
            it.prev.next, it.next.prev=it.next, it.prev
            self._length-=1
            return it.elem
    pass

class Stack(LCList):
    def __init__(self):
        super(Stack, self).__init__()
        pass
    def Push(self, elem):
        super(Stack, self).Append(elem)
        pass
    def Pop(self):
        return super(Stack, self).Delete(self._length-1)
    def Top(self):
        return self._head.prev.elem
    pass

class BTNode:
    def __init__(self, data, lsib, rsib, par):
        self.data=data
        self.lsib=lsib
        self.rsib=rsib
        self.par=par
        pass

class LinkBiTree:
    def __init__(self, data=None):
        self.root=BTNode(data, None, None, None)
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
        s.root=self.root.rsib
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
        return max(
            self.GetLTree().Depth_recursive() if(not self.root.lsib is None) else 0,
            self.GetRTree().Depth_recursive() if(not self.root.rsib is None) else 0
            )+1
    
    def PreOrderTravel(self, func):
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
    
    def InOrderTravel(self, func):
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
                
    def PostOrderTravel(self, func):
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
                    
class Heap(LinkBiTree):
    def __init__(self, cmp_priority):
        super(Heap, self).__init__()
        self.elem=0
        self.tail=self.root
        self.cmp=lambda x, y:cmp_priority(x.data, y.data) if (not(x is None or y is None)) else None if(x is None and y is None) else (y is None)
        pass
    
    def isEmpty(self):
        return self.elem==0
    
    def Insert(self, data):#O(log n)
        if(self.isEmpty()):
            self.root.data=data
        p=self.root
        s=[]
        index=self.elem
        while(index!=0):
            s.append((index+1)%2)
            index=(index-1)//2
        for i in s[0:len(s)-2:-1]:
            p=p.rsib if(i==1) else p.lsib
        if(s[len(s)-1]==1):
            p.rsib=BTNode(data, None, None, p)
        else:
            p.lsib=BTNode(data, None, None, p)
        self.elem+=1
        self.Sift_Up()
        pass
    
    def Sift_Down(self):
        p=self.root
        x=self.cmp(p.lsib, p.rsib)
        while(True):
            if(x is True and self.cmp(p.lsib, p)):
                p.lsib.data, p.data=p.data, p.lsib.data
            elif(x is False and self.cmp(p.rsib, p)):
                p.rsib.data, p.data=p.data, p.rsib.data
            else:
                break 
        pass
    
    def Sift_Up(self):
        p=self.tail
        while(not p.par is None and self.cmp(p, p.par) is True):
            p.data, p.par.data=p.par.data, p.data
            p=p.par
        pass
    
    def Delete(self):
        self.elem-=1
        if(self.elem==0):
            self.root.data=None
            return
        self.root.data=self.tail.data
        index=self.elem-1
        if(index==0):
            p=self.root
        else:
            s=[]
            while(index!=0):
                s.append((index+1)%2)
                index=(index-1)//2
            for i in s[::-1]:
                p=p.rsib if(i==1) else p.lsib
        if(self.tail.par.lsib is self.tail):
            self.tail.par.lsib=None
        else:
            self.tail.par.rsib=None
        self.tail=p
        self.Sift_Down()
        pass

    def Pop(self):
        x=self.GetTop()
        self.Delete()
        return x
    
    def ElemCount(self):
        return self.elem

    def GetTop(self):
        return self.root.data


class AdjMatrixGraph:
    def __init__(self, matrix, elem, nullelem=0):
        #skip checking
        self.matrix=copy.deepcopy(matrix)
        self.null=nullelem
        self.index=elem
        pass
    def Length(self):
        return len(self.matrix)
    def AddVertex(self, elem, index):
        self.index.append(elem)
        for i in range(self.Length()):
            self.matrix[i].append(self.null)
        self.matrix.append([self.null]*self.Length()#No need to deepcopy
        self.index.append(index)
        pass
    def DeleteVertex(self, num):
        for i in range(self.Length()):
            del self.matrix[i][num]
        del self.matrix[num]
        del self.index[num]
        pass
    def GetEdge(self, v1, v2=None):
        return self.matrix[v1][v2] if(not v2 is None) else list(
            (i, self.matrix[v1][i]) for i in range(self.Length()) if(self.matrix[v1][i]!=self.null)
            )
    def SetEdge(self, v1, v2, elem):
        self.matrix[v1][v2]=elem
        pass
    def Degree(self, v):#(out, in)
        return (sum((i!=self.null) for i in self.matrix[v]), sum((i[v]!=self.null) for i in self.matrix))
        pass
    def Visualize(self, filename="out"):
        f=sys.stdout
        sys.stdout=open(filename, "w")
        print("digraph G{ \n rankdir = LR \n node[shape=record, height=.1]")
        for i in range(self.Length()):
            print("node"+str(i), "[label=\"{<f0>#", i, "|<f1>", self.index[i], "}\"]")
        for i in range(self.Length()):
            for j in range(self.Length()):
                if(self.matrix[i][j]!=self.null):
                    print("node"+str(i), "->", "node"+str(j)+" [label=\"", self.matrix[i][j], "\"]")
        print("}")
        sys.stdout.flush()
        sys.stdout=f
        if(os.path.isfile(filename+".jpg")):
            os.remove(filename+".jpg")
        os.popen("dot -Tjpg -O "+filename)
        time.sleep(0.3)
        os.remove(filename)
        os.popen(filename+".jpg")
        pass
    def DFTFrom(self, v, func):
        s=Stack()
        p=v
        visited=[0]*self.Length()
        while(True):
            if(visited[p]==0):
                yield func(self.index[p])
                visited[p]=1
            for (i, t) in self.GetEdge(p):
                if(visited[i]==0):
                    s.Push(i)
            if(s.isEmpty()):
                if(all(visited)):
                    break
                elif(p!=v):
                    for i in range(self.Length()):
                        if(visited[i]==0):
                            p=i
                            break
                    continue
            p=s.Pop()
        pass
    
    def BFTFrom(self, v, func):
        s=[]
        p=v
        visited=[0]*self.Length()
        while(True):
            if(visited[p]==0):
                yield func(self.index[p])
                visited[p]=1
            if(len(s)==0):
                if(all(visited)):
                    break
                elif(p!=v):
                    for i in range(self.Length():
                        if(visited[i]==0):
                            p=i
                            break
                    continue
            for (i, t) in self.GetEdge(p):
                if(visited[i]==0):
                    s.append(i)
            p=s[0]
            del s[0]
    pass
