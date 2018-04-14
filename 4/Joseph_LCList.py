from LCList import *
n, m=int(input("total:")), int(input("step:"))
print()
x=LCList()
for i in range(n):
    x.Append(i+1)
while(x.Length()!=1):
    x.MovePointer(m-1)
    e=x.Delete()
    #print("position ", e, " out")
print("position ", x.Delete(),
      " remains")
