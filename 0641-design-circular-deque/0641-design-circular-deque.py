class Node:
    def __init__(self,val,prev=None,nxt=None):
        self.val = val
        self.prev = prev
        self.nxt = nxt

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.left = Node(0)
        self.right = Node(0,self.left,None)
        self.left.nxt = self.right

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        newNode = Node(value)
        prevNode = self.right.prev
        
        self.right.prev = newNode
        newNode.nxt = self.right
        newNode.prev = prevNode
        prevNode.nxt = newNode
        
        self.size -= 1
        
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        newNode = Node(value)
        nextNode = self.left.nxt
        
        self.left.nxt = newNode
        newNode.prev = self.left
        newNode.nxt = nextNode
        nextNode.prev = newNode
        
        self.size -= 1
        
        return True
        
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        prevNode = self.right.prev.prev
        self.right.prev = prevNode
        prevNode.nxt = self.right
        
        self.size += 1
        
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        nextNode = self.left.nxt.nxt
        self.left.nxt = nextNode
        nextNode.prev = self.left
        
        self.size += 1
        
        return True
        
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val
        
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.left.nxt.val
        
        

    def isEmpty(self) -> bool:
        return self.left.nxt == self.right
        

    def isFull(self) -> bool:
        return self.size == 0
        


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