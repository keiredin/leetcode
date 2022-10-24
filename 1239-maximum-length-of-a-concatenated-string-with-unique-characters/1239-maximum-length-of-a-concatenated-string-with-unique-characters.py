class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.maximum = 0
        def backtrack(start,array,s):
            if len(s)==len(set(s)):
                self.maximum = max(self.maximum,len(s))
            else:
                return
            for i in range(start,len(array)):
                backtrack(i+1,array,s + array[i])
                
        backtrack(0,arr,"")
        return self.maximum
        