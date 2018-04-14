from Classes import *

if(Version==1.0):

    class Dict:
        def __init__(self, Length):
            self.Length=Length
            self.data=list(LCList() for i in list(range(self.Length)))
        def BKDRHash(self, s):
            seed=31
            ret=0
            for i in s:
                ret+=(ret*seed+ord(i)-ord('a'))
            return ret%self.Length
        def Insert(self, key, value):
            self.data[self.BKDRHash(key)].Append((key, value))
            pass
        def Delete(self, key):
            self.Search(key)
            k=self.data[self.BKDRHash(key)]
            if(k.isEmpty()):
                return None
            else:
                for i in k.Iterable():
                    if(i.elem[0]==key):
                        k.DeleteNode(i)
                        return i.elem[1]
                return None
        def Search(self, key):
            k=self.data[self.BKDRHash(key)]
            if(k.isEmpty()):
                return None
            else:
                for i in k.Iterable():
                    if(i.elem[0]==key):
                        return i.elem[1]
                return None
        

    l=Dict(10000)
    s, sys.stdin=sys.stdin, open("in.csv")
    print("source: in.csv")
    while(True):
        try:
            x=input()
        except(EOFError):
            break
        x=str(x).split(',')
        l.Insert(x[0], x[1])
    m=max(i.Length() for i in l.data)
    for j in range(m+1):
        print("bucket size="+str(j), sum(1 for i in l.data if i.Length()==j))
    
    
    sys.stdin=s
    while(True):
        x=str(input("word:"))
        print(l.Search(x))
