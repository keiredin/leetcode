class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        answ = []
        potions.sort()
        
        def findValue(spell):
            idx = bisect.bisect_left(potions, success / spell)
            return idx
        
        
        for spell in spells:
            idx = findValue(spell)
            if idx < len(potions):
                answ.append(len(potions) - idx)
            else:
                answ.append(0)
        
        
        return answ
        
            
        