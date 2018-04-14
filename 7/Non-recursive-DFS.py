READ_FILE=True

import sys

sys.path.append("Lib")
from Stack import *

if(READ_FILE):
    sys.stdin=open('in.txt', 'r')
    print("read from file")

n, m=int(input("length:" if not READ_FILE else "")), int(input("width:" if not READ_FILE else ""))

if(not READ_FILE):
    print("input matrix:")
maze=[]
for i in range(m):
    s=input().split()
    for i in range(n):
        s[i]=int(s[i])
    maze.append(s)

direction=[[0, -1], [0, 1], [1, 0], [-1, 0]]
sol=Stack()

def Add(a, b):
    return [a[0]+b[0], a[1]+b[1]]
def Valid(a):
    return a[0]>=0 and a[0]<m and a[1]>=0 and a[1]<n and maze[a[0]][a[1]]!=1 and maze[a[0]][a[1]]!=2

def solve(st, ed):
    sol.Push(st)
    maze[st[0]][st[1]]=2
    while(not sol.isEmpty()):
        flag=True
        if(sol.Top()==ed):
            return True
        for i in range(4):
            t=Add(direction[i], sol.Top())
            if(Valid(t)):
                sol.Push(t)
                maze[t[0]][t[1]]=2
                flag=False
                break
        if(flag):
            sol.Pop()
    return False

st, ed=input("start:" if not READ_FILE else "").split(), input("end:" if not READ_FILE else "").split()
st[0], st[1]=int(st[1]), int(st[0])
ed[0], ed[1]=int(ed[1]), int(ed[0])

if(not solve(st, ed)):
    print("not found")
else:
    for i in sol.Iterable():
        print(i)
