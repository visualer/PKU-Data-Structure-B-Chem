from LCList import *

class Stack(LCList):
    def __init__(self):
        super(Stack, self).__init__()
        pass
    def Length(self):
        return super(Stack, self).Length()
    def Push(self, elem):
        super(Stack, self).Append(elem)
        pass
    def Pop(self):
        if(self.Length()>1):
            super(Stack, self).MovePointer(-1)
        return super(Stack, self).Delete()
    def Top(self):
        if(self.Length()>1):
            return self._head.prev.elem
        else:
            return self._head.elem
    pass
