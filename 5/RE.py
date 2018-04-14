p, t=str(input("pattern:")), str(input("target:"))

def match(pt, tg, pos):
    j=pos-1
    i=0
    while(i in range(len(pt))):
        if(pt[i]=='$'):
            return 0 if(j!=len(tg)-1) else 1
        if(j==len(tg)-1):
            if(pt[i]!='*'):
                return 0
            else:
                i+=1
                continue
        j+=1
        if(pt[i]=='.'):
            i+=1
            continue
        elif(pt[i]=='*'):#warning: "a*aa" but "a**" or "a.*" is matched with "aaa" 
            count=0
            count1=0
            while(i+1+count<len(pt) and pt[i+1+count]==pt[i-1]):
                count+=1
            while(j+count1<len(tg) and tg[j+count1]==tg[j-1]):
                count1+=1
            if(count>count1):
                return 0
            else:
                i+=count+1
                j+=count1-1
                continue
        elif(pt[i]!=tg[j]):
            return 0
        else:
            i+=1
        pass
    return 1


if(p[0]=='^'):
    print(match(p[1:], t, 0)-1)
else:
    flag=False
    for i in range(len(t)):
        if(match(p, t, i)==1):
            print(i)
            flag=True
            break
    if(not flag):
        print(-1)

