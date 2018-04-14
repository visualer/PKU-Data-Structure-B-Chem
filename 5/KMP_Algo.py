'''KMP Algorithm. I'm bored with simple pattern matching,
so I made this KMP program instead.
'''
p, t=str(input("pattern:")), str(input("target:"))
s=range(len(p))
pnext=[-1]*len(p)
#generate pnext

chain=-1
for i in filter(lambda x:x>0, s):
    if(p[chain+1]!=p[i]):
        pnext[i]=chain+1
        chain=0 if (p[i]==p[0]) else -1
    else:
        chain+=1
        pnext[i]=-1 if(p[i]==p[0]) else 0

i=0
flag=True
while(i<len(t)-len(p)):
    flag=True
    for j in range(len(p)):
        if(t[i+j]!=p[j]):
            flag=False
            i+=j-pnext[j]
            break
    if(flag):
        print(t[:i-1], t[i:i+len(p)-1], t[i+len(p):])
        break
    pass

if(not flag):
    print("not found")
