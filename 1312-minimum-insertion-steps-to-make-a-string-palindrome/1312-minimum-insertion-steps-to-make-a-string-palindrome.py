class Solution:
    def minInsertions(self, s: str) -> int:
        
        memo = {}
        def dp(l,r):
            if (l,r) in memo:
                return memo[l,r]
            if l >= r:
                return 0
            if s[l] == s[r]:
                memo[l,r] = dp(l+1, r-1)
            else:
                memo[l,r] = 1 + min(dp(l+1,r), dp(l,r-1))
                
            return memo[l,r]
            
        return dp(0,len(s)-1)
        