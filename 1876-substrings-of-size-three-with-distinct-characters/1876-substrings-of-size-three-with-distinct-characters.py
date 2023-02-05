class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        unique = defaultdict(int)
        
        count,l,r = 0,0,0
        while r < len(s):
            unique[s[r]] += 1
            if r-l >= 2:
                count += len(unique) == 3
                unique[s[l]] -= 1 
                if unique[s[l]] == 0:
                    del unique[s[l]]
                l+= 1
            r += 1
        return count
        