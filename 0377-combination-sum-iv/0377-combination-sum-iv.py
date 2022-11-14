class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
#         memo = [-1]*(target + 1)
        
#         def dp(curSum):
#             if curSum == target:
#                 return 1
#             if curSum > target:
#                 return 0
            
#             if memo[curSum] != -1:
#                 return memo[curSum]
            
#             ans = 0
#             for j in range(len(nums)):
#                 ans += dp(curSum + nums[j]) 
                
#             memo[curSum] = ans
#             return memo[curSum]
        
#         answ = dp(0)
#         print(memo)
#         return answ
    
    
        dp = [0]*(target + 1)
        dp[target] = 1
        for state in range(target)[::-1]:
            for val in nums:
                if state + val < len(dp):
                    dp[state] += dp[state + val]
       
        return dp[0]
        
                
                
                