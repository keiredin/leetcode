class Solution:
    def numSplits(self, s: str) -> int:
        sLeft = defaultdict(int)
        sRight = Counter(s)
        
        lenSleft, lenSright = 0, len(sRight)
        answ = 0
        
        for i in range(1,len(s)+1):
            
            if s[i-1] not in  sLeft:
                lenSleft += 1
                sLeft[s[i-1]] += 1
            
            if sRight[s[i-1]] > 1:
                sRight[s[i-1]] -= 1
            else:
                lenSright -= 1
                
            if lenSleft == lenSright:
                answ += 1
                
        return answ
        
    