import sys;
sys.path.append("Lib")
from IE2PE import *
from PE_Eval import *

def Str2List(Str):
    num="0123456789"
    ie=list()
    p=str()
    for i in Str:
        if(i in num):
            p=p+i
        else:
            if(p!=""):
                ie.append(p)
                p=""
            ie.append(i)
    if(p!=""):
        ie.append(p)
    return ie

while(True):
    s=str(input("IE:"))
    PE_Eval(IE2PE(Str2List(s))).print()
    print()
