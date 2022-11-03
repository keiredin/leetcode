class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefSum = [*nums]
        for i in range(1,len(nums)):
            prefSum[i] = prefSum[i-1] + nums[i]
            
        for i in range(len(nums)):
            leftSum = prefSum[i] - nums[i]
            rightSum = prefSum[-1] - prefSum[i]
            if leftSum  == rightSum:
                return i
            
        return -1
        