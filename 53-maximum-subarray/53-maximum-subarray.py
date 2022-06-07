class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         # kadane's algorithm
#         maxSumSoFar, maxSumEndHere = 0, 0
        
#         for i in range(len(nums)):
#             maxSumEndHere += nums[i]
            
#             if maxSumEndHere < 0:
#                 maxSumEndHere = 0
                
#             if maxSumSoFar  < maxSumEndHere:
#                 maxSumSoFar = maxSumEndHere
                
#         return maxSumSoFar

    # dp
    def maxSubArray(self, nums) -> int:
        def find(index, curr_max):
            if index >= len(nums):
                return float('-inf')
            curr_max = max(nums[index], curr_max + nums[index])
            return max(curr_max,  find(index + 1, curr_max))
        return find(0, 0)