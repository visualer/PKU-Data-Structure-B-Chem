        
########Well it is just useless to implement this for python supports list.

class SList: #Sequence List 
    def __init__(self, maxsize):
        if(not type(maxsize)==int):
            raise TypeError
        elif(not maxsize>=0):
            raise ValueError
        else:
            self.maxsize=maxsize
            self.data=list(range(maxsize))
            self.it=-1
        pass
    def __del__(self):
        del self.maxsize
        del self.it
        del self.data
        pass
    def isEmpty(self):
        return self.it==-1
    def isFull(self):
        return self.it==self.maxsize-1
    def _posValid(self, pos):
        if(not (pos in range(self.it+1))):
            return False
        else:
            return True
        pass
    def get(self, pos): #__getitem__ is better
        if(not self._posValid(pos)):
           raise IndexError
        else:
           return self.data[pos]
        pass
    def __getitem__(self, pos):
        return self.get(pos)
    def set(self, pos, val):
        if(not self._posValid(pos)):
           raise IndexError
        else:
            self.data[pos]=val
        pass
    def __setitem__(self, pos, val):
        self.set(self, pos, val)
        pass
    #operands of classical queue
    def append(self, elem):
        if(self.isFull()):
            raise OverflowError
        else:
            self.it=self.it+1
            self.data[self.it]=elem
    def pop(self):
        if(self.isEmpty()):
            raise OverflowError
