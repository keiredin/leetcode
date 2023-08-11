class Solution:
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay): return -1
        
        def search(mid,k):
            count = 0
            flower = 0
            i = 0

            while i < len(bloomDay):
                                
                if bloomDay[i] <= mid:
                    flower += 1
                else:
                    flower = 0

                if flower >= k:
                    flower = 0
                    count += 1
            
                i += 1

            return count
    
  

        l = min(bloomDay)
        r = max(bloomDay)


        best = r
        while l <= r:
            mid = (l+r) // 2
            if search(mid,k) < m:
                l = mid + 1
            else:
                best = mid
                r = mid - 1

        return best


        