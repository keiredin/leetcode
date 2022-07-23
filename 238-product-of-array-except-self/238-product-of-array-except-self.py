class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answ = [1] * n 
        
        prefix = 1
        for i in range(n):
            answ[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        for i in range(n-1,-1,-1):
            answ[i] *= postfix
            postfix *= nums[i]
            
        return answ
        
        
            
        
        
 
        
        