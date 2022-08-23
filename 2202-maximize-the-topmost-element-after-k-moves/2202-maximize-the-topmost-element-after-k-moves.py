class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if (len(nums) == 1) and (k & 1): return -1
        
        maxx = -1
        for i in range(min(len(nums), k-1)):
            maxx = max(maxx, nums[i])
        
        if k < len(nums):
            maxx = max(maxx, nums[k])
            
        return maxx
        