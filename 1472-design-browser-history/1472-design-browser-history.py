class Node:
    def __init__(self,val,prev,nxt):
        self.val = val
        self.prev = prev
        self.nxt = nxt


class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.cur = Node(homepage,None,None)
        self.left = Node(0,None,self.cur)  
        self.right = Node(0,self.cur,None)
        
        self.cur.nxt = self.right
        self.cur.prev = self.left
        
      
        

    def visit(self, url):
        newNode = Node(url,None,self.right)
        self.right.prev = newNode
        newNode.prev = self.cur
        self.cur.nxt = newNode
        self.cur = self.cur.nxt
        
        

    def back(self, steps):
        while steps and self.cur.prev != self.left:
            steps -= 1
            self.cur = self.cur.prev
            
        return self.cur.val
        

    def forward(self, steps):
        
        while steps and self.cur.nxt != self.right:
            steps -= 1
            self.cur = self.cur.nxt
            
        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)