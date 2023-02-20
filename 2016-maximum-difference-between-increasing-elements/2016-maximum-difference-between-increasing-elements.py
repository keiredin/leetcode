class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)-1
        res = -1
        for j in range(n,0,-1):
            for i in range(j-1,-1,-1):
                res = max(res, nums[j] - nums[i])
                
        return res if res > 0 else -1
        