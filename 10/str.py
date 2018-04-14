def Ret_(short, long):
    p=[0, 0]
    s=[[0]*(len(short)+2)]
    #s=[[0]*(len(long)+1)]*(len(short)+1)#SHALLOW COPY
    for i in range(1, len(short)+1):
        s.append([0])
        for j in range(1, len(long)+1):
            if(short[i-1]==long[j-1]):
                s[i].append(s[i-1][j-1]+1)
                if(s[i][j]>s[p[0]][p[1]]):
                    p[0], p[1]=i, j
            else:
                s[i].append(0)
    return short[p[0]-s[p[0]][p[1]]:p[0]]

def Ret(short, long):
    x=Ret_(short, long)
    y=Ret_(short[::-1], long)
    return x if len(x)>len(y) else y

n=int(input())
while(n>0):
    n-=1
    h=[]
    m=int(input())
    for i in range(m):
        h.append(str(input()))
    h.sort(key=lambda x:len(x))
    while(len(h)>1):
        h.append(Ret(h.pop(), h.pop()))
        print(h[len(h)-1])
    print(len(h[0]))
