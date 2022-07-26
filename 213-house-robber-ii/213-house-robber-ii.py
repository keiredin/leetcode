class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        def dp(i,num,memo=None):
            memo = {} if memo is None else memo
            if i in memo:
                return memo[i]
            if i >= len(num):
                return 0
            
            memo[i] = num[i] + max(dp(i+2,num,memo), dp(i+3,num,memo))
            return memo[i]
        
        ans1 = max(dp(0,nums[:n - 1]),dp(1,nums[:n - 1]))
        ans2 = max(dp(0,nums[1:]),dp(1,nums[1:]))              
        return max(nums[0],ans1,ans2)
        