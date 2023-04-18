class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        turn = True
        res = ""
        
        i,j = 0,0
        
        while i < len(word1) and j < len(word2):
            if turn:
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1
            turn = not turn
            
        if i < len(word1):
            res += word1[i:]
        if j < len(word2):
            res += word2[j:]
            
        return res
        