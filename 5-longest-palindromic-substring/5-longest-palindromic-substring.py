class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        answ = ""
        inbound = lambda left,right : left >= 0 and right < len(s) 
        
        for i in range(len(s)):
            l = r = i
            
            # for odd length palindromes
            while inbound(l,r) and s[l] == s[r]:
                cur = r - l + 1
                if cur > res:
                    res = cur
                    answ = s[l:r+1]
                    
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            
            while inbound(l,r) and s[l] == s[r]:
                cur = r - l + 1
                if cur > res:
                    res = cur
                    answ = s[l:r+1]
                l -= 1
                r += 1
                
        return answ
        