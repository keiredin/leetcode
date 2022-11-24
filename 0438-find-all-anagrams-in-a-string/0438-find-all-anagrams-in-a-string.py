class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countS = Counter()
        countP = Counter(p)
        lenP = len(p)
        
        if len(p) > len(s):
            return []
        
        for i in range(lenP):
            countS[s[i]] += 1
            
        answ = []
        l = 0
        if countS == countP:
            answ.append(l)

        for r in range(lenP, len(s)):            
            countS -= {s[l]:1}                
            countS[s[r]] += 1
            l += 1

            if countS == countP:
                answ.append(l)
            
        return answ
        