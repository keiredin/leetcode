class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                choise1 = self.isPalindrome(l+1, r, s)
                choise2 = self.isPalindrome(l, r-1, s)
                return choise1 or choise2
            l += 1
            r -= 1
        return True
        
    def isPalindrome(self,l,r,s):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        