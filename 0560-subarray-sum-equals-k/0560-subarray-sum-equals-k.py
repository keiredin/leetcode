class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answ = 0
        curSum = 0
        prefixSumCount = {0:1}
        
        for n in nums:
            curSum += n
            diff = curSum - k
            
            answ += prefixSumCount.get(diff,0)
            prefixSumCount[curSum] = 1 + prefixSumCount.get(curSum,0) 
            
            
        return answ
            
    
        