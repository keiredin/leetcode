class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        lst = []
        lst[:0] = palindrome
        n = len(lst) // 2 - len(lst) % 2
        
        for i in range(n):
            if lst[i] != 'a':
                lst[i] = 'a'
                return "".join(map(str,lst))
        
        if lst[0] == 'a':
            lst[-1] = 'b'
        else:
            lst[0] = 'a'
        return "".join(map(str,lst))
            
        