n, m=int(input("total:")), int(input("steps:")) 
x=list(range(1, n+1))
pos=0
for i in range(n, 1, -1):
    pos=(pos+m-1)%i
    print("position ", x.pop(pos), " out")
print("position ", x.pop(0), "remains")
