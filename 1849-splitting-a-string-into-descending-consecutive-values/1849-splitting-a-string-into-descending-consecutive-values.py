class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(start, prev,splitCount):
            if start == len(s) and splitCount >= 2:
                return True
            
            for i in range(start, len(s)):
                num = int(s[start:i+1])
                if num == prev - 1 or prev == -1:
                    if backtrack(i+1, num, splitCount + 1):
                        return True
            return False
        
        return backtrack(0, -1,0)

        