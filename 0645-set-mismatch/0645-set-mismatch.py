class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        duplicated, missing = -1,1
        
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                duplicated = nums[i]
            elif nums[i] > nums[i-1] + 1:
                missing = nums[i-1] + 1
                
        return [duplicated,len(nums) if nums[-1] != len(nums) else missing]
        