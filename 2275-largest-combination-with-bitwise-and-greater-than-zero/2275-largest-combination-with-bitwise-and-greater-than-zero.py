class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0
        
        for i in range(31,-1,-1):
            count = 0
            for num in candidates:
                if num & (1 << i) != 0:
                    count += 1
            res = max(res,count)
            
        return res
        