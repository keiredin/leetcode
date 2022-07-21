class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # this changes the question to 560. Subarray Sum Equals K
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
                
        prefixSumCount = defaultdict(int)
        prefixSumCount[0] = 1
        curSum = 0
        answ = 0
        
        for n in nums:
            curSum += n
            diff = curSum - k
            
            answ += prefixSumCount.get(diff,0)
            prefixSumCount[curSum] += 1
             
        return answ
            
                
            