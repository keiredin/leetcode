class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        pairs = 0
        leftOver = 0
        
        for key in count:
            pairs += count[key] // 2
            leftOver += count[key] % 2
        return [pairs, leftOver]
        