class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(capacity):
            count = 0
            for pile in piles:
                count += ceil(pile/capacity)
            return count
        
        
        l,r = 1,max(piles)
        best = r
        while l <= r:
            mid = (l+r) // 2
            
            if helper(mid) > h:
                l = mid + 1
            else:
                best = mid
                r = mid -1
        return best