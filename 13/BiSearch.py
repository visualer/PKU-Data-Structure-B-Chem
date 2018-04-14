import random

s=[]
for i in range(100):
    s.append((random.randint(0, 65535), i))
key=lambda x:x[0]
s.sort(key=key)
print(s)
while(True):
    n=int(input("find:"))
    x, y=0, 99
    t=-1
    while(True):
        if(key(s[x])==n):
            t=s[x][1]
            break
        elif(y-x==1):
            break
        else:
            p=(x+y)//2
            if(n<key(s[p])):
                y=p
            else:
                x=p
    print(t)
            
