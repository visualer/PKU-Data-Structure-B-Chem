import sys
sys.path.append("lib")
from Heap import *

s=Heap(lambda x,y:x>y)
for i in str(input()).split():
    s.Insert(int(i))
while(not s.isEmpty()):
    print(s.GetTop(), end=' ')
    s.Delete()
