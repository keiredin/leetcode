class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        return max(math.prod(nums[0:2]) * nums[-1],math.prod(nums[-3:]))
        
        