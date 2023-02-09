class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        idx = 0
        
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                idx = i
                break
        
        largest = idx
        for i in range(idx, len(nums)):
            if nums[i] >= nums[largest]:
                largest = i
       
        
        for i in range(idx):
            if nums[i] < nums[largest]:
                nums[i],nums[largest] = nums[largest],nums[i]
                break
        
        return int("".join(nums))
                