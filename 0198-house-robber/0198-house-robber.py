class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # space optimization
        prev = nums[0]
        prev2 = 0

        for i in range(1, len(nums)):
            take = nums[i]
            if i > 1:
                take += prev2

            noTake = 0 + prev
            cur = max(take, noTake)
            prev2 = prev
            prev = cur

        return prev
    
#         dp = [0] * len(nums)
#         dp[0] = nums[0]
        
#         for i in range(1, len(nums)):
#             rob = nums[i]
#             if i > 1:
#                 rob += dp[i-2]
                
#             notRob = dp[i-1]
#             dp[i] = max(rob, notRob)
            
#         return dp[len(nums)-1]
     
#         memo = {}
#         def dp(idx):
#             if idx in memo:
#                 return memo[idx]
#             if idx == 0:
#                 return nums[idx]
#             if idx < 0:
#                 return 0
            
#             pick = nums[idx] + dp(idx-2)
#             notPick = dp(idx-1)

#             memo[idx] = max(pick,notPick)
#             return memo[idx]


#         return dp(len(nums) - 1)

        
        
        
        
        
        
        
        
        
#         if len(nums) < 2:
#             return nums[0]
        
#         prev = nums[0]
#         maxx = max(nums[0],nums[1])
#         for i in range(2, len(nums)):
#             prev, maxx = maxx, max(maxx, prev+nums[i])
    
#         return maxx