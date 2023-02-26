class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start,end = 0,0
        maxS = 0
        sett = set()
        
        while end < len(s):
            if s[end] not in sett:
                sett.add(s[end])

            else:
                maxS = max(maxS, end-start)
                while s[end]  in sett:
                    sett.remove(s[start])
                    start += 1
                    
                sett.add(s[end])
                
            end += 1
        maxS = max(maxS, end-start)
        return maxS
            
        