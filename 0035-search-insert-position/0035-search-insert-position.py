class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i,num in enumerate(nums):
            if num == target or num > target:
                return i
            
        return len(nums)