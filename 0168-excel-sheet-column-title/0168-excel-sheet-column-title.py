class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        numCHarMap = {0:"Z"}
        for i in range(1,26):
            numCHarMap[i] = chr(64 + i)
     
        answ = ""
        while columnNumber > 0:
            cur = columnNumber % 26
            columnNumber //= 26
            
            if cur == 0: columnNumber -= 1
            answ += numCHarMap[cur]
        return answ[::-1]
            
            