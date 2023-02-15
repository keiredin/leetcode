class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        a_s = sorted(A)
        
        def dfs(nums, prev):
            if not nums:
                return 1
            
            out = 0
            for i, num in enumerate(nums):
                if i and num == nums[i - 1]:
                    continue
                if prev < 0 or int(sqrt(num + prev))**2 == num + prev:
                    out += dfs(nums[:i] + nums[i+1:], num)
            return out
        return dfs(a_s, -1) if A else 0