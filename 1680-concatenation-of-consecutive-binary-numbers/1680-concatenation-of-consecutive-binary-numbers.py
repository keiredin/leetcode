class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = (10**9 + 7)
        answ = 0
        
        for i in range(1,n+1):
            bitLength = i.bit_length()
            
            # create space for next number and inter its bit by using or operation
            answ = (answ << bitLength | i) % mod 
        
        return answ 