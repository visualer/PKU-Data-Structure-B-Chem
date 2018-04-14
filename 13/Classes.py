import sys
import os
import copy
import time

Version=1.0

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
            yield it
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
    
    def DeleteNode(self, it):
        if(it is self._head):
                #print("Deleting self._head while self._length>1, self._head moving to next domain")
                self._head=self._head.next
        it.prev.next, it.next.prev=it.next, it.prev
        pass
        
    def Delete(self, pos):
        if(self._length==1):
            e=self._head.elem
            self._head=None
            self._length-=1
            return e
        else:
            it=self.Seek(pos)
            self.DeleteNode(it)
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
    def _Construct(self, root):
        self.root=root
        pass

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

class Heap(LinkBiTree):#用链接二叉树实现的堆
    def __init__(self, cmp_priority):
        super(Heap, self).__init__()
        self.elem=0
        self.tail=self.root
        self.cmp=lambda x, y:cmp_priority(x.data, y.data) if (not(x is None or y is None)) else None if(x is None and y is None) else (y is None)
        pass

    def isEmpty(self):
        return self.elem==0

    def Visualize(self, filename=".tree"):
        s=[self]
        l=[]
        while(len(s)!=0):
            p=s[0]
            del s[0]
            l.append(p.root.data)
            x=p.GetLTree()
            if(x is not None):
                s.append(x)
            y=p.GetRTree()
            if(y is not None):
                s.append(y)

        #非迭代广度优先遍历

        f=sys.stdout
        sys.stdout=open(filename, "w")
        print("graph G{ \n rankdir = LR \n node[shape=record, height=.1]")
        for i in range(len(l)):
            print("node"+str(i), "[label=\"{<f0>#", i, "|<f1>", l[i], "}\"]")
        for i in range(len(l)):
            if(2*i+1<len(l)):
                print("node"+str(i), "--", "node"+str(2*i+1))
            if(2*i+2<len(l)):
                print("node"+str(i), "--", "node"+str(2*i+2))
        print("}")
        sys.stdout.flush()
        sys.stdout=f
        os.popen("dot -Tjpg -O "+filename)
        time.sleep(1)
        os.remove(filename)
        os.popen(filename+".jpg")
        pass

    #堆的二叉树结构可视化，用于追迹sift过程。如果在二叉树父类中也引入元素计数器self.elem，也可做成Tree Writer一样的东西。

    def Insert(self, data):#O(log n)
        if(self.isEmpty()):
            self.root.data=data
            self.elem+=1
            return
        p=self.root
        s=[]
        index=self.elem
        while(index!=0):
            s.append((index+1)%2)
            index=(index-1)//2
        if(len(s)>1):#Changed
            for i in s[1:][::-1]:
                p=p.rsib if(i==1) else p.lsib
        #追踪新尾巴结点的父节点以创造新尾巴
        if(s[0]==1):
            p.rsib=BTNode(data, None, None, p)
            self.tail=p.rsib
        else:
            p.lsib=BTNode(data, None, None, p)
            self.tail=p.lsib
        self.Sift_Up()
        self.elem+=1
        pass

    def Sift_Down(self):
        p=self.root
        #求您不要再犯智障错误了，求求
        while(True):
            if(self.cmp(p.lsib, p.rsib) and self.cmp(p.lsib, p)):
                p.lsib.data, p.data=p.data, p.lsib.data
                p=p.lsib
            elif(self.cmp(p.rsib, p.lsib) and self.cmp(p.rsib, p)):
                p.rsib.data, p.data=p.data, p.rsib.data
                p=p.rsib
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
        if(self.elem==1):
            self.elem-=1
            self.root.data=None
            return
        self.root.data=self.tail.data
        index=self.elem-2
        p=self.root
        s=[]
        if(index!=0):
            while(index!=0):
                s.append((index+1)%2)
                index=(index-1)//2
            for i in s[::-1]:
                p=p.rsib if(i==1) else p.lsib
        #追踪尾巴结点的前一个结点
        if(self.tail.par.lsib is self.tail):
            self.tail.par.lsib=None
        else:
            self.tail.par.rsib=None
        self.tail=p
        self.Sift_Down()
        self.elem-=1
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
    def __init__(self, matrix, elem, nullelem=0, dir_=False):
        #skip checking
        self.matrix=copy.deepcopy(matrix)
        self.null=nullelem
        self.index=elem
        self.flag=dir_
        self.dir=lambda x, y: x<y if (not dir_) else True
        pass
    def Length(self):
        return len(self.matrix)
    def AddVertex(self, elem, index):
        self.index.append(elem)
        for i in range(self.Length()):
            self.matrix[i].append(self.null)
        self.matrix.append([self.null]*self.Length())#No need to deepcopy
        self.index.append(index)
        pass
    def DeleteVertex(self, num):
        for i in range(self.Length()):
            del self.matrix[i][num]
        del self.matrix[num]
        del self.index[num]
        pass

    def GetOutEdge(self, v1):#兼容无向图，无向图会返回对应的所有边
        return list((i, self.matrix[v1][i])
                    for i in range(self.Length())
                    if(self.matrix[v1][i]!=self.null
                       and self.dir(v1, i)))+([] if(self.flag)
                                              else list((i, self.matrix[i][v1])
                                                        for i in range(self.Length())
                                                        if(self.matrix[i][v1]!=self.null
                                                           and self.dir(i, v1))))
    def Degree(self, v):#(out, in)
        a=sum((i!=self.null) for i in self.matrix[v])
        b=sum((i[v]!=self.null) for i in self.matrix)
        return (a, b) if(self.flag) else a+b

    def Visualize(self, filename=".out"):
        f=sys.stdout
        sys.stdout=open(filename, "w")
        print(("di" if(self.flag) else "")+"graph G{ \n rankdir = LR \n node[shape=record, height=.1]")
        for i in range(self.Length()):
            print("node"+str(i), "[label=\"{<f0>#", i, "|<f1>", self.index[i], "}\"]")
        for i in range(self.Length()):
            for j in range(self.Length()):
                if(self.matrix[i][j]!=self.null):
                    print("node"+str(i), "->" if(self.flag) else "--", "node"+str(j)+" [label=\"", self.matrix[i][j], "\"]")
        print("}")
        sys.stdout.flush()
        sys.stdout=f
        os.popen("dot -Tjpg -O "+filename)
        time.sleep(1)
        os.remove(filename)
        os.popen(filename+".jpg")
        os.remove(filename+".jpg")
        pass

    #利用GraphViz dot语言进行可视化，需安装GraphViz软件包并将\bin加入%PATH%

    def DFTFrom(self, v, func):
        s=Stack()
        p=v
        visited=[0]*self.Length()
        while(True):
            if(visited[p]==0):
                yield func(self.index[p])
                visited[p]=1
            for (i, t) in self.GetOutEdge(p):
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
                    for i in range(self.Length()):
                        if(visited[i]==0):
                            p=i
                            break
                    continue
            for (i, t) in self.GetOutEdge(p):
                if(visited[i]==0):
                    s.append(i)
            p=s[0]
            del s[0]
        pass

    #s.isEmpty() is not required for connected graph

    def DFTList(self, v):
        span_forest=[-1]*self.Length()
        s=Stack()
        p=(v, -1)
        span_forest[v]=None
        while(True):
            if(span_forest[p[0]]==-1):
                span_forest[p[0]]=(p[1], self.matrix[p[1]][p[0]])
            for (i, t) in self.GetOutEdge(p[0]):
                if(span_forest[i]==-1):
                    s.Push((i, p[0]))
            if(all((i!=-1) for i in span_forest)):
                break
            p=s.Pop()
        return span_forest

    #返回span_forest的算法

    def Kruskal(self):#贪心+并查集，不考虑有向图的联通
        tag=[-1]*self.Length()
        mat=list([self.null]*self.Length() for i in range(self.Length()))
        e=[]
        for i in range(self.Length()):
            for j in self.GetOutEdge(i):
                e.append((j[1], i, j[0]))
        e.sort(key=lambda x:x[0])
        for x in e:
            if(tag[x[1]]!=tag[x[2]] or tag[x[1]]==-1):
                mat[x[1]][x[2]]=x[0]
                c=[tag[x[1]], tag[x[2]]]
                tag[x[1]], tag[x[2]]=x[1], x[1]
                for i in range(len(tag)):
                    if((tag[i] in c) and tag[i]!=-1):
                        tag[i]=x[1]
        return AdjMatrixGraph(mat, self.index, self.null, self.flag)
    #返回相应的图，便于可视化，也可以更改为返回前接表

    def Prim(self):#贪心+优先队列，考虑有向图问题
        h=Heap(lambda x, y:x[0]<y[0])
        tag=[True]+[False]*(self.Length()-1)
        mat=list([self.null]*self.Length() for i in range(self.Length()))
        for i in self.GetOutEdge(0):
            h.Insert((i[1], 0, i[0]))
        while(not h.isEmpty()):
            x=h.Pop()
            for i in [1 if(self.flag) else 2, 2]:
                if(not tag[x[i]]):
                    tag[x[i]]=True
                    mat[x[1]][x[2]]=x[0]
                    for j in self.GetOutEdge(x[i]):
                        if(not tag[j[0]]):
                            h.Insert((j[1], x[i], j[0]) if(self.dir(x[i], j[0])) else (j[1], j[0], x[i]))
                    continue
        if(not all(tag)):
            return None
        else:
            return AdjMatrixGraph(mat, self.index, self.null, self.flag)
        #加入第一个顶点的所有边，然后pop权值最小的，计入结果，顶点也mark。将那个顶点相关的所有边加入堆。重复的情况只可能在对面顶点已经被mark的情况
        #才会出现，所以1)如果这条边的另一个顶点已经被mark，那就弃了这条边。2)如果pop出来的边两个顶点都已经被mark，那就弃了这条边

    def Dijkstra(self, v0):
        dist, dist[v0]=[False]*self.Length(), (0, -1) #(distance, previous_node)
        h=Heap(lambda x, y:x[0]<y[0])
        for i in self.GetOutEdge(v0):
            h.Insert((i[1], v0, i[0]))
        while(not h.isEmpty()):
            x=h.Pop()
            if(not dist[x[2]]):
                dist[x[2]]=(x[0], x[1])
                for i in self.GetOutEdge(x[2]):
                    h.Insert((i[1]+x[0], x[2], i[0]))
        return dist
        #有向图也好，无向图也好，因为这里没有返回图类而是返回了前接表，所以一定是x[2]在前，i[0]在后。如果是无向图，需要可视化，
        #那么判断一下self.dir(x[2], i[0])，再决定顺序就好。

