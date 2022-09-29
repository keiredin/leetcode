class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        dec_queue = collections.deque()    
        l = r = 0
        curWindowSum = res = 0
        
        while r < len(chargeTimes):
            
            while dec_queue and dec_queue[-1] < chargeTimes[r]:
                dec_queue.pop() 
                
            dec_queue.append(chargeTimes[r])
            
            curWindowSum += runningCosts[r]
            curCost = dec_queue[0] + (r-l+1) * curWindowSum
            
            while dec_queue and curCost > budget:
                
                if chargeTimes[l] == dec_queue[0]:
                    dec_queue.popleft()
                    
                curWindowSum -= runningCosts[l]
                l += 1
                
                if not dec_queue:
                    break
                # re calculate curCost after removing runningCosts[l]
                curCost = dec_queue[0] + (r-l+1) * curWindowSum
            
            if curCost <= budget:
                res = max(res, r-l+1)
            r += 1
                
            
        return res