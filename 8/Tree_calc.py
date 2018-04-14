def priority(s):
    return 2 if(s=="+" or s=="-") else 3 if(s=="*" or s=="/") else 1

Operand="+-*/()"

def _Exp2Tree(lst, start=0, prio=0):
#递归生成树
    temp=[None, None, None]
    i=start
    while(i<len(lst)):
        if(lst[i]=="("):
            z=_Exp2Tree(lst, i+1)
            i=z[1]+1
            lst[i]=z[0]
            continue
        elif(i==len(lst)-1 or lst[i+1]==")"):
            if(temp[0] is None):
                return (lst[i], i)
            temp[2]=lst[i]
            return (temp, i)
        else:#next is operand
            if(temp[0] is None):
                temp[1]=lst[i]
                temp[0]=lst[i+1]
                i+=2
            elif(priority(temp[0])>=priority(lst[i+1])):#> error
                temp[2]=lst[i]
                if(priority(lst[i+1])<=prio):
                    return (temp, i)
                temp=[lst[i+1], temp, None]
                i+=2
            else:
                z=_Exp2Tree(lst, i, priority(temp[0]))
                i=z[1]
                lst[i]=z[0]
                continue
    raise Exception

def Exp2Tree(lst):
    return _Exp2Tree(lst)[0]

def Str2List(Str, type_):
    num="0123456789."
    ie=list()
    p=str()
    for i in Str:
        if(i in num):
            p=p+i
        else:
            if(p!=""):
                ie.append(type_(p))
                p=""
            ie.append(i)
    if(p!=""):
        ie.append(type_(p))
    return ie

def evaluate(x):
#递归计算树
    if(type(x) is float):
        return x
    if(x[0]=="+"):
        return evaluate(x[1])+evaluate(x[2])
    if(x[0]=="-"):
        return evaluate(x[1])-evaluate(x[2])
    if(x[0]=="*"):
        return evaluate(x[1])*evaluate(x[2])
    if(x[0]=="/"):
        return evaluate(x[1])/evaluate(x[2])

#expr=input()
expr="6-(38-345/(45+89*78)-6)*(8*9+3)*9-9"
s=Exp2Tree(Str2List(str(expr), float))
#print(s)
print(evaluate(s))
