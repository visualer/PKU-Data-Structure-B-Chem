class LNode: #LDNode
    def __init__(self, elem, prev, next_):
        self.elem=elem
        self.next=next_
        self.prev=prev
        pass
    pass

class LCList():#LDCList, without iterator
    def __init__(self):
        self._head=None
        self._length=0
        self._pointer=None
        self._moved=False
        pass
    def Length(self):
        return self._length
    def isEmpty(self):
        return self._length==0
    def isValid(self):
        return not(self._length==0 or self._length==1)
    def Iterable(self): #Generator Function
        it=self._head
        count=0
        while(count!=self._length):
            yield it.elem
            it=it.next
            count+=1
        pass
    def Print(self):
        print("[", end=' ')
        for i in self.Iterable():
            print(i, end=' ')
        print("]")
        pass
    def MovePointer(self, steps):
        if(not self.isValid()):
            raise StopIteration("No enough elements")
        if(steps==0):
            self._moved=True
            return None
        elif(steps<0):
            self._moved=True
            for i in range(-steps):
                self._pointer=self._pointer.prev
        else:
            self._moved=True
            for i in range(steps):
                self._pointer=self._pointer.next
        pass
    def MovePointerTo(self, pos):
        self._pointer=self.Seek(pos)
        pass
    def GetPointerPos(self):
        raise NotImplementedError
    def GetPointerElem(self):
        return self._pointer.elem
    def SetPointerElem(self, elem):
        self._pointer.elem=elem
        pass
    def ResetPointer(self):
        self._pointer=self._head

        
    def Seek(self, pos):
        if(pos<0 or pos>=self._length):
            raise IndexError
        elif(pos>=self._length/2):
            it=self._head.prev
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
    def __getitem__(self, pos):
        return self.Seek(pos).elem
    def __setitem__(self, pos, elem):
        self.Seek(pos).elem=elem
    
    #prepend partially identical to append
        
    #based on head pointer operations  
    def Append(self, elem):
        if(self._length==0):
            self._head=LNode(elem, None, None)
            self._length+=1
            self._pointer=self._head
        else:
            self._head.prev=LNode(elem, self._head.prev, self._head)
            if(self._head.prev.prev==None): #self._length==1
                self._head.next=self._head.prev
                self._head.prev.prev=self._head
            else:
                self._head.prev.prev.next=self._head.prev
            self._length+=1
            pass
        pass
    def Prepend(self, elem):#pointer perturbation!
        self.Append(elem)
        if(self._head.prev!=None): #pointer move forward if _length>=2
            self._head=self._head.prev
            if(not self._moved):
                self.ResetPointer()
        pass


    #calibrated operations, both position and _pointer
    def InsertAfter(self, elem, pos=-1):#without pos will operate on _pointer; 
        flag=(pos!=-1)
        if(self._length==0 or self._length==1):#Only choice
            self.Append(elem)
        else:
            if(flag):
                if(pos<-1 or pos>=self._length):
                    raise IndexError
                if(pos==self._length-1):
                    self.Append(elem)
                    return None
            else:
                if(self._pointer is self._head.prev):
                    self.Append(elem)
                    return None
            if(flag):
                it=self.Seek(pos)
            else:
                it=self._pointer
            it.next=LNode(elem, it, it.next)
            it.next.next.prev=it.next
            self._length+=1
            pass
        pass
    
    def InsertBefore(self, elem, pos=-1):#perturbation of pointer
        flag=(pos!=-1)
        if(self._length==0 or self._length==1):#Only Choice
            self.Prepend(elem)
        else:
            if(flag):
                if(pos<-1 or pos>=self._length):
                    raise IndexError
                if(pos==0):
                    self.Prepend(elem)
                    return None
            else:
                if(self._pointer is self._head):
                    self.Prepend(elem)
                    return None
            if(flag):
                it=self.Seek(pos)
            else:
                it=self._pointer
            it.prev=LNode(elem, it.prev, it)
            it.prev.prev.next=it.prev
            self._length+=1
            if(not self._moved):#WARNING
                self.ResetPointer()
            pass
        pass
    
    def Delete(self, pos=-1):#Delete and move to next pointer domain
        flag=(pos!=-1)
        if(self._length==0):
            raise UnderflowError("No element")
        elif(self._length==1):
            e=self._head.elem
            self._head=None
            self._length-=1
            self._pointer=None
            return e
        elif(self._length==2):
            if(flag):
                it=self.Seek(pos)
            else:
                it=self._pointer
            self._head=it.next
            self._head.prev=None
            self._head.next=None
            self._length-=1
            self._pointer=self._head
            return it.elem
        else:
            if(flag):
                if(pos<-1 or pos>=self._length):
                    raise IndexError
                it=self.Seek(pos)
            else:
                it=self._pointer
            if(it==self._pointer):
                self._pointer=self._pointer.next #move to next domain
            if(it is self._head):#Ugh.
                self._head=self._head.next
            if(not self._moved):
                '''WARNING: even if you haven't used MovePointer(0),
                if you delete the _head, the pointer will still move to the next "_head".'''
                self.ResetPointer()
            it.prev.next=it.next
            it.next.prev=it.prev
            self._length-=1
            return it.elem
