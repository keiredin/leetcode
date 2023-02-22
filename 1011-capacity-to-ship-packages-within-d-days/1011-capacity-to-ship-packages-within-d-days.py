class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        capacity = r
        
        
        while l <= r:
            mid = (l + r) // 2
            if self.helper(weights,days,mid):
                capacity = mid
                r = mid - 1
            else:
                l = mid + 1
                
        return capacity
    
    def helper(self,weights,days,capacity):
        days_needed = 1
        summ = 0
        for i in weights:
            if summ + i <= capacity:
                summ += i
                
            else:
                summ = 0
                days_needed += 1
                summ += i
                
        if days_needed <= days:
            return True
        else:
            return False
                
                    