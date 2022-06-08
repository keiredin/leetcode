class Solution:
    def removePalindromeSub(self, s: str) -> int:
        start,end = 0, len(s)-1
        
        while start < end:
            if s[start] != s[end]:
                return 2
            start += 1
            end -= 1
            
        return 1


# class Solution:
#     def removePalindromeSub(self, s: str) -> int:
#         return 1 if s == s[::-1] else 2