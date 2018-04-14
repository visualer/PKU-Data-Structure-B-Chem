from Stack import *

ext_opr="+-*/()"
paren="()"
def priority(s):
    return 2 if(s=="+" or s=="-") else 3 if(s=="*" or s=="/") else 1
def IE2PE(ie):
    pe=list()
    token=Stack()
    if(type(ie)!=list):
        raise TypeError
    for i in ie:
        if(i in ext_opr):
            if(token.isEmpty() or (priority(token.Top())<=priority(i) and i!=")") or i=="("):
                token.Push(i)
            else: #(i==")" or priority(token.Top())>priority(i)) and i!="("
                while(not token.isEmpty() and priority(token.Top())>priority(i)):
                    c=token.Pop()
                    if(not c in paren):
                        pe.append(c)
                if(i==")"):
                    c=token.Pop()
                else:
                    token.Push(i)
        else:
            pe.append(i)
    
    while(not token.isEmpty()):
        c=token.Pop()
        pe.append(c)#c cannot be paren
    return pe
