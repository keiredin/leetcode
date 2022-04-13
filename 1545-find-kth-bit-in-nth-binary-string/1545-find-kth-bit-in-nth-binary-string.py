class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        answ = self.recursive(n,k)
        return answ[k-1]
    
    def recursive(self,num,k):
        if num == 1:
            return "0"
        curr = self.recursive(num-1,k)
        res =  curr + "1" + self.reverse(self.invert(curr))
        if len(res) >= k:
            return res
        return res
          
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
        