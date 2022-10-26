class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainderIdxMap = {0:-1}
        summ = 0
        
        for i in range(len(nums)):
            summ += nums[i]
            
            remainder = summ % k
            if remainder in remainderIdxMap:
                if i - remainderIdxMap[remainder] >= 2:
                    return True
            else:
                remainderIdxMap[remainder] = i
            
        return False
                