from functools import lru_cache
class Solution:
    def minDifficulty(self, J, d):
        @lru_cache(maxsize=None) # memoization
        def helper(intended, end):
		    # the base case, if we only have 1 day left, we need to handle all the tasks on that day
            if intended == 1: return max(J[:end])
			
            res, mx = math.inf, 0
            for done in range(1,end-intended+2):
                mx = max(mx, J[end-done])
                res = min(helper(intended-1, end-done) + mx, res)
            return res                
        
        return helper(d, len(J)) if len(J) >= d else -1