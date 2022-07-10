class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n+1)
    
        def helper(n,memo):
            if(n < 3):return n
            if(memo[n] != 0):
                return memo[n]

            memo[n] = helper(n-1, memo) + helper(n-2, memo)
            return memo[n]

        return helper(n,memo)
