class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        count = defaultdict(int)
        
        for i in range(1,len(nums)):
            if nums[i-1] == key:
                count[nums[i]] += 1
        return max(count.items(), key = lambda x: x[1])[0]
        