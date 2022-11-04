class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        print(s)
        
        l,r = 0,len(s)-1
        while l < r:
            if (s[l] in "aeiou" or s[l] in "AEIOU" ) and (s[r] in "aeiou" or s[r] in "AEIOU"):
                s[l],s[r] = s[r],s[l]
                l += 1
                r -= 1
            elif s[l] in "aeiou" or s[l] in "AEIOU":
                r -= 1
            elif s[r] in "aeiou" or s[r] in "AEIOU":
                l += 1
            else:
                l += 1
                r -= 1
                
        return "".join(s)
        