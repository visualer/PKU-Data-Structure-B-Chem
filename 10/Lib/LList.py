class UnderflowError(BaseException):
    pass

class LNode: #LDNode
    def __init__(self, elem, prev, next_):
        self.elem=elem
        self.next=next_
        self.prev=prev
        pass
    pass

class LList: #LDList
    
    def __init__(self):
        self._head=None
        self._tail=None
        self._length=0
        pass

    def Length(self):
        return self._length
    def isEmpty(self):
        return self._length==0
    
    def Iterable(self): #Generator Function
        it=self._head
        while(it!=None):
            yield it.elem
            it=it.next
        pass
    def Filter(self, filter_): #just for simplifying
        return filter(filter_, self.Iterable())
    def Print(self):
        print("[", end=' ')
        for i in self.Iterable():
            print(i, end=' ')
        print("]")
        pass



    
    def Seek(self, pos):
        if(pos<0 or pos>=self._length):
            raise IndexError
        elif(pos>=self._length/2):
            it=self._tail
            currpos=self._length-1
            while(currpos!=pos):
                it=it.prev
                currpos-=1
            return it
        else:
            it=self._head
            currpos=0
            while(currpos!=pos):
                it=it.next
                currpos+=1
            return it
        pass
        
    
    
    #It is useless to modify the address of iterator. Modify the member instead.

    ###Operations 
    
    def Prepend(self, elem):
        if(self.isEmpty()):
            self._head=LNode(elem, None, None)
            self._tail=self._head
        else:
            self._head=LNode(elem, None, self._head)
            self._head.next.prev=self._head
        self._length+=1
        pass
    
    def Append(self, elem):
        if(self.isEmpty()):
            self._head=LNode(elem, None, None)
            self._tail=self._head
        else:
            self._tail=LNode(elem, self._tail, None)
            self._tail.prev.next=self._tail          
        self._length+=1
        pass
    
    def Pop(self):
        if(self.isEmpty()):
            raise UnderflowError
        else:
            e=self._head.elem
            self._head=self._head.next
            if(self._head==None): #self._length==1
                self._tail=None #completely let the last LNode's citing number==0
            else:
                self._head.prev=None
            self._length-=1
            return e
        pass
    
    def PopLast(self):
        if(self.isEmpty()):
            raise UnderflowError
        else:                
            e=self._tail.elem
            self._tail=self._tail.prev
            if(self._tail==None): #self._length==1
                self._head=None #completely let the last LNode's citing number==0
            else:
                self._tail.next=None
            self._length-=1
            return e
        pass
    
    ####Seek() based functions
    def InsertAfter(self, pos, elem):
        if(pos==self._length-1 or self.isEmpty()):
            self.Append(elem)
        else:
            it=self.Seek(pos)
            it.next=LNode(elem, it, it.next)
            it.next.next.prev=it.next
            self._length+=1
        pass
    def InsertBefore(self, pos, elem):
        if(pos==0 or self.isEmpty()):
            self.Prepend(elem)
        else:
            it=self.Seek(pos)
            it.prev=LNode(elem, it.prev, it)
            it.prev.prev.next=it.prev
            self._length+=1
        pass
    def Delete(self, pos):#returns the deleted data
        if(pos==0):
            return self.Pop()
        elif(pos==self._length-1):
            return self.PopLast()
        else:
            it=self.Seek(pos)
            it.prev.next=it.next
            it.next.prev=it.prev
            self._length-=1
            return it.elem
    pass
