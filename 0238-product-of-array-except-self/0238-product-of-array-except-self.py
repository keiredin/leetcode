class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix_arr = [1] * n 
        prefix = 1
        for i in range(n):
            prefix_arr[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        postfix_arr = [1] * n 
        for i in range(n-1,-1,-1):
            postfix_arr[i] *= postfix
            postfix *= nums[i]
            
            
        res = [] 
        for i in range(n):
            cur_res = postfix_arr[i] * prefix_arr[i]
            res.append(cur_res)
            
        return res
        
        
            
        
        
 
        
        