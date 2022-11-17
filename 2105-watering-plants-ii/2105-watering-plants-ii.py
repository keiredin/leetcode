class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        curCapacityA, curCapacityB = capacityA, capacityB
        refill = 0
        
        l,r = 0,len(plants)-1
        
        while l < r:
            if plants[r] > curCapacityB:
                refill += 1
                curCapacityB = capacityB
            if plants[l] > curCapacityA:
                refill += 1
                curCapacityA = capacityA
            
            
            curCapacityB -= plants[r]
            curCapacityA -= plants[l]
            l += 1
            r -= 1
            
        if l == r and (curCapacityB < plants[r] and curCapacityA < plants[r]):
            refill += 1
            
        return refill