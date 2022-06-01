class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums
    

# # one line 
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         s = 0
#         return [s:=s+v for _, v in enumerate(nums)]