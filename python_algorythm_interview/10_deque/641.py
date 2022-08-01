class MyCircularDeque:
    
    def __init__(self, k: int):
        self.arr=[None]*k
        self.front=0
        self.rear=0
        self.maxlen=k
    def insertFront(self, value: int) -> bool:
        if(self.isFull()):
            return False
        if(self.isEmpty()):
            self.arr[self.front]=value
            return True
        else:
            self.front=(self.front+self.maxlen-1)%self.maxlen
            self.arr[self.front]=value
            return True

    def insertLast(self, value: int) -> bool:
        if(self.isFull()):
            return False
        if(self.isEmpty()):
            self.arr[self.front]=value
            return True
        else:
            self.rear=(self.rear+1)%self.maxlen
            self.arr[self.rear]=value
            return True

    def deleteFront(self) -> bool:
        if(self.isEmpty()):
            return False
        if(self.front==self.rear):
            self.arr[self.front]=None
            return True
        else:
            self.arr[self.front]=None
            self.front=(self.front+1)%self.maxlen
            return True

    def deleteLast(self) -> bool:
        if(self.isEmpty()):
            return False
        if(self.front==self.rear):
            self.arr[self.rear]=None
            return True
        else:
            self.arr[self.rear]=None
            self.rear=(self.rear-1)%self.maxlen
            return True
    def getFront(self) -> int:
        if(self.isEmpty()):
            return -1
        return self.arr[self.front]

    def getRear(self) -> int:
        if(self.isEmpty()):
            return -1
        return self.arr[self.rear]

    def isEmpty(self) -> bool:
        return self.front==self.rear and self.arr[self.front]==None

    def isFull(self) -> bool:
        return self.front==(self.rear+1)%self.maxlen 


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()