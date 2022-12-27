class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff = [capacity[i] - rocks[i] for i in range(len(rocks))]
        diff.sort()
        
        countFull = 0
        
        for num in diff:
            if additionalRocks >= num:
                countFull += 1
                additionalRocks -= num
            else:
                break
                
        return countFull
            
        