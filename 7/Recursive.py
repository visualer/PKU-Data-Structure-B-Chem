READ_FILE=True

if(READ_FILE):
    import sys
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
solution=[]

def Add(a, b):
    return [a[0]+b[0], a[1]+b[1]]

def Valid(a):
    return a[0]>=0 and a[0]<m and a[1]>=0 and a[1]<n and maze[a[0]][a[1]]!=1 and maze[a[0]][a[1]]!=2
def solve(st, ed):
    maze[st[0]][st[1]]=2
    if(st==ed):
        solution.append(st)
        return 1
    else:
        for i in range(4):
            t=Add(direction[i], st)
            if(not Valid(t)):
                continue
            if(solve(t, ed)==1):
                solution.append(st)
                return 1
        return 0

st, ed=input("start:" if not READ_FILE else "").split(), input("end:" if not READ_FILE else "").split()
st[0], st[1]=int(st[1]), int(st[0])
ed[0], ed[1]=int(ed[1]), int(ed[0])

if(not solve(st, ed)):
    print("not found")
else:
    for i in reversed(range(len(solution))):
        print(solution[i])
