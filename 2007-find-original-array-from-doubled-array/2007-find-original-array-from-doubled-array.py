class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if(n%2 != 0):
            return []
        count = Counter(changed)
        changed.sort()
        original = []
        
        for num in changed:
            if num == 0 and count[num] >= 2:
                count[num] -= 2
                original.append(num)
            elif num > 0 and count[num] and count[num*2]:
                count[num] -= 1
                count[num*2] -= 1
                original.append(num)
                
        return original if len(original) == n // 2 else []