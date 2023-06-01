class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        def dp(idx,l,memo=None):
            memo = {} if memo is None else memo
            if idx in memo:
                return memo[idx]
            if idx >= l:
                return 0
            
            pick = nums[idx] + dp(idx + 2,l,memo)
            notPick = dp(idx+1,l,memo)
            
            memo[idx] = max(pick, notPick)
            return memo[idx]
        
        ans1 = dp(0,n-1)
        ans2 = dp(1,n)              
        return max(nums[0],ans1,ans2)
        