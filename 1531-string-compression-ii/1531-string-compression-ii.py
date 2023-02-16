class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        edges = set([1,99,9])
        
        @lru_cache(None)
        def dp(start, last, last_count, left):
            
            if left < 0:
                return float('inf')
            if start >= len(s):
                return 0
            if s[start] == last:
                incr = 1 if last_count in edges else 0
                return incr + dp(start+1, last, last_count+1, left)
            else:
                
                use = 1 + dp(start+1, s[start], 1, left)
                
				# delete counter
                delete =  dp(start + 1, last, last_count, left - 1)
                
                return min(use, delete)
            
        return dp(0, "", 0, k)