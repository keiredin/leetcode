class Solution:
    def bitwiseComplement(self, num: int) -> int:
        if num == 0: return 1
        
        res = 0
        shiftCounter = 0
        
        while num:
            # check if MSB is 0
            if 1 & num == 0:
                res |= (1 << shiftCounter)
                
            num >>= 1
            shiftCounter += 1
                
        return res