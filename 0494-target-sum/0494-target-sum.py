class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.totalWays(0, target, nums, {})
        
    def totalWays(self,curIndex, targetSum, nums,memo):
        
        if (curIndex, targetSum) in memo:
            return memo[curIndex, targetSum]
        
        if targetSum == 0 and curIndex == len(nums):
            return 1
        if curIndex >= len(nums):
            return 0
        
        usePlus = self.totalWays(curIndex + 1, targetSum - nums[curIndex], nums,memo)
        useMinus = self.totalWays(curIndex + 1, targetSum + nums[curIndex], nums, memo)
        
        memo[curIndex, targetSum] = usePlus + useMinus
        return memo[curIndex, targetSum]
            
        