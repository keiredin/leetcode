class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        right = len(nums) - 1
        left = 0
        
        while left < right:
            if nums[left] % 2 == 0 and nums[right] % 2 == 0:
                left += 1
            elif nums[left] % 2 == 1 and nums[right] % 2 == 1:
                right -= 1
            elif nums[left] % 2 == 1 and nums[right] % 2 == 0:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
            else:
                left += 1
                right -= 1
                
        return nums