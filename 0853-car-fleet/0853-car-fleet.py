class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speedPair = [[p,s] for p,s in zip(position,speed)]
        
        pos_speedPair = sorted(pos_speedPair, reverse=True)
        
        mon_stack = []
        fleets = len(position)
        for p,s in pos_speedPair:
            timeTaken = (target - p) / s
            if not mon_stack:
                mon_stack.append(timeTaken)
            else:
                if timeTaken <= mon_stack[-1]:
                    fleets -= 1
                else:
                    mon_stack.append(timeTaken)
                    
        return fleets