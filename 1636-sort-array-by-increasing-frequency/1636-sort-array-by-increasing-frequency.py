class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        answ = sorted(count.keys(), key = lambda x: (count[x], -x))
        res = []
        
        for num in answ:
            res.extend([num] * count[num])
        
        return res
        
                    
                
        