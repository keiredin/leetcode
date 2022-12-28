class Solution:
    def halveArray(self, nums: List[int]) -> int:
        maxHeap = [-1 * num for num in nums]
        totalSum = sum(nums)
        half = totalSum / 2
        heapify(maxHeap)
        steps = 0
        
        while maxHeap and totalSum > half:
            cur = heappop(maxHeap) * -1
            cur /= 2
            totalSum -= cur
            
            if cur:
                heappush(maxHeap, -1 * cur)
            steps += 1
                
        return steps