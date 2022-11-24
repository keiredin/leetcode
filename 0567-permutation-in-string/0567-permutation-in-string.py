class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = Counter(s1)
        countS2 = Counter()
        lenP = len(s1)
        
        
        if len(s1) > len(s2):
            return False
        
        for i in range(lenP):
            countS2[s2[i]] += 1
            
        if countS1 == countS2:
            return True

        l = 0
        for r in range(lenP, len(s2)):            
            countS2 -= {s2[l]:1}                
            countS2[s2[r]] += 1
            l += 1

            if countS1 == countS2:
                return True
            
        return False