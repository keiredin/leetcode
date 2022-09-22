class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l,count,product = 0,0,1
        
        for r in range(len(nums)):
            product *= nums[r]
            while product >= k and l <= r:
                product /= nums[l]
                l += 1
            
            count += r-l+1
        return count