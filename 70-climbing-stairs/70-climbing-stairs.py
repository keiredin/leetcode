# memoization
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         memo = [0] * (n+1)
    
#         def helper(n,memo):
#             if(n < 3):return n
#             if(memo[n] != 0):
#                 return memo[n]

#             memo[n] = helper(n-1, memo) + helper(n-2, memo)
#             return memo[n]

#         return helper(n,memo)

# DP - bottom up

# // Time complexity: O(n)
# // Space complexity: O(n)
    
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = [0] * (n+1)
#         dp[0] = 1
#         dp[1] = 1
        
#         for i in range(2,n+1):
#             dp[i] = dp[i-1] + dp[i-2]
            
#         return dp[n]
    

# Bottom-Up DP (Space Optimized)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n
        n1, n2 = 2, 3
        
        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2

