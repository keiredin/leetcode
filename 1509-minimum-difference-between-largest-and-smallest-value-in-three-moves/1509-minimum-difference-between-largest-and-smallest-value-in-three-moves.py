class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        # there are three possibilities
        
        #possibility 1 - remove the first 3
        poss1 = nums[-1] - nums[3]
        
        # remove the first two and the last element
        poss2 = nums[-2] - nums[2]
        
        #remove the first and the last two elements
        poss3 = nums[-3] - nums[1]
        
        # remove the last three
        poss4 = nums[-4] - nums[0]
        
        return min(poss1,poss2,poss3,poss4)
        