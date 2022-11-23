class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        minHeap, maxHeap = [], []
        
        for num in nums:
            heappush(minHeap, num)
            heappush(maxHeap, -num)
            
            if len(maxHeap) > 4:
                heappop(maxHeap)
                
            if len(minHeap) > 4:
                heappop(minHeap)
        res = inf
        
        maxHeap = sorted([num * -1 for num in maxHeap])
        i = 0
        while minHeap:
            res = min(res, heappop(minHeap) - maxHeap[i])
            i += 1
        return res
        
#         nums.sort()
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
        