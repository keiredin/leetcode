class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            
            memo[i] = nums[i] + max(dfs(i+2), dfs(i+3))
            return memo[i]
        
        return max(dfs(0),dfs(1))
        
        
        
        
        
        
        
        
        
        
        
        
#         if len(nums) < 2:
#             return nums[0]
        
#         prev = nums[0]
#         maxx = max(nums[0],nums[1])
#         for i in range(2, len(nums)):
#             prev, maxx = maxx, max(maxx, prev+nums[i])
    
#         return maxx