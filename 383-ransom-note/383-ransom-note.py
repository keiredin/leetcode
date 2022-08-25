class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countMagazine = Counter(magazine)
        
        for char in ransomNote:
            if char not in countMagazine or countMagazine[char] <= 0:
                return False
            
            countMagazine[char] -= 1
            
        return True
        