# class MyCircularQueue:

#     def __init__(self, k: int):
        

#     def enQueue(self, value: int) -> bool:
        

#     def deQueue(self) -> bool:
        

#     def Front(self) -> int:
        

#     def Rear(self) -> int:
        

#     def isEmpty(self) -> bool:
        

#     def isFull(self) -> bool:

class Node:
    def __init__(self,val,prev,nxt):
        self.val = val
        self.prev = None
        self.nxt = None
        

class MyCircularQueue:

    def __init__(self, k):
        self.size = k
        self.left = Node(0,None,None)
        self.right = Node(0,self.left,None)
        self.left.nxt = self.right
        
    def enQueue(self, value):
        if self.isFull():
            return False
        newNode = Node(value,None,None)
        nextNode = self.left.nxt
        
        self.left.nxt = newNode
        newNode.prev = self.left
        newNode.nxt = nextNode
        nextNode.prev = newNode
        
        self.size -= 1
        
        return True
    def deQueue(self):
        if self.isEmpty():
            return False
        
        prevNode = self.right.prev.prev
        self.right.prev = prevNode
        prevNode.nxt = self.right
        
        self.size += 1
        
        return True
        

    def Front(self):
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.left.nxt.val

    def isEmpty(self):
        return self.left.nxt == self.right

    def isFull(self):
        return self.size == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()