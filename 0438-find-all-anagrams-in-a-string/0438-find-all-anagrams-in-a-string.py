class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countS = defaultdict(int)
        countP = Counter(p)
        lenP = len(p)
        
        if len(p) > len(s):
            return []
        
        for i in range(lenP):
            countS[s[i]] += 1
            
        answ = []
        l = 0
        for r in range(lenP, len(s)):
            if countS == countP:
                answ.append(l)
            
            if countS[s[l]] > 1:
                countS[s[l]] -= 1
            else:
                del countS[s[l]]
                
            countS[s[r]] += 1
            l += 1
            r += 1
            
        if countS == countP:
            answ.append(l)
            
        return answ
        