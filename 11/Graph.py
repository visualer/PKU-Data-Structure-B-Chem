from Classes import *
import sys
import os
import copy
import time
class AdjMatrixGraph:
    def __init__(self, matrix, elem, nullelem=0):
        for i in range(len(matrix)):
            if(len(matrix[i])!=len(matrix)):
                raise Exception
        if(not (type(elem) is list and len(elem)==len(matrix))):
            raise Exception
        self.matrix=copy.deepcopy(matrix)
        self.null=nullelem
        self.index=elem
        pass
    def Normalize(self):
        for i in range(len(matrix)):
            matrix[i][i]=self.null
    def isEmpty(self):
        return self.matrix is None
    def GetVertexNum(self):
        return len(self.matrix)
    def GetVertexData(self):
        return self.index
    def AddVertex(self, elem):
        self.index.append(elem)
        for i in range(len(self.matrix)):
            self.matrix[i].append(self.null)
        self.matrix.append([self.null]*len(self.matrix[0]))#No need to deepcopy
        pass
    def DeleteVertex(self, num):
        for i in range(len(self.matrix)):
            del self.matrix[i][num]
        del self.matrix[num]
        pass
    def GetEdge(self, v1, v2=None):
        return self.matrix[v1][v2] if(not v2 is None) else list(
            (i, self.matrix[v1][i]) for i in range(self.GetVertexNum()) if(self.matrix[v1][i]!=self.null)
            )
    def SetEdge(self, v1, v2, elem):
        self.matrix[v1][v2]=elem
        pass
    def Degree(self, v):#(out, in)
        return (sum((i!=self.null) for i in self.matrix[v]), sum((i[v]!=self.null) for i in self.matrix))
        pass
    def Visualize(self, filename="out"):
        #generate GraphViz dot language
        #requires GraphViz installed and set installpath\bin to %Path%
        f=sys.stdout
        sys.stdout=open(filename, "w")
        print("digraph G{")
        print("rankdir = LR")
        print("node[shape=record, height=.1]")
        for i in range(len(self.index)):
            print("node"+str(i), "[label=\"{<f0>#", i, "|<f1>", self.index[i], "}\"]")
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if(self.matrix[i][j]!=self.null):
                    #print("node"+str(i)+":<f0>", "->", "node"+str(j)+":<f0> [label=\"", self.matrix[i][j], "\"]")
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
        visited=[0]*self.GetVertexNum()
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
                    #there're 2 conditions may cause not all visited and stack empty:
                    #1st is p==v, for s is empty when initializing
                    #2nd is the subgraph is fully travelled, and we need to travel a new subgraph
                    #and here we pick the smallest possible number of vertex  
                    for i in range(self.GetVertexNum()):
                        if(visited[i]==0):
                            p=i
                            break
                    continue
            p=s.Pop()
        pass
    
    def BFTFrom(self, v, func):
        s=[]
        p=v
        visited=[0]*self.GetVertexNum()
        while(True):
            if(visited[p]==0):
                yield func(self.index[p])
                visited[p]=1
            if(len(s)==0):
                if(all(visited)):
                    break
                elif(p!=v):
                    for i in range(self.GetVertexNum()):
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


class AdjListGraph:
    #unimplemented
    pass

#TEST

sys.stdin=open("in.txt")
n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(int(i) for i in str(input()).split()))
lst=str(input()).split()
s=AdjMatrixGraph(matrix, lst)
s.Visualize()
for i in s.BFTFrom(0, lambda x:x):
    print(i)
