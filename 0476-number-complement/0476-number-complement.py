class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        i = 0
        
        while num:
            # check if MSB is 0
            if 1 & num == 0:
                res |= (1 << i)
                
            num >>= 1
            i += 1
                
        return res
                
            
            

            
        
        