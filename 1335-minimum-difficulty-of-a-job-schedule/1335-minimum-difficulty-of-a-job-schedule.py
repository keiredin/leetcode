# Recursion with Memoization, Top-down

# Starting from the last day, we simply try out all the possible schdules for each day.
# We track the intended finished day (intended) and the first i-th jobs (end).



# from functools import lru_cache
# class Solution:
#     def minDifficulty(self, J, d):
#         @lru_cache(maxsize=None) # memoization
#         def helper(intended, end):
# 		    # the base case, if we only have 1 day left, we need to handle all the tasks on that day
#             if intended == 1: return max(J[:end])
			
#             res, mx = math.inf, 0
#             for done in range(1,end-intended+2):
#                 mx = max(mx, J[end-done])
#                 res = min(helper(intended-1, end-done) + mx, res)
#             return res                
        
#         return helper(d, len(J)) if len(J) >= d else -1
    
    
# DP, Bottom-up

class Solution:
    def minDifficulty(self, J, d):
        if len(J) < d: return -1
        
        dp = {} # (index of day, index of the last finished job)
        for i,job in enumerate(J):
            # the base case, all jobs need to be finish in one day
            dp[0, i] = max(dp.get((0, i-1), 0), job)
            
        for i in range(1, d):
            for j in range(i, len(J)):
                mx = J[j]
                for k in range(j, i-1, -1):
                    mx = max(mx, J[k])
                    dp[i, j] = min(dp.get((i, j), math.inf), mx + dp[i-1, k-1])
                
        return dp[d-1, len(J)-1]