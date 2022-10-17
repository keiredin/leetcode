class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        count = Counter(s)
        
        oddCount = 0
        
        for key,val in count.items():
            if val % 2 == 1:
                oddCount += 1
                
        return len(s) >= k and oddCount <= k
        