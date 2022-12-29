class Solution:
    def maxJump(self, nums: List[int]) -> int:
        maxJump = nums[1] - nums[0]
        
        for i in range(2,len(nums),2):
            maxJump = max(nums[i]-nums[i-2],maxJump)
            
        for i in range(3,len(nums),2):
            maxJump = max(nums[i]-nums[i-2],maxJump)
        
        return maxJump
        
        
        