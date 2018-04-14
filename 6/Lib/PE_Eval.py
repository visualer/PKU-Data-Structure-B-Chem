from Stack import *
from Rational import *

opr="+-*/"

def PE_Eval(expr):
    if(type(expr)!=list):
        raise TypeError
    s=Stack()
    for i in expr:
        if(not i in opr):
            s.Push(Rational(int(i)))
        else:
            b=s.Pop()
            a=s.Pop()
            s.Push(a+b if(i=="+") else a-b if(i=="-") else a*b if(i=="*") else a/b)
    return s.Pop()
            
