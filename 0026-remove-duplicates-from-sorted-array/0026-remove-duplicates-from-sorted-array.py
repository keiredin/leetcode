class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         i = 0
#         j = 1
#         while j < len(nums):
#             if nums[i] == nums[j]:
#                 nums.pop(j)
                
#             else:
#                 i +=1
#                 j += 1
#         return len(nums)
                

        
    def removeDuplicates(self,nums: 'List[int]') -> int:
        if not nums:
            return 0
        slow = 0
        for fast in range(1, len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
            
        
        
        