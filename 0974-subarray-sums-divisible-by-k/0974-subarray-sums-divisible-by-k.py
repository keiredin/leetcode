class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = [0] * k
        count[0] = 1
        subarrayCount,summ = 0,0
        for i in range(len(nums)):
            summ += nums[i]
            mod = (summ % k + k) % k
            subarrayCount += count[mod]
            count[mod] += 1
        
        return subarrayCount
        
        
        
        
