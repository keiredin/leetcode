class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        
        
        def dp(curSum):
            if curSum == target:
                return 1
            if curSum > target:
                return 0
            
            if curSum in memo:
                return memo[curSum]
            
            ans = 0
            for j in range(len(nums)):
                ans += dp(curSum + nums[j]) 
                
            memo[curSum] = ans
            return memo[curSum]
        
        answ = dp(0)
        # print(memo)
        return answ
        
                
                
                