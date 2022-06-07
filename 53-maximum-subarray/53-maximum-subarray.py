class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm
        maxSumSoFar  = nums[0]
        maxSumEndHere = maxSumSoFar
        
        for i in range(1,len(nums)):
            maxSumEndHere = max( maxSumEndHere + nums[i], nums[i])
            maxSumSoFar = max(maxSumSoFar, maxSumEndHere)
                
        return maxSumSoFar

#     # dp
#     def maxSubArray(self, nums) -> int:
#         def find(index, curr_max):
#             if index >= len(nums):
#                 return float('-inf')
#             curr_max = max(nums[index], curr_max + nums[index])
#             return max(curr_max,  find(index + 1, curr_max))
#         return find(0, 0)
    
    
    