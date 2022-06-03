class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
            
        minn = min(nums)
        return 1 if minn > 0 else -minn + 1
        