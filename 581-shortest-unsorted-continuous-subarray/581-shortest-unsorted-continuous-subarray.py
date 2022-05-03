class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        end = -1
        maxx = nums[0]
        
        for i in range(1,len(nums)):
            if maxx > nums[i]: # the left value is greater than the current
                end = i
            else:
                maxx = nums[i]
        start = 0
        minn = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if minn < nums[i]: # the right value is smaller then current value
                start = i
            else:
                minn = nums[i]
        
        return end-start + 1
    
    

                
        
                
                
        