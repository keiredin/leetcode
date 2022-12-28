class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxHeap = [-1 * pile for pile in piles]
        totalSum = sum(piles)
        heapify(maxHeap)
        
        while k and maxHeap:
            cur = heappop(maxHeap) * -1
            toBeRemoved = floor(cur / 2)
            totalSum -= toBeRemoved
            cur -= toBeRemoved
            
            if cur:
                heappush(maxHeap, -1 * cur)
            k -= 1
                
        return totalSum
        