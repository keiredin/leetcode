class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        answ = 0
        xor = 0
        
        for num in nums:
            xor ^= num
            
            
        firstSetBitPos = 0
        
        # to find the rightmost set bit
        while xor & 1 == 0:
            firstSetBitPos += 1
            xor >>= 1
        
        mask = 1 << firstSetBitPos
        # print(firstSetBitPos,mask)
        num1,num2 = 0, 0
        
        for num in nums:
            if num & mask != 0:
                num1 ^= num
            else:
                num2 ^= num
                
        return [num1,num2]
            

        