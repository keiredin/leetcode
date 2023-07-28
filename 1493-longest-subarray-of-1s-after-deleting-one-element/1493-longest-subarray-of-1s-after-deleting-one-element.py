class Solution:
    def longestSubarray(self, nums):
        # Number of zero's in the window.
        zeroCount = 0
        longestWindow = 0
        # Left end of the window.
        start = 0
        
        for i in range(len(nums)):
            zeroCount += 1 if nums[i] == 0 else 0
                          
            # Shrink the window until the zero counts come under the limit.
            while zeroCount > 1:
                zeroCount -= 1 if nums[start] == 0 else 0
                start += 1
              
            longestWindow = max(longestWindow, i - start)
        
        return longestWindow

            
        