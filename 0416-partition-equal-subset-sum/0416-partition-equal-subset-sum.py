class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2 != 0: return False
        
        target = summ // 2
        memo = {}
        def dp(i,halfSum):
            if (i,halfSum) in memo:
                return memo[i,halfSum]
            if i == len(nums):
                return halfSum == target
            if halfSum > target:
                return False
            memo[i,halfSum] =  dp(i+1, halfSum + nums[i]) or dp(i+1, halfSum)
            return memo[i,halfSum]
        
        return dp(0,0)
        