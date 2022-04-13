class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        answ = self.recursive(n)
        return answ[k-1]
    
    def recursive(self,num):
        if num == 1:
            return "0"
        return self.recursive(num-1) + "1" + self.reverse(self.invert(self.recursive(num-1)))
          
    def reverse(self,s):
        return s[::-1]
    def invert(self,s):
        newS = []
        for i in s:
            if i == "1":
                newS.append("0")
            else:
                newS.append("1")
                
        return "".join(newS)
        