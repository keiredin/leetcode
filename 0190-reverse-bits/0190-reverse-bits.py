class Solution:
    def reverseBits(self, n: int) -> int:
        print(n)
        
        answ = 0
        shiftCounter = 0
        while n:
            # check if MSB is 0
            if 1 & n == 1:
                answ |= (1 << (31 - shiftCounter))
                
            n >>= 1
            shiftCounter += 1
            
        return answ
                
                
     
            
            