class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = str(x)
        
        l,r = 0, len(digits)-1
        
        while l < r:
            if digits[l] != digits[r]:
                return False
            l += 1
            r -= 1
        
        return True
        