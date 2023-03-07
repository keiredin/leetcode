class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right, best = 1, totalTrips * min(time) + 1, 1
        print(len(time))
        
        while left <= right:
            mid = left + (right-left)//2
            
            result  = self.time(time, mid)
            
            if result >= totalTrips:
                best = mid
                right = mid - 1 
            else:
                left = mid + 1
                
        return best
    
    def time(self, arr, val):
        result = 0
        for i in arr:
            if i <= val:
                result += val//i

        return result
        