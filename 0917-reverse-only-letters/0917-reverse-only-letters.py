class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l,r = 0,len(s)-1 
        s = list(s)
        
        while l < r:
            if s[l].isalpha() and s[r].isalpha():
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l].isalpha():
                r -= 1
            elif s[r].isalpha():
                l += 1
            else:
                l += 1
                r -= 1
                
        return "".join(s)
                
                
        