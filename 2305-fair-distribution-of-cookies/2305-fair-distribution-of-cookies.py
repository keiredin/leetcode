class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if len(cookies) == k:
            return max(cookies)
        
        bucks = [0] * k
        maxRes = inf
        
        def backtrack(i):
            nonlocal maxRes
            if max(bucks) > maxRes:
                return
            if i == len(cookies):
                maxRes = min(maxRes, max(bucks))
                return
                
            for j in range(k):
                bucks[j] += cookies[i]
                backtrack(i+1)
                bucks[j] -= cookies[i]
                
        backtrack(0)
        return maxRes