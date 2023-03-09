class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        if len(self.q1) == 0:
            self.q1.append(x)
        else:
            while self.q1:
                self.q2.append(self.q1.pop())
                
            self.q1.append(x)
            while self.q2:
                self.q1.append(self.q2.pop())
            
        

    def pop(self) -> int:
        return self.q1.popleft()
        
    def top(self) -> int:
        return self.q1[0]
        
    def empty(self) -> bool:
        return len(self.q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()