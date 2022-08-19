class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
            
        def helper(candidate, h):
            answ = 0
            for i in range(len(piles)):
                answ += (ceil(piles[i] / candidate))
            return answ
                
        l,r = 1,max(piles)
        best = r
        while l <= r:
            mid = (l+r) // 2
            res = helper(mid,h)
            if res > h:
                l = mid + 1
            else:
                best = mid
                r = mid - 1
        return best
            
        