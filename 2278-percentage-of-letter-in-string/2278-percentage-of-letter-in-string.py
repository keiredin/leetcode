class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        for char in s:
            count += letter == char
            
        return int((count/len(s)) * 100)