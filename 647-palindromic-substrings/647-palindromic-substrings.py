class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        inbound = lambda left,right : left >= 0 and right < len(s) 
        
        for i in range(len(s)):
            l = r = i
            
            # for odd length palindromes
            while inbound(l,r) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            
            while inbound(l,r) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
                
        return res
                
        